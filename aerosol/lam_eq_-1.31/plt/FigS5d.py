import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=1850
xlim_max=2021
plt.xlim(xlim_min,xlim_max)

x_min=1850
x_max=2019
nx=x_max-x_min+1
x=np.linspace(x_min,x_max,nx)
linewidth_value=3
pathname='../out/factor_0.0_eps_1.34/'
name='tas'
filename=pathname+name+'.txt'
y_median=np.loadtxt(filename)
pathname='../out/factor_-0.33_eps_1.34/'
filename=pathname+name+'.txt'
y=np.loadtxt(filename)
plt.plot(x,y-y_median,color='green',linewidth=linewidth_value)
pathname='../out/factor_0.33_eps_1.34/'
filename=pathname+name+'.txt'
y=np.loadtxt(filename)
plt.plot(x,y-y_median,color='red',linewidth=linewidth_value)

plt.grid()
plt.minorticks_on()
plt.tight_layout()
filename='../../../fig/FigS5d.eps'
plt.savefig(filename, dpi=300)

plt.show()
