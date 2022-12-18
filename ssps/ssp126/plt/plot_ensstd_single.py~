import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 18

xlim_min=1850
xlim_max=2018
#plt.xlim(xlim_min,xlim_max)

ylim_min=-3
ylim_max=3
#plt.ylim(ylim_min,ylim_max)
linewidth_value=3
#plt.axhline(y=-1.44,color='g',linewidth=linewidth_value,linestyle='dashed')

pathname='../out/ensmean/'
name='tod'
filename=pathname+name+'.txt'
ensmean=np.loadtxt(filename)
pathname='../out/ensstd/'
filename=pathname+name+'.txt'
ensstd=np.loadtxt(filename)
#x=np.linspace(1865,2004,140)
x_min=1850
x_max=2100
nx=x_max-x_min+1
x=np.linspace(x_min,x_max,nx)
y=ensmean
color_name='peru'
linewidth_value=3
plt.plot(x,y,color=color_name,linewidth=linewidth_value)
alpha_value=0.2
plt.fill_between(x,y-ensstd,y+ensstd,color=color_name,alpha=alpha_value)



plt.grid()
plt.minorticks_on()
plt.tight_layout()
extension='.png'
filename='/home/saga-t/work/python/fig/'+name+extension
plt.savefig(filename, dpi=300)
plt.show()
