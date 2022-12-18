import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20

str_eps='1.0'
gams=np.array([0.49,0.62,0.75])
n_gam=len(gams)
for i_gam in range(n_gam):
    gam=gams[i_gam]
    str_gam=str(int(gam*100)/100)
    pathname='../out/gam_'+str_gam+'_eps_'+str_eps+'/'
    name='tas'
    filename=pathname+name+'.txt'
    xs=np.loadtxt(filename)
    name='rtmt'
    filename=pathname+name+'.txt'
    ys=np.loadtxt(filename)
    x=xs
    y=ys
    s_value=100
    plt.scatter(x,y,s=s_value,marker='o')
plt.grid()
plt.minorticks_on()
plt.tight_layout()
name='Gregory_abrupt-4xCO2'
filename='../../fig/FigS1a.eps'
plt.savefig(filename, dpi=300)
plt.show()
