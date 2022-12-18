import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=-0.4
xlim_max=0.4
plt.xlim(xlim_min,xlim_max)
ylim_min=0.3
ylim_max=4
plt.ylim(ylim_min, ylim_max)
dd=0.05
lam_eqs=np.arange(-1.,1.01,0.2)
epss=np.arange(0.1,4.05,dd)

nx=len(lam_eqs)
ny=len(epss)
#x=-F_2x/lam_eqs
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
CS = plt.contour(X,Y,Z,levels=[0.1614],colors=color_name,linewidths=linewidth_value)
#CS = plt.contour(X,Y,Z,levels=[0.1482,0.1718],colors=color_name,linestyles='dashed',linewidths=linewidth_value)
#plt.scatter(-a,1.22,color='blue')
a=0.331
xs=np.array([-a,a])
y_mins=np.array([ylim_min,ylim_min])
y_maxs=np.array([ylim_max,ylim_max])
plt.fill_between(xs,y_mins,y_maxs,edgecolor='None',color='gray',alpha=0.5)
plt.minorticks_on()
#plt.grid()
filename='../../../../fig/FigS6b'+'.png'
plt.savefig(filename, dpi=300)
plt.show()
