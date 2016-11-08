# -*- coding: utf-8 -*-

# Author: Albert Mundu
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
import numpy as np
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import fcluster

X=np.loadtxt("samples/sample01.rtf",dtype=np.int)

#a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
#b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])

#M=np.concatenate((a,b),)
#print values.shape
#plt.scatter(values[:,0],values[:,1])
#plt.show()
#result=values/np.linalg.norm(values,axis=-1)[:,np.newaxis]
Z=linkage(X,'single')
#Z=linkage(X,'ward')
#Y = pdist(values[100], 'euclidean')

#print pdist(values)
#c, coph_dists=cophenet(Z,pdist(X))

##############################
'''
idxs = [33, 68, 62]
plt.figure(figsize=(10, 8))
plt.scatter(X[:,0], X[:,1])
plt.scatter(X[idxs,0], X[idxs,1], c='r')
idxs = [15, 69, 41]
plt.scatter(X[idxs,0], X[idxs,1], c='y')
plt.show()
'''
####################################
# calculate full dendrogram
'''plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()
'''
max_d = 5
clusters = fcluster(Z, max_d, criterion='distance')
print clusters
plt.figure(figsize=(10, 8))
plt.scatter(X[:,0], X[:,1], c=clusters, cmap='prism')  # plot points with cluster dependent colors
plt.show()

