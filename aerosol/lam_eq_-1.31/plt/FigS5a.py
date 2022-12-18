import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=1850
xlim_max=2019
plt.xlim(xlim_min,xlim_max)

x=np.linspace(1850,2019,170)
pathname='../DF/'
name='DF'
filename=pathname+name+'.txt'
y=np.loadtxt(filename)
color_name='black'
linewidth_value=3
plt.plot(x,y,color=color_name,linewidth=linewidth_value)

pathname='../DF/'
name='DF_aerosol_std'
filename=pathname+name+'.txt'
std=np.loadtxt(filename)
plt.fill_between(x,y+std,y-std,color=color_name,alpha=0.2)

pathname='../DF/'
name='DF_aerosol'
filename=pathname+name+'.txt'
add=np.loadtxt(filename)
add=add*0.331
color_name='red'
plt.plot(x,y+add,color=color_name,linewidth=linewidth_value)
color_name='green'
plt.plot(x,y-add,color=color_name,linewidth=linewidth_value)

plt.grid()
plt.minorticks_on()
plt.tight_layout()
filename='../../../fig/FigS5a.png'
plt.savefig(filename, dpi=300)

plt.show()
