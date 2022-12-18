import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.rcParams["font.size"]=20
xlim_min=-0.5
xlim_max=4.6
plt.xlim(xlim_min,xlim_max)
ylim_min=0
ylim_max=7
plt.ylim(ylim_min,ylim_max)

pathname=''
name='tass_2100_FigS10'
filename=pathname+name+'.txt'
invalues=np.loadtxt(filename)
print(invalues)

ssps=['ssp119','ssp126','ssp245','ssp370','ssp585']
n_ssp=len(ssps)
color_names=['skyblue','blue','orange','red','darkred']
for i_ssp in range(n_ssp):
    experiment=ssps[i_ssp]
    distance=0.15
    left=i_ssp-distance
    value_bottom=invalues[2,i_ssp]
    height=invalues[0,i_ssp]-invalues[2,i_ssp]
    color_name=color_names[i_ssp]
    width_value=0.2
    alpha_value=0.5
    plt.bar(left,height,bottom=value_bottom,color=color_name,width=width_value,alpha=alpha_value)
    value_bottom=invalues[1,i_ssp]
    plt.bar(left,0,bottom=value_bottom,color='None',edgecolor='black',width=width_value)
    left=i_ssp+distance
    value_bottom=invalues[5,i_ssp]
    height=invalues[3,i_ssp]-invalues[5,i_ssp]
    plt.bar(left,height,bottom=value_bottom,color=color_name,width=width_value)
    value_bottom=invalues[4,i_ssp]
    plt.bar(left,0,bottom=value_bottom,color='None',edgecolor='black',width=width_value)

pathname=''
name='tass_2100_obs_and_aerosol_FigS10'
filename=pathname+name+'.txt'
invalues=np.loadtxt(filename)
print(invalues)
for i_ssp in range(n_ssp):
    experiment=ssps[i_ssp]
    distance=0.35
    value_bottom=invalues[2,i_ssp]
    ymax_value=invalues[0,i_ssp]
    ymin_value=invalues[2,i_ssp]
    color_name='green'
    width_value=0.08
    alpha_value=0.5
    left=i_ssp+distance
    plt.vlines(x=left,ymin=ymin_value,ymax=ymax_value,color=color_name)
    value_bottom=invalues[1,i_ssp]
    plt.bar(left,0,bottom=value_bottom,color='None',edgecolor=color_name,width=width_value)

name='tass_2100_obs_and_variability_FigS10'
filename=pathname+name+'.txt'
invalues=np.loadtxt(filename)
print(invalues)
for i_ssp in range(n_ssp):
    experiment=ssps[i_ssp]
    distance=0.5
    value_bottom=invalues[2,i_ssp]
    ymax_value=invalues[0,i_ssp]
    ymin_value=invalues[2,i_ssp]
    color_name='blue'
    width_value=0.08
    alpha_value=0.5
    left=i_ssp+distance
    plt.vlines(x=left,ymin=ymin_value,ymax=ymax_value,color=color_name)
    value_bottom=invalues[1,i_ssp]
    plt.bar(left,0,bottom=value_bottom,color='None',edgecolor=color_name,width=width_value)

x=np.array([xlim_min,xlim_max])
y1=np.array([2.5,2.5])
y2=np.array([4,4])
#plt.fill_between(x,y1,y2,color='black',alpha=0.2)
plt.xticks([])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.minorticks_on()
plt.tight_layout()
filename='../../fig/FigS10.eps'
plt.savefig(filename, dpi=300)
plt.show()
