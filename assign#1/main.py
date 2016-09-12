from datastructures import linkedlist,inout

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

	if M[1]==maxima[1] and M[0]==maxima[0]:
		ll_max.insert(M[0],M[1])
		maxima=M
	elif M[1]==minima[1] and M[0]==minima[0]:
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

ll_max.display()