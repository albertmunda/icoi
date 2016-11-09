# -*- coding: utf-8 -*-

# Author: Albert Mundu
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
import numpy as np
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import fcluster

sample_number=raw_input("Enter sample number: ")
max_clusters = input('Number of clusters to create: ')

X=np.loadtxt("samples/sample0"+sample_number+".rtf",dtype=np.int)


Y=pdist(X,'euclidean')

Z=linkage(Y,'centroid')

for i,j,d,n in Z:
    print "{%d - %d} merge_distance=%d clusters_merged=%d" %(i,j,d,n)
#Z=linkage(X,'centroid')
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
plt.title('Agglomerative Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()
'''

clusters = fcluster(Z, max_clusters, criterion='maxclust')
plt.figure(figsize=(10, 8))
plt.scatter(X[:,0], X[:,1], c=clusters, cmap='prism')  # plot points with cluster dependent colors
plt.show()
