from audioop import avg
import numpy as np
import math
import matplotlib.pyplot as plt

'''
This is a class that has a field for an 8-bit bitstream ('byte_list') and 
has a method (modulator) that outputs an 80000 element 1-D array representing 
a time-series for the modulated signal

Fields: 
st -> modulated signal (using your choice of modulation)
Tstart -> start time 
Tstop -> stop time
Tstep -> time increment
resolution -> 1/Tstep (number of data points per second)
'''

class Modulator:
    def __init__(self, byte_list, Tstart, Tstop, Tstep, resolution):
        self.byte_list = byte_list
        self.Tstart = Tstart
        self.Tstop = Tstop
        self.Tstep = Tstep
        self.resolution = resolution

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

    def modulator(self, Tstart, Tstop, Tstep, byte):
        # noise_profile = np.random.normal(0,1,8*self.resolution)
        # noise_amplitude = 0.05
        Am = 0.5
        fm = 800
        Ac = 1
        fc = 8000
        Ka = 1

        t=np.arange(Tstart,Tstop,Tstep) # time
        mt=Am*np.cos(fm*t/1e6) # message
        ct=Ac*np.cos(fc*t/1e6) # carrier
        st=(1+Ka*mt)*ct * self.extend_byte(self.byte_convert(byte))# normal AM modulation
        # noisy_st = st + noise_profile * noise_amplitude
        return st
