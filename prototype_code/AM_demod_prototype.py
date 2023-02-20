# import pygame module in this program
#import pygame
from math import sin
from pydoc import resolve
from random import sample
import numpy as np
import matplotlib.pyplot as plt

resolution = 10000 # points per second

noise_to_left = np.random.normal(0,1,8*resolution)
noise_to_right = np.random.normal(0,1,8*resolution)

left_byte = [0,0,0,0,0,0,0,0] 
right_byte = [0,0,0,0,0,0,0,0]

left_byte_true = [1,1,1,1,0,0,1,0]
right_byte_true = [0,0,0,0,1,1,1,1]

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

t = np.linspace(0, 8, 8 * resolution)

def compute_AM_list(message_list, f_message, f_carrier):
	ret_list = []
	for t_ms in range(len(message_list)):
		curr_val = message_list[t_ms] * sin(t[t_ms] * f_message) * sin(t[t_ms] * f_carrier)
		ret_list.append(curr_val)
	return ret_list

n_spikes_per_message_bit = 2
carrier_freq = 100
signal_list = compute_AM_list(extend_byte(byte_convert(left_byte_true)), np.pi * n_spikes_per_message_bit, carrier_freq)

noise_factor = .2
noisy_sig_list = np.array(signal_list) + noise_factor * np.array(noise_to_left)

plt.subplot(3,1,1)
plt.plot(signal_list)
plt.ylabel('original signal')

plt.subplot(3,1,2)
plt.plot(noise_to_left)
plt.ylabel('noise')

plt.subplot(3,1,3)
plt.plot(noisy_sig_list)
plt.ylabel('noisy signal')
plt.show()

# ------------------- AMPLITUDE DEMODULATION -----------------------------------

# def rectify(list):
# 	ret_list = []
# 	for i in list:
# 		if i >= 0:
# 			ret_list.append(i)
# 		else:
# 			ret_list.append(0)


# ------------------------ unclear how this works -----------------------------
# def func_filter(Vrc,trc,Tau):
#       #B=1/(2*math.pi*Tau)
#   #gt1=Vc0*math.exp(-1*2*math.pi*B*ti)
#   grc=Vrc*np.exp(-1*trc/Tau)
#   return grc

# Tau=3/1000
# st = signal_list# st is the normal AM signal (i.e., sent)

# Vc0=st[0]
# gt=func_filter(Vc0,0,Tau)
# rt=[]
# T=0
# t1=[]
# for cnt in range(len(t)):
#   if st[cnt]>=gt:
#     rt.append(st[cnt])
#     T=t[cnt]
#     Vc0=st[cnt]
#     gt=st[cnt]
#   else:
#     t1.append(t[cnt]-T)
#     rt.append(gt)
#     gt=func_filter(Vc0,t[cnt]-T,Tau)

# plt.plot(rt)
# plt.show()



# what variables can they play with to change the robustness/speed trade off:
# noise factor, f_message, f_carrier, noise profile (guassian, etc), noise addition function (addition, multiplication, etc),
# demodulation scheme (envelop detector vs rectifier and LPF), Tau (RC constant)
# -- Maybe they shoudl code their own demod scheme to affect its robustness (but we impose some constraints)

# !!! how to actually demodulate (and return to a list of binary numbers)?
# we can get back to a "demodulated signal" but we still need a classifier to figure out the boundary between a 1 and a 0
# Should this just be a simple thesehold/historosis? or do we need to do an integral

# Noise profile and SNR power ratio


# #A_c = float(input('Enter carrier amplitude: '))
# #f_c = float(input('Enter carrier frquency: '))
# A_c_left = 1
# f_c_left = 1e2
# A_c_right = 1
# f_c_right = 1e2

# A_m_left = 1
# f_m_left = 1e1
# A_m_right = 1
# f_m_right = 1e1
# # modulation_index = float(input('Enter modulation index: '))
# modulation_index = 1

# t = np.linspace(0, 1, 1000)

