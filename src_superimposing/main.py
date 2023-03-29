import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import time
import sys
import numpy as np
# from byte_to_AM import Byte_to_AM
# from example_student_code.demodulator import Demodulator
# from example_student_code.modulator import Modulator

from demodulator import Demodulator
from modulator import Modulator

### ---------------------------- Create Subplots -------------------------------
# displayRT = True

rows = 7
# if displayRT:
#     rows = 8

fig = plt.figure()
ax1_input_bits = fig.add_subplot(rows,2,1)
ax2_input_bits = fig.add_subplot(rows,2,2)
ax1_mt = fig.add_subplot(rows,2,3)
ax2_mt = fig.add_subplot(rows,2,4)
ax1_ct = fig.add_subplot(rows,2,5)
ax2_ct = fig.add_subplot(rows,2,6)
ax1_st = fig.add_subplot(rows,2,7)
ax2_st = fig.add_subplot(rows,2,8)
ax1_noise = fig.add_subplot(rows,2,9)
ax2_noise = fig.add_subplot(rows,2,10)
ax1_noisy_st = fig.add_subplot(rows,2,11)
ax2_noisy_st = fig.add_subplot(rows,2,12)

# if rows == 7:
ax1_output_bits = fig.add_subplot(rows,2,13)
ax2_output_bits = fig.add_subplot(rows,2,14)

# else: # rows == 8:
#     ax1_rt = fig.add_subplot(8,2,13)
#     ax2_rt = fig.add_subplot(8,2,14)
#     ax1_output_bits = fig.add_subplot(rows,2,15)
#     ax2_output_bits = fig.add_subplot(rows,2,16)

### ------------------ Helper Methods for Plotting Bits ------------------------
resolution = 10000

def byte_convert(list):
        ret_list = []
        for i in range(len(list)):
            ret_list.append((list[i] + 1) / 2)
        return ret_list

def extend_byte(list):
        ret_list = []
        for i in list:
            for j in range(resolution):
                ret_list.append(i)
        return ret_list

def byte_grapher(byte):
        return extend_byte(byte_convert(byte))

### ---------------------------- Create Live Animation -------------------------

def animate(i):
    # generate time values
    Tstart = 0
    Tstop = 80000
    Tstep = 1
    t = np.arange(0,8e4,1)

    # ------------------ TEAM 1 ---------------------
    byte_list1 =[1,0,1,0,1,0,1,1]
    resolution1 = 10000
    noise_profile1 = np.random.normal(0,1,8*resolution1)
    noise_amplitude1 = 0.1
    Am1 = 0.5
    fm1 = 800
    Ac1 = 1
    fc1 = 8000

    # create a modulator object
    modulator1 = Modulator(byte_list1, Tstart, Tstop, Tstep, resolution1)

    # generate mt and ct signals
    mt1=Am1*np.cos(fm1*t/1e6) # message
    ct1=Ac1*np.cos(fc1*t/1e6) # carrier

    # generate the SENT signal
    st1 = modulator1.modulator(Tstart, Tstop, Tstep, byte_list1)

    # add noise to the sent signal 
    noisy_st1 = st1 + noise_profile1 * noise_amplitude1

    # create a modulator object
    demodulator1 = Demodulator(st1, Tstart, Tstop, Tstep, resolution1)

    # demodulate the signal and recover back the bits
    recovered_data1 = demodulator1.demodulator(noisy_st1)

    # graph the byte signals
    input_bits1 = byte_grapher(byte_list1)
    output_bits1 = byte_grapher(recovered_data1)
    
    ax1_input_bits.clear()
    ax1_input_bits.plot(t,input_bits1)
    ax1_mt.clear()
    ax1_mt.plot(t,mt1)
    ax1_ct.clear()
    ax1_ct.plot(t,ct1)
    ax1_st.clear()
    ax1_st.plot(t,st1)
    ax1_noise.clear()
    ax1_noise.plot(t,noise_profile1)
    ax1_noisy_st.clear()
    ax1_noisy_st.plot(t,noisy_st1)
    # if displayRT:
    #     ax1_rt.clear()
    #     ax1_rt.plot(t,rt1)
    ax1_output_bits.clear()
    ax1_output_bits.plot(t,output_bits1)

    # ------------------ TEAM 2 ---------------------

    byte_list2 =[1,0,1,0,1,0,1,1]
    resolution2 = 10000
    noise_profile2 = np.random.normal(0,1,8*resolution2)
    noise_amplitude2 = .2
    Am2 = 0.5
    fm2 = 800
    Ac2 = 1
    fc2 = 8000

    # create a modulator object
    modulator2 = Modulator(byte_list2, Tstart, Tstop, Tstep, resolution2)

    # generate mt and ct signals
    mt2=Am2*np.cos(fm2*t/1e6) # message
    ct2=Ac2*np.cos(fc2*t/1e6) # carrier

    # generate the SENT signal
    st2 = modulator2.modulator(Tstart, Tstop, Tstep, byte_list2)

    # add noise to the sent signal 
    noisy_st2 = st2 + noise_profile2 * noise_amplitude2

    # create a modulator object
    demodulator2 = Demodulator(st2, Tstart, Tstop, Tstep, resolution2)

    # demodulate the signal and recover back the bits
    recovered_data2 = demodulator2.demodulator(noisy_st2)

    # graph the byte signals
    input_bits2 = byte_grapher(byte_list2)
    output_bits2 = byte_grapher(recovered_data2)
    
    ax2_input_bits.clear()
    ax2_input_bits.plot(t,input_bits2)
    ax2_mt.clear()
    ax2_mt.plot(t,mt2)
    ax2_ct.clear()
    ax2_ct.plot(t,ct2)
    ax2_st.clear()
    ax2_st.plot(t,st2)
    ax2_noise.clear()
    ax2_noise.plot(t,noise_profile2)
    ax2_noisy_st.clear()
    ax2_noisy_st.plot(t,noisy_st2)
    ax2_output_bits.clear()
    ax2_output_bits.plot(t,output_bits2)

ani = animation.FuncAnimation(fig, animate, interval=500)

plt.show()