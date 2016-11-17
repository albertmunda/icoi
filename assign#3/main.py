# -*- coding: utf-8 -*-

# Author: Albert Mundu
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import numpy as np
from scipy.spatial.distance import pdist

sample_number=raw_input("Enter sample number: ")
max_clusters = input('Cut-off distance: ')

X=np.loadtxt("samples/sample0"+sample_number+".rtf",dtype=np.int)


Y=pdist(X,'euclidean') #condensed distance matrix
#Y=pdist(X,'cityblock')

Z=linkage(Y,'average') #single,complete,centroid

# for i,j,d,n in Z:
#     print "{%d - %d} merge_distance=%d clusters_merged=%d" %(i,j,d,n)

# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Agglomerative Clustering Dendrogram')
plt.xlabel('index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

cutoff=max_clusters
#clusters = fcluster(Z, max_clusters, criterion='maxclust')
clusters = fcluster(Z, cutoff, criterion='distance')
plt.figure(figsize=(10, 8))
plt.scatter(X[:,0], X[:,1], c=clusters, cmap='prism')  # plot points with cluster dependent colors
plt.show()
