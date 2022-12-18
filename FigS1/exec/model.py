import numpy as np
import subprocess

#CMIP6
c=8.1
c_d=110.0
gam=0.62

lam_eq=-1.03
gams=np.array([0.49,0.62,0.75])
for i in range(len(gams)):
    gam=gams[i]
    epss=np.array([1.,1.34])
    for j in range(len(epss)):
        eps=epss[j]
        dt=1.0
        n=2000

        foc=3.93*2
        def f(x,t):
            surface=(foc+lam_eq*x[0]-eps*gam*(x[0]-x[1]))/c
            deep=gam*(x[0]-x[1])/c_d
            outs=np.array([surface,deep])
            return outs

        h=1.0
        tmps=np.array([])
        tmp_ds=np.array([])
        dns=np.array([])
        dndfs=np.array([])
        x=np.zeros([2])
        for l in range(n):
            t=2*l
            k1=h*f(x,t)
            k2=h*f(x+0.5*k1,t+h)
            k3=h*f(x+0.5*k2,t+h)
            k4=h*f(x+k3,t+2*h)
            x+=(k1+2*k2+2*k3+k4)/6
            dn=foc+lam_eq*x[0]-(eps-1)*gam*(x[0]-x[1])
            dndf=dn-foc
            tmps=np.append(tmps,x[0])
            tmp_ds=np.append(tmp_ds,x[1])
            dns=np.append(dns,dn)
            dndfs=np.append(dndfs,dndf)
        lams=lam_eq-(eps-1)*gam*(1-tmp_ds/tmps)

        str_gam=str(int(gam*100)/100)
        str_eps=str(int(eps*100)/100)
        pathname='../out/gam_'+str_gam+'_eps_'+str_eps+'/'
        command='mkdir '+pathname
        subprocess.call(command,shell=True)
        name='tas'
        filename=pathname+name+'.txt'
        np.savetxt(filename,tmps,fmt ='%.3f')
        name='tod'
        filename=pathname+name+'.txt'
        np.savetxt(filename,tmp_ds,fmt ='%.3f')
        name='rtmt'
        filename=pathname+name+'.txt'
        np.savetxt(filename,dns,fmt ='%.3f')
        name='lam'
        filename=pathname+name+'.txt'
        np.savetxt(filename,lams,fmt ='%.3f')
