import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import time
import sys
import numpy as np
from byte_to_AM import Byte_to_AM



fig = plt.figure()
ax1_input_bits = fig.add_subplot(7,2,1)
ax2_input_bits = fig.add_subplot(7,2,2)
ax1_mt = fig.add_subplot(7,2,3)
ax2_mt = fig.add_subplot(7,2,4)
ax1_ct = fig.add_subplot(7,2,5)
ax2_ct = fig.add_subplot(7,2,6)
ax1_st = fig.add_subplot(7,2,7)
ax2_st = fig.add_subplot(7,2,8)
ax1_noise = fig.add_subplot(7,2,9)
ax2_noise = fig.add_subplot(7,2,10)
ax1_rt = fig.add_subplot(7,2,11)
ax2_rt = fig.add_subplot(7,2,12)
ax1_output_bits = fig.add_subplot(7,2,13)
ax2_output_bits = fig.add_subplot(7,2,14)

def animate(i):
    # generate time values
    Tstart = 0
    Tstop = 80000
    Tstep = 1
    t = np.arange(0,8e4,1)

    # ------------------ TEAM 1 ---------------------
    byte_list1 =[1,1,1,1,0,0,1,0]
    resolution1 = 10000
    noise_profile1 = np.random.normal(0,1,8*resolution1)
    noise_amplitude1 = 0.1
    Am1 = 0.5
    fm1 = 800
    Ac1 = 1
    fc1 = 8000
    Ka1 = 1
    Tau1 = 1.5e4

    # create a Byte_to_AM object
    byte_to_AM1 = Byte_to_AM(byte_list1, resolution1, noise_profile1, noise_amplitude1, Am1, fm1, Ac1, fc1, Ka1, Tau1)

    # generate the AM signals
    mt1, ct1, st1, noisy_st1 = byte_to_AM1.AM_signal(Tstart, Tstop, Tstep, byte_to_AM1.byte_list)

    # demodulate the signal
    rt1 = byte_to_AM1.demodulate(noisy_st1, Tstart, Tstop, Tstep)

    # recover back the bits
    threshold_multiplier1 = 1.04
    recovered_data1 = byte_to_AM1.recover_data(rt1, threshold_multiplier1)

    # graph the byte signals
    input_bits1 = byte_to_AM1.byte_grapher(byte_list1)
    output_bits1 = byte_to_AM1.byte_grapher(recovered_data1)
    
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
    ax1_rt.clear()
    ax1_rt.plot(t,rt1)
    ax1_output_bits.clear()
    ax1_output_bits.plot(t,output_bits1)

    # ------------------ TEAM 2 ---------------------

    byte_list2 =[1,1,1,1,0,0,1,0]
    resolution2 = 10000
    noise_profile2 = np.random.normal(0,1,8*resolution2)
    noise_amplitude2 = 0.3
    Am2 = 0.5
    fm2 = 800
    Ac2 = 1
    fc2 = 8000
    Ka2 = 1
    Tau2 = 1.5e4

    # create a Byte_to_AM object
    byte_to_AM2 = Byte_to_AM(byte_list2, resolution2, noise_profile2, noise_amplitude2, Am2, fm2, Ac2, fc2, Ka2, Tau2)

    # generate the AM signals
    mt2, ct2, st2, noisy_st2 = byte_to_AM2.AM_signal(Tstart, Tstop, Tstep, byte_to_AM1.byte_list)

    # demodulate the signal
    rt2 = byte_to_AM2.demodulate(noisy_st2, Tstart, Tstop, Tstep)

    # recover back the bits
    threshold_multiplier2 = 1.04
    recovered_data2 = byte_to_AM1.recover_data(rt1, threshold_multiplier2)

    # graph the byte signals
    input_bits2 = byte_to_AM1.byte_grapher(byte_list2)
    output_bits2 = byte_to_AM1.byte_grapher(recovered_data2)
    
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
    ax2_rt.clear()
    ax2_rt.plot(t,rt2)
    ax2_output_bits.clear()
    ax2_output_bits.plot(t,output_bits2)

ani = animation.FuncAnimation(fig, animate, interval=500)

plt.show()