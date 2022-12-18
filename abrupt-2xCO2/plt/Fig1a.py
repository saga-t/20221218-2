import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20

lam_eq=-1.03
epss=np.array([0.93,1.34,1.75])
n_eps=len(epss)
for i_eps in range(n_eps):
    eps=epss[i_eps]
    pathname='../out/lam_eq_'+str(lam_eq)+'_eps_'+str(eps)+'/'
    name='tas'
    filename=pathname+name+'.txt'
    xs=np.loadtxt(filename)
    pathname='../out/lam_eq_'+str(lam_eq)+'_eps_'+str(eps)+'/'
    name='rtmt'
    filename=pathname+name+'.txt'
    ys=np.loadtxt(filename)
    x=xs
    y=ys
    s_value=100
    plt.scatter(x,y,s=s_value,marker='o')
#plt.grid()
plt.minorticks_on()
plt.tight_layout()
name='Gregory_abrupt-4xCO2'
filename='../../fig/Fig1a.eps'
plt.savefig(filename, dpi=300)
plt.show()
