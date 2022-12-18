import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.rcParams["font.size"]=20
xlim_min=-0.5
xlim_max=4.5
#plt.xlim(xlim_min,xlim_max)
ylim_min=0.12
ylim_max=0.225
plt.ylim(ylim_min,ylim_max)

left_orig=np.array([0,1,2,3])
left=left_orig*2
std=np.array([0.0093,0.0104,0.0255,0.0195])
mean=np.array([0.1615,0.2107,0.1858,0.1983])
height=std*2
value_bottom=mean-std
width_value=0.8
plt.bar(left,height,bottom=value_bottom,color='blue',width=width_value)
value_bottom=mean
plt.bar(left,0,bottom=value_bottom,color='None',edgecolor='white',width=width_value,linewidth=3)
plt.xticks([])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.minorticks_on()
plt.tight_layout()
filename='../../fig/FigS8a.eps'
plt.savefig(filename, dpi=300)
plt.show()
