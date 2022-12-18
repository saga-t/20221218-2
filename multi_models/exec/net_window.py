import netCDF4
import numpy as np
import subprocess

models=['CAM4','CESM2','CNRM-CM6-1','CanESM5','GFDL-AM3','GFDL-AM4','HadGEM3-GC31-LL','IPSL-CM6A-LR','MIROC6','MPI-ESM1-2-LR','MRI-ESM2-0']
nmodel=len(models)
for i_model in range(nmodel):
    model=models[i_model]
    pathname='../amip-piForcing/'+model+'/'
    name='tas'
    filename=pathname+name+'.txt'
    xs=np.loadtxt(filename)
    name='rtmt'
    filename=pathname+name+'.txt'
    ys=np.loadtxt(filename)
    window=30
    nt=len(xs)
    ni=nt-window+1
    values=np.array([])
    for i in range(ni):
        imin=i
        imax=imin+window
        x=xs[imin:imax]
        y=ys[imin:imax]
        values=np.append(values,np.polyfit(x,y,1)[0])
    name='net30'
    filename=pathname+name+'.txt'
    np.savetxt(filename,values)
