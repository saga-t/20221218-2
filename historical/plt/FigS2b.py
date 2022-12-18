import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20

xlim_min=1850
xlim_max=2019
plt.xlim(xlim_min, xlim_max)


x=np.arange(1850,2100.1,1)
plt.axhline(y=0,color="black",linewidth=1.0)

pathname='../AR5/out/lam_eq_-1.31_eps_1.34/'
name='tas'
filename=pathname+name+'.txt'
values=np.loadtxt(filename)
y=values
color_name='blue'
label_name='AR5'
linewidth_value=3
plt.plot(x[0:162],y,color=color_name,label=label_name,linewidth=linewidth_value)

pathname='../AR6/out/lam_eq_-1.31_eps_1.34/'
filename=pathname+name+'.txt'
values=np.loadtxt(filename)
y=values
color_name='darkorange'
label_name='AR6'
plt.plot(x[0:170],y,color=color_name,label=label_name,linewidth=linewidth_value)

pathname='../AR5_and_AR6/out/lam_eq_-1.31_eps_1.34/'
filename=pathname+name+'.txt'
values=np.loadtxt(filename)
y=values
color_name='red'
label_name='AR5 and AR6'
plt.plot(x[0:170],y,color=color_name,label=label_name,linewidth=linewidth_value)

pathname=''
name='HadCRUT5'
filename=pathname+name+'.txt'
obs=np.loadtxt(filename)
y=obs
color_name='black'
plt.plot(x[0:172],y,color=color_name,linewidth=linewidth_value)

plt.legend()
plt.minorticks_on()
plt.tight_layout()
filename='../../fig/FigS2b.eps'
plt.savefig(filename, dpi=300)
plt.show()
