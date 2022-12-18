import numpy as np

outvalues = np.array([])

n_member=1000
vars=['tas','tod','rtmt','lam']
#vars=['net30','net30_cor','net30_int']
#vars=['epsiron_gamma_T-T_d']
vars=['tas']
nvar=len(vars)
for i_var in range(nvar):
    var=vars[i_var]
    invalues = np.array([])
    dd=0.05
    factors=np.arange(-1.0,1.01,0.2)
    for i in range(len(factors)):
        facotor=factors[i]
        epss=np.arange(0.1,4.05,dd)
        for j in range(len(epss)):
            eps=epss[j]
            it=100
            str_factor=str(int(facotor*it)/it)
            str_eps=str(int(eps*it)/it)
            pathname='../out/factor_'+str_factor+'_eps_'+str_eps+'/'
            name=var
            filename=pathname+name+'.txt'
            invalue=np.loadtxt(filename)
            x=np.arange(0,54,1)
            imin=1961-1850
            imax=2014-1850+1
            y=invalue[imin:imax]
            slope=np.polyfit(x,y,1)[0]
            name=var+'_trend_1961-2014'
            filename=pathname+name+'.txt'
            trend=slope.reshape([1,])
            np.savetxt(filename,trend)
            outvalues=np.append(outvalues,slope)
    pathname='../out/all/'
    filename=pathname+name+'.txt'
    np.savetxt(filename,outvalues)
