import matplotlib.pyplot as plt 
import numpy as np 
import math as mt

class Graph(object):
    def __init__(self):
        self.freq={}

    def getfrequency(self,distance,r):
        p=1
        d=np.array(distance,dtype=np.int)
        for i in range(r,d.max()+r,r):
            self.freq[i]=d[(p <= d) & (d <= i)].size
            p=i+1
        return self.freq

    def plothistogram(self,x,y,r):
        #plt.axis([0, 100, 0, 20])
        pos=[i for i in x]
        label=[]
        prev=0
        for i in x:
            label.append(str(prev)+"-"+str(i))
            prev=i

        plt.grid(True)
        plt.bar(x,y,width=r,alpha=0.7,facecolor='red')
        plt.xticks(pos, label,rotation=90)
        plt.xlabel('Distances')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()
