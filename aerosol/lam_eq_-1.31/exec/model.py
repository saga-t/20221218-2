import numpy as np
import subprocess

#CMIP6
c=8.1
c_d=110.0
gam=0.62
lam_eq=-1.31

filename='../DF/DF_int.txt'
df=np.loadtxt(filename)
filename='../DF/DF_aerosol_int.txt'
df_aerosol=np.loadtxt(filename)
n=len(df)//2

foc=df
def f(x,t):
    surface=(foc[t]+lam_eq*x[0]-eps*gam*(x[0]-x[1]))/c
    deep=gam*(x[0]-x[1])/c_d
    outs=np.array([surface,deep])
    return outs
h=1

factors=np.arange(-2.,2.01,0.2)
factors=np.array([-0.331,0,0.331])
for i in range(len(factors)):
    factor=factors[i]
    foc=df+factor*df_aerosol
    epss=np.arange(0.1,4.05,0.05)
    epss=np.array([1.34])
    for j in range(len(epss)):
        eps=epss[j]
        tmps=np.array([])
        tmp_ds=np.array([])
        dns=np.array([])
        x=np.zeros([2])
        for l in range(n):
            t=2*l
            k1=h*f(x,t)
            k2=h*f(x+0.5*k1,t+h)
            k3=h*f(x+0.5*k2,t+h)
            k4=h*f(x+k3,t+2*h)
            x+=(k1+2*k2+2*k3+k4)/6
            dn=foc[t+2*h]+lam_eq*x[0]-(eps-1)*gam*(x[0]-x[1])
            tmps=np.append(tmps,x[0])
            tmp_ds=np.append(tmp_ds,x[1])
            dns=np.append(dns,dn)
        lams=lam_eq-(eps-1)*gam*(1-tmp_ds/tmps)
        str_factor=str(int(factor*100)/100)
        str_eps=str(int(eps*100)/100)
        pathname='../out/factor_'+str_factor+'_eps_'+str_eps+'/'
        command='mkdir '+pathname
        subprocess.call(command,shell=True)
        name='tas'
        filename=pathname+name+'.txt'
        np.savetxt(filename,tmps)
        name='tod'
        filename=pathname+name+'.txt'
        np.savetxt(filename,tmp_ds)
        name='rtmt'
        filename=pathname+name+'.txt'
        np.savetxt(filename,dns)
        name='lam'
        filename=pathname+name+'.txt'
        np.savetxt(filename,lams)
            
