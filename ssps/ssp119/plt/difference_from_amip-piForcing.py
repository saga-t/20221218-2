import numpy as np
import subprocess

models=['CESM2','CNRM-CM6-1','CanESM5','HadGEM3-GC31-LL','IPSL-CM6A-LR','MIROC6','MPI-ESM1-2-LR','MRI-ESM2-0']
n_model=len(models)
i_starts=np.array([0,0,0,0,0,0,1,0])
for i_model in range(n_model):
    pathname='/home/saga-t/work/CMIP6/timothyandrews/out/'
    model=models[i_model]
    var='net30'
    name='amip-piForcing_'+model+'_'+var
    filename=pathname+name+'.txt'
    amipPF=np.loadtxt(filename)
    i_start=i_starts[i_model]
    nlen=len(amipPF)
    pathname='../out/'+model+'/'
    name=var
    filename=pathname+name+'.txt'
    two_layer=np.loadtxt(filename)
    imin=20+i_start
    imax=imin+nlen
    difference=two_layer[imin:imax]-amipPF
    print(difference)
    pathname='../out/'+model+'/difference_from_amip-piForcing/'
    command='mkdir '+pathname
    subprocess.call(command,shell=True)
    filename=pathname+name+'.txt'
    np.savetxt(filename,difference)
