import numpy as np
import matplotlib.pyplot as plt
import netCDF4

plt.rcParams["font.size"] = 18

xlim_min=1850
xlim_max=2018
#plt.xlim(xlim_min,xlim_max)

ylim_min=-3
ylim_max=3
#plt.ylim(ylim_min,ylim_max)
linewidth_value=3
#plt.axhline(y=-1.44,color='g',linewidth=linewidth_value,linestyle='dashed')

pathname='../out/ensmean/'
var='net30'
name=var
filename=pathname+name+'.txt'
ensmean=np.loadtxt(filename)
pathname='../out/ensstd/'
filename=pathname+name+'.txt'
ensstd=np.loadtxt(filename)
pathname='../out/forced/'
filename=pathname+name+'.txt'
forced=np.loadtxt(filename)
#x=np.linspace(1865,2004,140)
x_min=1850
x_max=2100
x_min=1865
x_max=2086
nx=x_max-x_min+1
x=np.linspace(x_min,x_max,nx)
y=ensmean
color_name='peru'
linewidth_value=3
plt.plot(x,y,color=color_name,linewidth=linewidth_value)
alpha_value=0.2
plt.fill_between(x,y-ensstd,y+ensstd,color=color_name,alpha=alpha_value)
y=forced
color_name='brown'
plt.plot(x,y,color=color_name,linewidth=linewidth_value)


pathname='/mnt/clm34/saga-t/CMIP6/histall/saga-t/MIROC6/ensmean/delta/yearmonmean/fldmean/'
var='net30'
name=var+'_Amon_MIROC6_histall_ensmean_gn_185001-210012'
filename=pathname+name+'.nc'
ncin=netCDF4.Dataset(filename,'r',format='NETCDF4')
vin=ncin.variables[var]
values=np.array(vin)
ensmean=values.T[0][0]
ncin.close()
pathname='/mnt/clm34/saga-t/CMIP6/histall/saga-t/MIROC6/ensstd/delta/yearmonmean/fldmean/'
name=var+'_Amon_MIROC6_histall_ensstd_gn_185001-210012'
filename=pathname+name+'.nc'
ncin=netCDF4.Dataset(filename,'r',format='NETCDF4')
vin=ncin.variables[var]
values=np.array(vin)
ensstd=values.T[0][0]
ncin.close()
pathname='/mnt/clm34/saga-t/CMIP6/histall/saga-t/MIROC6/forced/delta/yearmonmean/fldmean/'
name=var+'_Amon_MIROC6_histall_forced_gn_185001-210012'
filename=pathname+name+'.nc'
ncin=netCDF4.Dataset(filename,'r',format='NETCDF4')
vin=ncin.variables[var]
values=np.array(vin)
forced=values.T[0][0]
ncin.close()
pathname='/mnt/clm34/saga-t/CMIP6/amip-piForcing/saga-t/MIROC6/r1i1p1f1/delta/yearmonmean/fldmean/'
name=var+'_Amon_MIROC6_amip-piForcing_r1i1p1f1_gn_187001-201412'
filename=pathname+name+'.nc'
ncin=netCDF4.Dataset(filename,'r',format='NETCDF4')
vin=ncin.variables[var]
values=np.array(vin)
amipPF=values.T[0][0]
ncin.close()
y=ensmean
color_name='purple'
plt.plot(x,y,color=color_name,linewidth=linewidth_value)
plt.fill_between(x,y-ensstd,y+ensstd,color=color_name,alpha=alpha_value)
y=forced
color_name='red'
plt.plot(x,y,color=color_name,linewidth=linewidth_value)
y=amipPF
color_name='darkorange'
plt.plot(x[20:136],y,color=color_name,linewidth=linewidth_value)
print(x[20:136])
plt.grid()
plt.minorticks_on()
plt.tight_layout()
extension='.png'
filename='/home/saga-t/work/python/fig/'+name+extension
plt.savefig(filename, dpi=300)
plt.show()
