import numpy as np
import subprocess

#CMIP6
c=8.1
c_d=110.0
gam=0.62

filename='../DF/DF_int.txt'
df=np.loadtxt(filename)
n=len(df)//2

foc=df
def f(x,t):
    surface=(foc[t]+lam_eq*x[0]-eps*gam*(x[0]-x[1]))/c
    deep=gam*(x[0]-x[1])/c_d
    outs=np.array([surface,deep])
    return outs
h=1

lam_eqs=np.array([-1.57,-1.31,-0.98,-1.51])
for i in range(len(lam_eqs)):
    lam_eq=lam_eqs[i]
    epss=np.array([0.93,1.34,1.75,1.,2.,1.31,1.72])
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
        str_lam_eq=str(int(lam_eq*100)/100)
        str_eps=str(int(eps*100)/100)
        pathname='../out/lam_eq_'+str_lam_eq+'_eps_'+str_eps+'/'
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
            
