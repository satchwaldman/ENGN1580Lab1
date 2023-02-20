import numpy as np
import matplotlib.pyplot as plt
from byte_to_AM import Byte_to_AM

# Create values for each input
byte_list =[1,1,1,1,0,0,1,0]
resolution = 10000
noise_profile = np.random.normal(0,1,8*resolution)
noise_amplitude = 1
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
threshold_multiplier = 1
recovered_data = byte_to_AM.recover_data(rt, threshold_multiplier)

# graph the byte signals
input_bits = byte_to_AM.byte_grapher(byte_list)
output_bits = byte_to_AM.byte_grapher(recovered_data)

# plot the signals
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
# ax1.plot(np.arange(len(st))*Tstep, st)
# ax1.set_title('Amplitude Modulated Signal')
# ax1.set_xlabel('Time (s)')
# ax1.set_ylabel('Amplitude')

# ax2.plot(np.arange(len(rt))*Tstep, rt)
# ax2.set_title('Demodulated Signal')
# ax2.set_xlabel('Time (s)')
# ax2.set_ylabel('Amplitude')

# plt.tight_layout()
def make_plots():
    plt.subplot(8,1,1)
    plt.plot(input_bits)
    plt.subplot(8,1,2)
    plt.plot(mt)
    plt.subplot(8,1,3)
    plt.plot(ct)
    plt.subplot(8,1,4)
    plt.plot(st)
    plt.subplot(8,1,5)
    plt.plot(noise_profile)
    plt.subplot(8,1,6)
    plt.plot(noisy_st)
    plt.subplot(8,1,7)
    plt.plot(rt)
    plt.subplot(8,1,8)
    plt.plot(output_bits)
    plt.show()
make_plots()