# carrier_left = A_c_left*np.cos(2*np.pi*f_c_left*t)
# modulator_left = A_m_left*np.cos(2*np.pi*f_m_left*t)
# product_left = A_c_left*(1+modulation_index*np.cos(2*np.pi*f_m_left*t))*np.cos(2*np.pi*f_c_left*t)

# carrier_right = A_c_right*np.cos(2*np.pi*f_c_right*t)
# modulator_right = A_m_right*np.cos(2*np.pi*f_m_right*t)
# product_right = A_c_right*(1+modulation_index*np.cos(2*np.pi*f_m_right*t))*np.cos(2*np.pi*f_c_right*t)

# plt.subplot(3,1,1)
# plt.title('Amplitude Modulation')
# plt.plot(modulator_left,'g')
# plt.ylabel('Amplitude')
# plt.xlabel('Message signal left')

# plt.subplot(3,1,2)
# plt.plot(carrier_left, 'r')
# plt.ylabel('Amplitude')
# plt.xlabel('Carrier signal left')

# plt.subplot(3,1,3)
# plt.plot(product_left, color="purple")
# plt.ylabel('Amplitude')
# plt.xlabel('AM signal left')

# plt.subplots_adjust(hspace=1)
# plt.rc('font', size=15)
# fig = plt.gcf()
# plt.show()

# plt.subplot(3,1,1)
# plt.title('Amplitude Modulation')
# plt.plot(modulator_left,'g')
# plt.ylabel('Amplitude')
# plt.xlabel('Message signal right')

# plt.subplot(3,1,2)
# plt.plot(carrier_right, 'r')
# plt.ylabel('Amplitude')
# plt.xlabel('Carrier signal right')

# plt.subplot(3,1,3)
# plt.plot(product_right, color="purple")
# plt.ylabel('Amplitude')
# plt.xlabel('AM signal right')

# plt.subplots_adjust(hspace=1)
# plt.rc('font', size=15)
# fig = plt.gcf()
# plt.show()
# ------------------------------------------------------------------------------

# # activate the pygame library .
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()

# # create the display surface object
# # of specific dimension..e(500, 500).
# win = pygame.display.set_mode((500, 500))

# # set the pygame window name
# pygame.display.set_caption("Moving rectangle")

# # object current co-ordinates
# x = 200
# y = 200

# # dimensions of the object
# width = 20
# height = 20

# # velocity / speed of movement
# vel = 1



# # Indicates pygame is running
# run = True

# # infinite loop
# while run:
# 	# creates time delay of 10ms
# 	pygame.time.delay(1000)
	
# 	# iterate over the list of Event objects
# 	# that was returned by pygame.event.get() method.
# 	for event in pygame.event.get():
		
# 		# if event object type is QUIT
# 		# then quitting the pygame
# 		# and program both.
# 		if event.type == pygame.QUIT:
			
# 			# it will make exit the while loop
# 			run = False
# 	# stores keys pressed
# 	keys = pygame.key.get_pressed()
	
# 	# if left arrow key is pressed
# 	if keys[pygame.K_LEFT] and x>0:
		
# 		# decrement in x co-ordinate
# 		x -= vel
		
# 	# if left arrow key is pressed
# 	if keys[pygame.K_RIGHT] and x<500-width:
		
# 		# increment in x co-ordinate
# 		x += vel
		
# 	# if left arrow key is pressed
# 	if keys[pygame.K_UP] and y>0:
		
# 		# decrement in y co-ordinate
# 		y -= vel
		
# 	# if left arrow key is pressed
# 	if keys[pygame.K_DOWN] and y<500-height:
# 		# increment in y co-ordinate
# 		y += vel
		
			
# 	# completely fill the surface object
# 	# with black colour
# 	win.fill((0, 0, 0))
	
# 	# drawing object on screen which is rectangle here
# 	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	
# 	# it refreshes the window
# 	pygame.display.update()

# # closes the pygame window

# #pygame.quit()

# # 
