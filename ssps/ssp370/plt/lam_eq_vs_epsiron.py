import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=-1.6
xlim_max=-0.5
plt.xlim(xlim_min,xlim_max)
ylim_min=0.3
ylim_max=4
plt.ylim(ylim_min, ylim_max)
plt.axvline(x=-1.03,color='green',linestyle='dashed')
plt.axvline(x=-1.54,color='green',linestyle='dashed')
plt.axvline(x=-0.62,color='green',linestyle='dashed')
plt.axhline(y=1.34,color='green',linestyle='dashed')
plt.axhline(y=1.75,color='green',linestyle='dashed')
plt.axhline(y=0.93,color='green',linestyle='dashed')

dd=0.05
lam_eqs=np.arange(-1.6,-0.4,dd)
epss=np.arange(0.1,4.05,dd)

nx=len(lam_eqs)
ny=len(epss)
#x=-F_2x/lam_eqs
x=lam_eqs
y=epss
filename='../out/all/tas_trend_1981-2014.txt'
invalues=np.loadtxt(filename)
z=invalues*10
X,Y = np.meshgrid(x, y)
Z=z.reshape(nx,ny).T
plt.contourf(X, Y, Z,cmap="rainbow",levels=np.arange(0.1,0.55,0.05))
#plt.contourf(X, Y, Z,cmap="rainbow")
plt.colorbar(ticks=np.arange(0.1,0.6,0.1))
color_name='black'
obs=0.176
CS = plt.contour(X,Y,Z,levels=[obs],colors=color_name)
plt.minorticks_on()
plt.grid()
filename='/home/saga-t/work/python/fig/lam_eq_vs_epsiron'+'.png'
plt.savefig(filename, dpi=300)
plt.show()
