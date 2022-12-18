import numpy as np
import matplotlib.pyplot as plt

#plt.figure(figsize=(10,5))
plt.rcParams["font.size"]=20
xlim_min=-1
xlim_max=4.5
#plt.xlim(xlim_min,xlim_max)
ylim_min=0.06
ylim_max=0.35
#plt.ylim(ylim_min,ylim_max)

left=np.array([0,1,2,3,4,5,6,7])
std=np.array([0.0223,0.0234,0.0373,0.0186,0.0368,0.0140,0.0147])
mean=np.array([0.2935,0.1962,0.1596,0.1654,0.1970,0.1314,0.1577])
height=std*2
value_bottom=mean-std
width_value=0.8
ymin_values=mean-std
ymax_values=mean+std
cmap_name='tab20'
cm=plt.cm.get_cmap(cmap_name)
color_names=cm.colors
n_model=len(std)
indexs=np.array([3,1,2,11,7,8,9]) 
for i_model in range(n_model):
    left=i_model
    ymin_value=ymin_values[i_model]
    ymax_value=ymax_values[i_model]
    linewidth_value=3
    index=indexs[i_model]
    color_name=color_names[index]
    plt.vlines(x=left,ymin=ymin_value,ymax=ymax_value,color=color_name,linewidth=linewidth_value)
    value_bottom=mean[i_model]
    plt.bar(left,0,bottom=value_bottom,color='None',edgecolor=color_name,width=0.2,linewidth=linewidth_value)
plt.xticks([])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.minorticks_on()
plt.tight_layout()
filename='../../fig/FigS8b.eps'
plt.savefig(filename, dpi=300)
plt.show()
