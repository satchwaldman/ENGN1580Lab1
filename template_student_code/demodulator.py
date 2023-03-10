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

    ### ------------------------ HELPER METHODS -----------------------------###

    def func_filter(self, Vrc, trc, Tau):
        grc=Vrc*np.exp(-1*trc/Tau)
        return grc

    def envelop_detector(self, st):
        '''
        Helper method that takes in a time-series signal (80000 element 1-D 
        array) and returns the output of this signal passing through an envelop 
        detector
        '''
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

    ### ---------------------------------------------------------------------###

    def demodulator(self, rt):
        '''
        TODO: Write a method to decode the noisy, received signal, using a
        demodulation scheme of your choosing.
        '''
        pass

    