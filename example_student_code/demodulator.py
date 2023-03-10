from audioop import avg
import numpy as np
import math
import matplotlib.pyplot as plt

'''
This is a class that has a field for a modulated signal ('st', a 80000 element 
1-D array representing a time-series) and has a method ('demodulator') that 
outputs an 8-bit bitstream representing the predicted demodulated bitstream

Fields: 
st -> modulated signal (using your choice of modulation)
Tstart -> start time 
Tstop -> stop time
Tstep -> time increment
resolution -> 1/Tstep (number of data points per second)
'''

class Demodulator:
    def __init__(self, st, Tstart, Tstop, Tstep, resolution):
        self.st = st
        self.Tstart = Tstart
        self.Tstop = Tstop
        self.Tstep = Tstep
        self.resolution = resolution

    def func_filter(self, Vrc, trc, Tau):
        grc=Vrc*np.exp(-1*trc/Tau)
        return grc

    def envelop_detector(self, st):
        t=np.arange(self.Tstart, self.Tstop, self.Tstep)
        Vc0=st[0]
        gt=self.func_filter(Vc0,0,1.5e4)
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

    def demodulator(self, rt):
        threshold_multiplier = 1.04

        rt = self.envelop_detector(self.st)
        recovered_list = []
        rt_sorted = sorted(rt)
        rt_sorted.sort()
        low_val = rt_sorted[0]
        high_val = rt_sorted[-1]
        avg_val = (low_val + high_val) / 2
        # print("Theshold: {} \nBit values: \n".format(avg_val * threshold_multiplier))
        for data_bit in range(len(8)):
            data_bit_range = rt[data_bit * self.resolution : (data_bit + 1) * self.resolution]
            # for rt_val in data_bit_range:
            avg_bit_val = sum(data_bit_range) / self.resolution
            # print(avg_bit_val)
            if avg_bit_val > avg_val * threshold_multiplier:
                recovered_list.append(1)
            else:
                recovered_list.append(0)
        return recovered_list

    