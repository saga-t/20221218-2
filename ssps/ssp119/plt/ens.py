import numpy as np

invalues = np.array([])

n_member=1000
vars=['tas','tod','rtmt','lam']
vars=['net30','net30_cor','net30_int']
#vars=['epsiron_gamma_T-T_d']
nvar=len(vars)
for i_var in range(nvar):
    var=vars[i_var]
    invalues = np.array([])
    for run in range(1,n_member+1):
        period='1850-2018'
        model='MIROC6'
        pathname='../out/run'+str(run)+'/'
        name=var
        filename=pathname+name+'.txt'
        invalue=np.loadtxt(filename)
        nt=len(invalue)
        invalues=np.append(invalues,invalue)
    reshape=np.reshape(invalues,[n_member,nt])
    values=reshape
    mean=np.mean(values,axis=0)
    std=np.std(values,axis=0)
    pathname='../out/ensmean/'
    filename=pathname+name+'.txt'
    np.savetxt(filename,mean)
    pathname='../out/ensstd/'
    filename=pathname+name+'.txt'
    np.savetxt(filename,std)
