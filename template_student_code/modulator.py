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

    ### ------------------------ HELPER METHODS -----------------------------###
    def extend_byte(self, list):
        '''
        Helper method to convert an 8-bit bitstream into an 80000 element 1-D 
        array. Each 10000 elements represent 1 bit.
        '''
        ret_list = []
        for i in list:
            for j in range(self.resolution):
                ret_list.append(i)
        return ret_list

    ### ---------------------------------------------------------------------###

    def modulator(self, Tstart, Tstop, Tstep, byte):
        '''
        TODO: Write this method to create a modulated signal using a 
        modulation scheme of your choosing
        '''
        pass
