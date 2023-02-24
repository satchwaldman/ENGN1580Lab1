import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import time
import sys
import numpy as np
from byte_to_AM import Byte_to_AM



fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

def animate(i):
    byte_list =[1,1,1,1,0,0,1,0]
    resolution = 10000
    noise_profile = np.random.normal(0,1,8*resolution)
    noise_amplitude = 0.4
    Am = 0.5
    fm = 800
    Ac = 1
    fc = 8000
    Ka = 1
    Tau = 1.5e4

    # create a Byte_to_AM object
    byte_to_AM = Byte_to_AM(byte_list, resolution, noise_profile, noise_amplitude, Am, fm, Ac, fc, Ka, Tau)

    # generate the AM signal
    Tstart = 0
    Tstop = 80000
    Tstep = 1
    mt, ct, st, noisy_st = byte_to_AM.AM_signal(Tstart, Tstop, Tstep, byte_to_AM.byte_list)

    # demodulate the signal
    rt = byte_to_AM.demodulate(noisy_st, Tstart, Tstop, Tstep)

    # recover back the bits
    threshold_multiplier = 1.04
    recovered_data = byte_to_AM.recover_data(rt, threshold_multiplier)

    # graph the byte signals
    input_bits = byte_to_AM.byte_grapher(byte_list)
    output_bits = byte_to_AM.byte_grapher(recovered_data)

    byte_to_AM.write_to_txt(input_bits, 'data/team_1_data/input_byte.txt')
    byte_to_AM.write_to_txt(mt, 'data/team_1_data/message_signal.txt')
    byte_to_AM.write_to_txt(ct, 'data/team_1_data/carrier_signal.txt')
    byte_to_AM.write_to_txt(st, 'data/team_1_data/sent_signal.txt')
    byte_to_AM.write_to_txt(rt, 'data/team_1_data/received_signal.txt')
    byte_to_AM.write_to_txt(noise_profile, 'data/team_1_data/noise.txt')
    byte_to_AM.write_to_txt(output_bits, 'data/team_1_data/output_byte.txt')

    pullData1 = open("data/team_1_data/sent_signal.txt","r").read()
    dataArray1 = pullData1.split('\n')
    xar1 = []
    yar1 = []

    pullData2 = open("data/team_2_data/sent_signal.txt","r").read()
    dataArray2 = pullData2.split('\n')
    xar2 = []
    yar2 = []

    for eachLine in dataArray1:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar1.append(int(x))
            yar1.append(int(y))
    
    for eachLine in dataArray2:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar2.append(int(x))
            yar2.append(int(y))
    ax1.clear()
    ax1.plot(xar1,yar1)
    ax2.clear()
    ax2.plot(xar2,yar2)
ani = animation.FuncAnimation(fig, animate, interval=3000)

plt.show()