import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=1.
xlim_max=8
plt.xlim(xlim_min,xlim_max)
ylim_min=0.5
ylim_max=2.1
plt.ylim(ylim_min,ylim_max)

pathname='../data/'
name='ECS'
filename=pathname+name+'.txt'
x=np.loadtxt(filename)
name='eps'
filename=pathname+name+'.txt'
y=np.loadtxt(filename)
color_name='black'
linewidth_value=3
plt.scatter(x,y,color=color_name,s=100,facecolor='none',linewidth=linewidth_value)
print(np.corrcoef(x,y)[0,1])

plt.minorticks_on()
#plt.grid()
filename='../../fig/FigS4b.eps'
plt.savefig(filename, dpi=300)
plt.show()
