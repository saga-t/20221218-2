import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=1.
xlim_max=8
#plt.xlim(xlim_min,xlim_max)
ylim_min=0.5
ylim_max=2.1
#plt.ylim(ylim_min,ylim_max)
plt.gca().invert_xaxis()

pathname='../data/'
name='ECS'
filename=pathname+name+'.txt'
x=np.loadtxt(filename)
name='eps'
filename=pathname+name+'.txt'
y=np.loadtxt(filename)
color_name='black'
linewidth_value=3
#plt.scatter(x,y,color=color_name,s=100,facecolor='none',linewidth=linewidth_value)

width=np.array([-1.08,-0.92,-1.65,-2.31,-1.08])
y=np.array([4,3,2,1,0])
std=np.array([0.39,0.32,0.29,0.50,0.34])
plt.barh(y,width,xerr=std,capsize=8)

plt.yticks([])
#plt.axvline(x=-0.1,color="black",linewidth=1)
plt.gca().spines['right'].set_visible(False)
#plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().xaxis.set_ticks_position('top')

plt.minorticks_on()
#plt.grid()
filename='/home/saga-t/work/python/fig/barh_lambda'+'.eps'
plt.savefig(filename, dpi=300)
plt.show()
