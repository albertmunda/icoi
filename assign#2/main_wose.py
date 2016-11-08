from datastructures import linkedlist,inout,graph
window_size=input("Enter the window size: ")
filename=raw_input("Enter the sample file name: ")

ll_obj=linkedlist.LinkedList() 				#for storing data read from a file
io_obj=inout.ReadData("samples/"+filename)	#reading file

ll_max=linkedlist.LinkedList() 				#for storing local maximas
ll_min=linkedlist.LinkedList()				#for storing local minimas

slide_value=1

for i in range(window_size):
	x,y,z=io_obj.getxy()
	ll_obj.insert(x,y)

loop_exit=False

maxima=ll_obj.getmaxima()
minima=ll_obj.getminima()

while loop_exit == False:
	M=ll_obj.getmid(window_size)

	if M[1]==maxima[1]:# and M[0]==maxima[0]:
		ll_max.insert(M[0],M[1])
		maxima=M
	elif M[1]==minima[1]:# and M[0]==minima[0]:
		ll_min.insert(M[0],M[1])
		minima=M

	for i in range(slide_value):
		ll_obj.delete()

	for i in range(slide_value):
		x,y,z=io_obj.getxy()
		if x!=None:
			new_item=x,y
			ll_obj.insert(x,y)
		else:
			loop_exit=True
			break

	if ll_obj.exists(maxima)==False:
		maxima=ll_obj.getmaxima()
		if minima[1] >= new_item[1]:
			minima=new_item
	elif ll_obj.exists(minima)==False:
		minima=ll_obj.getminima()
		if maxima[1] <= new_item[1]:
			maxima=new_item
	else:
		if maxima[1] <= new_item[1]:
			maxima=new_item
		elif minima[1] >= new_item[1]:
			minima=new_item

ll_max.write_list_io("max")
ll_min.write_list_io("min")

'''ll_max.sline_elimination()
ll_max.display()

with open("max","r") as f:
	values=f.readline().split()
	px=int(values[0])
	py=int(values[1])

	for i in f:
		values=i.split()
		x=int(values[0])
		y=int(values[1])

		if (x-px)==1 and y==py:
			pass
		elif (x-px)==1 and y!=py:
			print x,y
			px=

'''
##################MAXIMA###########################
r=input('Enter the range: ')
maxd=ll_max.successive_distance()
maxd.sort()
#print maxd
g=graph.Graph()
freq=g.getfrequency(maxd,r)
maxhisto=[]
maxkeys=[]
with open("maxhisto.data","w") as f:
	
	for i in sorted(freq):
		f.write(str(i)+" "+str(freq[i])+"\n")
		maxhisto.append(freq[i])
		maxkeys.append(i)

g.plothistogram(maxkeys,maxhisto,r)
###################################################

#print maxhisto
#print sum(maxhisto)

##################MAXIMA###########################
'''r=input('Enter the range: ')
mind=ll_min.successive_distance()
mind.sort()
#print mind
g=graph.Graph()
freq=g.getfrequency(mind,r)
minhisto=[]
minkeys=[]
with open("minhisto.data","w") as f:
	
	for i in sorted(freq):
		f.write(str(i)+" "+str(freq[i])+"\n")
		minhisto.append(freq[i])
		minkeys.append(i)

g.plothistogram(minkeys,minhisto,r)
###################################################'''