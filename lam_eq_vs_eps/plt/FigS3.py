import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
F_2x=3.93
xlim_min=-1.6
xlim_max=-0.6
plt.xlim(xlim_min,xlim_max)
ylim_min=0.3
ylim_max=4
plt.ylim(ylim_min, ylim_max)

dd=0.05
lam_eqs=np.arange(-2.0,-0.4,dd)
epss=np.arange(0.,4.05,dd)

nx=len(lam_eqs)
ny=len(epss)
x=lam_eqs
y=epss
filename='../out/all/tas_trend_1961-2014.txt'
invalues=np.loadtxt(filename)
z=invalues*10
X,Y = np.meshgrid(x, y)
Z=z.reshape(nx,ny).T
plt.contourf(X, Y, Z,cmap="rainbow",levels=np.arange(0.075,0.35,0.025))
#plt.contourf(X, Y, Z,cmap="rainbow")
plt.colorbar(ticks=np.arange(0.1,0.6,0.1))
color_name='white'
linewidth_value=3
CS=plt.contour(X,Y,Z,levels=[0.1614],colors=color_name,linewidths=linewidth_value)
CS=plt.contour(X,Y,Z,levels=[0.1482,0.1718],colors=color_name,linestyles='dashed',linewidths=linewidth_value)

plt.xticks([-1.5,-1.0])
plt.minorticks_on()
#plt.grid()
filename='../../fig/FigS3.eps'
plt.savefig(filename, dpi=300)
plt.show()
