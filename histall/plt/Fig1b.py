import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=1850
xlim_max=2100
plt.xlim(xlim_min,xlim_max)
ylim_min=-0.8
ylim_max=3.5
plt.ylim(ylim_min,ylim_max)

name='tas'
pathname='../out/lam_eq_-1.57_eps_1.34/'
filename=pathname+name+'.txt'
y_min=np.loadtxt(filename)
pathname='../out/lam_eq_-0.98_eps_1.34/'
filename=pathname+name+'.txt'
y_max=np.loadtxt(filename)
x_min=1850
x_max=2100
nx=x_max-x_min+1
x=np.linspace(x_min,x_max,nx)
linewidth_value=3
color_name='green'
alpha_value=0.2
plt.fill_between(x,y_min,y_max,color=color_name,alpha=alpha_value)

pathname=''
name='HadCRUT5'
filename=pathname+name+'.txt'
obs=np.loadtxt(filename)
x=np.linspace(1850,2021,172)
y=obs
color_name='black'
plt.plot(x,y,color=color_name,linewidth=linewidth_value)

#plt.grid()
plt.minorticks_on()
plt.tight_layout()
filename='../../fig/Fig1b.eps'
plt.savefig(filename, dpi=300)

plt.show()
