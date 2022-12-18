import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
xlim_min=-3.3
xlim_max=-0.4
plt.xlim(xlim_min,xlim_max)

pathname='/home/saga-t/work/CMIP6/amippi_grd/out/'
data_set_names=['amip','cobe','hadi','noaa','vaccaro']
window=30
i_year=131
cmap = plt.get_cmap("tab10")
for i_data in range(5):
    data_set_name=data_set_names[i_data]
    var='net30'
    name=var+'_amipPF_'+data_set_name+'_glb'
    filename=pathname+name+'.txt'
    invalues=np.loadtxt(filename)
    invalue=invalues[i_year-20]
    linewidth_value=3
    plt.axvline(x=invalue,linewidth=linewidth_value,label=data_set_name,color=cmap(i_data))
pathname='../out/ensmean/'
name=var
filename=pathname+name+'.txt'
ensmean=np.loadtxt(filename)
pathname='../out/ensstd/'
filename=pathname+name+'.txt'
ensstd=np.loadtxt(filename)
mu=ensmean[i_year]
sigma=ensstd[i_year]
N=1000
def f(x,mu,sigma):
    return np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*3.14)/sigma
p=np.linspace(xlim_min, xlim_max, N)
q=f(p,mu,sigma)
color_name='peru'
plt.plot(p,q,linewidth=linewidth_value,color=color_name)
plt.grid()
plt.minorticks_on()
plt.tight_layout()
name='PDF_MIROC6'
filename='/home/saga-t/work/python/fig/'+name+'.png'
plt.savefig(filename, dpi=300)
plt.show()
