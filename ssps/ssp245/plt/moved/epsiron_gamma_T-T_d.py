import numpy as np

n_member=1000
for i_member in range(1,n_member+1):
    run='run'+str(i_member)
    var='tas'
    pathname='../out/'+run+'/'
    name=var
    filename=pathname+name+'.txt'
    tass=np.loadtxt(filename)
    var='tod'
    name=var
    filename=pathname+name+'.txt'
    tods=np.loadtxt(filename)
    var='epsiron_half_year'
    name=var
    filename=pathname+name+'.txt'
    invalues=np.loadtxt(filename)
    epss=invalues[2::2]
    gamma=0.62
    outs=epss*gamma*(tass-tods)
    var='epsiron_gamma_T-T_d'
    name=var
    filename=pathname+name+'.txt'
    np.savetxt(filename,outs)
