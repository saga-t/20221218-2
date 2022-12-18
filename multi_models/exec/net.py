import netCDF4
import numpy as np
import subprocess

models=['CAM4','CESM2','CNRM-CM6-1','CanESM5','GFDL-AM3','GFDL-AM4','HadGEM3-GC31-LL','IPSL-CM6A-LR','MIROC6','MPI-ESM1-2-LR','MRI-ESM2-0']
nmodel=len(models)
for i_model in range(nmodel):
    model=models[i_model]
    pathname='../abrupt-4xCO2/'+model+'/'
    name='tas'
    filename=pathname+name+'.txt'
    xs=np.loadtxt(filename)
    name='rtmt'
    filename=pathname+name+'.txt'
    ys=np.loadtxt(filename)
    out=np.polyfit(xs,ys,1)[0]
    print(out)
    out=np.reshape(out,[1,])
    name='net'
    filename=pathname+name+'.txt'
    np.savetxt(filename,out)
