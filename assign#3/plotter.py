import matplotlib.pyplot as plt
import numpy as np
import subprocess as sp
out=sp.check_output(['ls','-1','cluster'],shell=False);
num=len(out.split())
theta = 2 * np.pi * np.random.rand(num)

for i in range(num):
    X=np.loadtxt("cluster/cluster_"+str(i),dtype=np.int)
    plt.plot(X[:,0],X[:,1],'o')
plt.show()
