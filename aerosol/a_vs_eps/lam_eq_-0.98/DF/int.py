import numpy as np

name='DF_aerosol'
filename=name+'.txt'
foc=np.loadtxt(filename)
df=np.array([0])
df=np.append(df,foc)
outs=np.array([])
for i in range(len(df)-1):
    outs=np.append(outs,df[i])
    outs=np.append(outs,(df[i]+df[i+1])/2)
outs=np.append(outs,df[-1])
#print(outs)
filename=name+'_int.txt'
np.savetxt(filename,outs)
