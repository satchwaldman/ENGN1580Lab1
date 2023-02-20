import numpy as np
import math
import matplotlib.pyplot as plt

def func_filter(Vrc,trc,Tau):
      #B=1/(2*math.pi*Tau)
  #gt1=Vc0*math.exp(-1*2*math.pi*B*ti)
  grc=Vrc*np.exp(-1*trc/Tau)
  return grc

# Am=1 # amplitude of message signal
# fm=3 * math.pi # frequency of message signal
# Ac=1 # amplitude of carrier signal
# fc=100 # fequency of carrier signal
# Ka=1 # amplitude sensitivity
# Tau=3/1000

# # Tstart=0
# # Tstop=4/fm
# # Tstep=0.00002/fm
# resolution = 10000
# # t=np.arange(Tstart,Tstop,Tstep) # time
# t = np.linspace(0, 8, 8 * resolution)
# st = []
# for t_ms in range(len(t)):
#     mt=Am*np.cos(fm*t[t_ms]) # message
#     ct=Ac*np.cos(fc*t[t_ms]) # carrier
#     st.append(mt * ct)
# # st=(1+Ka*mt)*ct # normal AM modulation
# At=np.abs(Ac*(1+Ka*mt))

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

# # print('Tc = {}, Tau = {}, Tm = {}'.format(1/fc,Tau,1/fm))

# # f = plt.figure()#figsize=(15,10))
# # ax1 = f.add_subplot(221)
# # ax2 = f.add_subplot(222)
# # ax3 = f.add_subplot(223)
# # ax4 = f.add_subplot(224)

# # ax1.plot(t,rt,'k',label='$r(t)$')
# # ax1.plot(t,At,'b--',label='$|A(t)|$')
# # ax1.plot(t,-1*At,'k--',label='$-|A(t)|$')
# # ax1.plot(t,st,'r:',label='$s(t)$')
# # ax1.set_xlabel('time (sec)')
# # ax1.legend()

# # ymin, ymax = ax1.get_ylim()
# # ax2.plot(t,rt,'k',label='$r(t)$')
# # ax2.plot(t,mt,'y--',label='$m(t)$')
# # ax2.set_xlabel('time (sec)')
# # ax2.set_ylabel('$r(t)$ (v)')
# # ax2.set_ylim([ymin, ymax])
# # ax2.legend()

# # ax3.plot(t,rt,'k')
# # ax3.plot(t,At,'b--')
# # ax3.plot(t,-1*At,'k--')
# # ax3.plot(t,st,'r:')
# # ax3.set_xlabel('time (sec)')
# # ax3.set_xlim([0, 1/fm])

# # ax4.plot(t,rt,'k')
# # ax4.plot(t,mt,'y--')
# # ax4.set_xlabel('time (sec)')
# # ax4.set_ylabel('$r(t)$ (v)')
# # ax4.set_ylim([ymin, ymax])
# # ax4.set_xlim([0, 1/fm])

# # plt.show()



# ----------------------------------------------------------------------------
resolution = 10000
noise_profile = np.random.normal(0,1,8*resolution)

byte = [0,0,0,0,1,1,1,1]
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

Am=0.5 # amplitude of message signal
fm=800 # frequency of message signal
Ac=1 # amplitude of carrier signal
fc=8000 # fequency of carrier signal
Ka=1 # amplitude sensitivity
Tau=3/1000 * 5e6

Tstart=0
Tstop=8/100 * 1e6
Tstep=0.0001/100 * 1e6
# t = np.linspace(0,8,80000)
t=np.arange(Tstart,Tstop,Tstep) # time
mt=Am*np.cos(fm*t/1e6) # message
ct=Ac*np.cos(fc*t/1e6) # carrier
st=(1+Ka*mt)*ct * extend_byte(byte_convert(byte))# normal AM modulation
noisy_st = st + noise_profile*(0.2)
At=np.abs(Ac*(1+Ka*mt))

Vc0=st[0]
gt=func_filter(Vc0,0,Tau)
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
    gt=func_filter(Vc0,t[cnt]-T,Tau)



# Vc0_noise=noisy_st[0]
# gt_noise=func_filter(Vc0_noise,0,Tau)
# rt_noise=[]
# T_noise=0
# t1_noise=[]
# for cnt in range(len(t)):
#   if noisy_st[cnt]>=gt_noise:
#     rt_noise.append(noisy_st[cnt])
#     T_noiseT=t[cnt]
#     Vc0_noise=noisy_st[cnt]
#     gt_noise=noisy_st[cnt]
#   else:
#     t1_noise.append(t[cnt]-T_noise)
#     rt_noise.append(gt_noise)
#     gt_noise=func_filter(Vc0_noise,t[cnt]-T_noise,Tau)

Vc0=noisy_st[0]
gt=func_filter(Vc0,0,Tau)
rt_noise=[]
T=0
t1=[]
for cnt in range(len(t)):
  if st[cnt]>=gt:
    rt_noise.append(st[cnt])
    T=t[cnt]
    Vc0=st[cnt]
    gt=st[cnt]
  else:
    t1.append(t[cnt]-T)
    rt_noise.append(gt)
    gt=func_filter(Vc0,t[cnt]-T,Tau)


# print('Tc = {}, Tau = {}, Tm = {}'.format(1/fc,Tau,1/fm))

# f = plt.figure(figsize=(15,10))
# ax1 = f.add_subplot(221)
# ax2 = f.add_subplot(222)
# ax3 = f.add_subplot(223)
# ax4 = f.add_subplot(224)

# ax1.plot(t,rt,'k',label='$r(t)$')
# ax1.plot(t,At,'b--',label='$|A(t)|$')
# ax1.plot(t,-1*At,'k--',label='$-|A(t)|$')
# ax1.plot(t,st,'r:',label='$s(t)$')
# ax1.set_xlabel('time (sec)')
# ax1.legend()

# plt.show()

# print(rt)
plt.subplot(7,1,1)
plt.plot(mt)
plt.subplot(7,1,2)
plt.plot(ct)
plt.subplot(7,1,3)
plt.plot(st)
plt.subplot(7,1,4)
plt.plot(rt)
plt.subplot(7,1,5)
plt.plot(noise_profile)
plt.subplot(7,1,6)
plt.plot(noisy_st)
plt.subplot(7,1,7)
plt.plot(rt_noise)
plt.show()

# print(len(st))
# print(len(noise_profile))
