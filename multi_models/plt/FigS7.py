import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 18

xlim_min=1885
xlim_max=2003
plt.xlim(xlim_min,xlim_max)

models=['CAM4','CESM2','CNRM-CM6-1','CanESM5','GFDL-AM3','GFDL-AM4','HadGEM3-GC31-LL','IPSL-CM6A-LR','MIROC6','MPI-ESM1-2-LR','MRI-ESM2-0']
i_starts=np.array([0,0,0,0,0,0,0,0,0,1,0])
net_abrupt4xCO2_1_150s=np.array([-1.233,-0.657,-0.75,-0.648,-0.744,-0.864,-0.63,-0.748,-1.443,-1.393,-1.098])
nmodel=len(models)
cmap_name='tab20'
cm=plt.cm.get_cmap(cmap_name)
color_names=cm.colors

for i_model in range(nmodel):
    model=models[i_model]
    pathname='../amip-piForcing/'+model+'/'
    name='net30'
    filename=pathname+name+'.txt'
    invalues=np.loadtxt(filename)
    i_start=i_starts[i_model]
    xmin=1885+i_start
    xmax=xmin+len(invalues)
    x=np.arange(xmin,xmax,1)
    y=invalues
    color_name=color_names[i_model]
    linewidth_value=3
    plt.plot(x,y,color=color_name,linewidth=linewidth_value,label=model)
    #plt.plot(x,y,label=model)
    net_abrupt4xCO2_1_150=net_abrupt4xCO2_1_150s[i_model]
    plt.axhline(y=net_abrupt4xCO2_1_150,color=color_name,linestyle='dashed')
#plt.legend(bbox_to_anchor=(1.05, 1))
#plt.grid()
plt.minorticks_on()
plt.tight_layout()
extension='.eps'
name='FigS7'
#name='legend'
filename='../../fig/'+name+extension
plt.savefig(filename, dpi=300)
plt.show()
