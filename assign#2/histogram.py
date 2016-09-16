import matplotlib.pyplot as plt 
import sys

ran=input('Enter the bin size: ')
f=open(sys.argv[1],"r")
x=f.readlines()
freq=[]
distances=[]
pos=[]
label=[]
prev=0
for i in range(len(x)):
    value=x[i].split()
    distances.append(value[0])
    freq.append(value[1])
    pos.append((i+1)*ran)
    label.append(str(prev*ran)+"-"+str(i*ran))
    prev=i

print freq
print distances

plt.bar(distances,freq,width=ran,alpha=0.4,facecolor='red')
plt.xticks(pos, label,rotation=90)
plt.grid(True)
plt.xlabel('Distances')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()