from audioop import avg
import numpy as np
import math
import matplotlib.pyplot as plt

class Byte_to_AM:
    def __init__(self, byte_list, resolution, noise_profile, noise_amplitude, Am, fm, Ac, fc, Ka, Tau):
        self.byte_list = byte_list
        self.resolution = resolution
        self.noise_profile = noise_profile
        self.noise_amplitude = noise_amplitude
        self.Am = Am
        self.fm = fm
        self.Ac = Ac
        self.fc = fc
        self.Ka = Ka
        self.Tau = Tau

    def func_filter(self, Vrc, trc, Tau):
        #B=1/(2*math.pi*Tau)
        #gt1=Vc0*math.exp(-1*2*math.pi*B*ti)
        grc=Vrc*np.exp(-1*trc/Tau)
        return grc

    def byte_convert(self, list):
        ret_list = []
        for i in range(len(list)):
            ret_list.append((list[i] + 1) / 2)
        return ret_list

    def extend_byte(self, list):
        ret_list = []
        for i in list:
            for j in range(self.resolution):
                ret_list.append(i)
        return ret_list

    
    
    # Tstart=0
    # Tstop=8/100 * 1e6
    # Tstep=0.0001/100 * 1e6
    def AM_signal(self, Tstart, Tstop, Tstep, byte):
        t=np.arange(Tstart,Tstop,Tstep) # time
        mt=self.Am*np.cos(self.fm*t/1e6) # message
        ct=self.Ac*np.cos(self.fc*t/1e6) # carrier
        st=(1+self.Ka*mt)*ct * self.extend_byte(self.byte_convert(byte))# normal AM modulation
        noisy_st = st + self.noise_profile*self.noise_amplitude
        # At=np.abs(Ac*(1+Ka*mt))
        return mt, ct, st, noisy_st
    
    def demodulate(self, st, Tstart, Tstop, Tstep):
        t=np.arange(Tstart,Tstop,Tstep)
        Vc0=st[0]
        gt=self.func_filter(Vc0,0,self.Tau)
        rt=[]
        T=0
        t1=[]
        for cnt in range(len(t)):
            if st[cnt]>=gt:
                rt.append(st[cnt])
                T=t[cnt]
                Vc0=st[cnt]
                gt=st[cnt]
            else:
                t1.append(t[cnt]-T)
                rt.append(gt)
                gt=self.func_filter(Vc0,t[cnt]-T,self.Tau)
        return rt

    def new_sort(self, ls):
        ls.sort()
        return ls

    def recover_data(self, rt, threshold_multiplier):
        recovered_list = []
        rt_sorted = sorted(rt)
        rt_sorted.sort()
        low_val = rt_sorted[0]
        high_val = rt_sorted[-1]
        avg_val = (low_val + high_val) / 2
        print("Theshold: {} \nBit values: \n".format(avg_val * threshold_multiplier))
        for data_bit in range(len(self.byte_list)):
            data_bit_range = rt[data_bit * self.resolution : (data_bit + 1) * self.resolution]
            # for rt_val in data_bit_range:
            avg_bit_val = sum(data_bit_range) / self.resolution
            print(avg_bit_val)
            if avg_bit_val > avg_val * threshold_multiplier:
                recovered_list.append(1)
            else:
                recovered_list.append(0)
        return recovered_list

    def byte_grapher(self, byte):
        return self.extend_byte(self.byte_convert(byte))

    def write_to_txt(self, signal, path):
        with open(path, 'w') as f:
            inc = 0
            for val in signal:
                f.write(str(inc))
                f.write(',')
                f.write(str(int(np.ceil(val * 1e5))))
                f.write('\n')
                inc += 1
