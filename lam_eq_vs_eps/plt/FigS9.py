import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
F_2x=3.93
xlim_min=2
xlim_max=5
plt.xlim(xlim_min,xlim_max)
ylim_min=0.3
ylim_max=4
plt.ylim(ylim_min, ylim_max)
linewidth_value=2
plt.hlines(y=1,xmin=xlim_min,xmax=xlim_max,color='black',linestyle='dashed',linewidths=linewidth_value)

dd=0.05
lam_eqs=np.arange(-2.0,-0.4,dd)
epss=np.arange(0.,4.05,dd)

nx=len(lam_eqs)
ny=len(epss)
x=-F_2x/lam_eqs
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
CS=plt.contour(X,Y,Z,levels=[0.1614],colors='gray',linewidths=linewidth_value)
CS=plt.contour(X,Y,Z,levels=[0.1983],colors=color_name,linewidths=linewidth_value)
CS=plt.contour(X,Y,Z,levels=[0.1788,0.2178],colors=color_name,linestyles='dashed',linewidths=linewidth_value)


xs=np.array([2.5,4.])
y_mins=np.array([ylim_min,ylim_min])
y_maxs=np.array([ylim_max,ylim_max])
plt.fill_between(xs,y_mins,y_maxs,edgecolor='None',color='gray',alpha=0.5)

plt.minorticks_on()
#plt.grid()
filename='../../fig/FigS9.png'
plt.savefig(filename, dpi=300)
plt.show()
