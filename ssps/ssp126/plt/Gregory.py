import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 18
invalues = np.array([])

window=30
imin=131
imax=imin+window

n_member=3
for run in range(1,n_member+1):
    pathname='../out/run'+str(run)+'/'
    name='tmp'
    filename=pathname+name+'.txt'
    invalue=np.loadtxt(filename)
    x=invalue[imin:imax]
    name='dn'
    filename=pathname+name+'.txt'
    dn=np.loadtxt(filename)
    name='df'
    filename=pathname+name+'.txt'
    df=np.loadtxt(filename)
    pathname='../DF/'
    name='DF'
    filename=pathname+name+'.txt'
    df_without_noise=np.loadtxt(filename)
    dndf=dn-df
    y=dndf[imin:imax]
    color_name='blue'
    s_value=100
    plt.scatter(x,y,color=color_name,facecolor='none',s=s_value,marker='o')
    x_fit=np.array([np.min(x),np.max(x)])
    y_fit=np.polyfit(x, y, 1)[0]*x_fit+np.polyfit(x, y, 1)[1]
    linewidth_value=3
    plt.plot(x_fit,y_fit,color=color_name,linewidth=linewidth_value)
    print(np.polyfit(x, y, 1))
    print(np.corrcoef(x,y)[0,1])
    
    dndf_without_noise=dn-df_without_noise[0:-1]
    y=dndf_without_noise[imin:imax]
    color_name='red'
    plt.scatter(x,y,color=color_name,facecolor='none',s=s_value,marker='o')
    y_fit=np.polyfit(x, y, 1)[0]*x_fit+np.polyfit(x, y, 1)[1]
    plt.plot(x_fit,y_fit,color=color_name,linewidth=linewidth_value)
    print(np.corrcoef(x,y)[0,1])
    plt.grid()
    plt.minorticks_on()
    plt.tight_layout()
    extension='.png'
    name='Gregory_run'+str(run)
    filename='/home/saga-t/work/python/fig/'+name+extension
    plt.savefig(filename, dpi=300)
    plt.show()
