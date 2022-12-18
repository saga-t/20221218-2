import numpy as np

nt=251
window=30
models=['CESM2','CNRM-CM6-1','CanESM5','HadGEM3-GC31-LL','IPSL-CM6A-LR','MIROC6','MPI-ESM1-2-LR','MRI-ESM2-0']
n_model=len(models)
for i_model in range(n_model):
    model=models[i_model]
    run=model
    var='tas'
    pathname='../out/'+run+'/'
    name=var
    filename=pathname+name+'.txt'
    dts=np.loadtxt(filename)
    var='rtmt'
    name=var
    filename=pathname+name+'.txt'
    dns=np.loadtxt(filename)
    filename='../DF/DF.txt'
    dfs=np.loadtxt(filename)
    values=np.array([])
    ni=nt-window+1
    nvar=3
    for i in range(ni):
        imin=i
        imax=imin+window
        dt=dts[imin:imax]
        dn=dns[imin:imax]
        df=dfs[imin:imax]
        x=dt
        y=dn-df
        values=np.append(values,np.polyfit(x,y,1))
        values=np.append(values,np.corrcoef(x,y)[0,1])
    reshapes=np.reshape(values,[ni,nvar])
    vars=['','_int','_cor']
    for i_var in range(nvar):
        name='net'+str(window)+vars[i_var]
        filename=pathname+name+'.txt'
        out=reshapes[:,i_var]
        np.savetxt(filename,out)
