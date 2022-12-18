import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
ylim_min=-2
ylim_max=-0.5
#plt.ylim(ylim_min,ylim_max)
pathname='../out/'
name='net30_cor'
filename=pathname+name+'.txt'
y=np.loadtxt(filename)
x_min=1850
x_max=2100
x_min=1865
x_max=2086
nx=x_max-x_min+1
x=np.linspace(x_min,x_max,nx)
linewidth_value=3
color_name='peru'
plt.plot(x,y,color=color_name,linewidth=linewidth_value)
plt.grid()
plt.minorticks_on()
plt.tight_layout()
filename='/home/saga-t/work/python/fig/'+name+'.png'
plt.savefig(filename, dpi=300)
plt.show()
