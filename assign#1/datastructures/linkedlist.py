class Node(object):
    def __init__(self,x=None,y=None,next_node=None):
        self.x=x
        self.y=y
        self.next_node=next_node

class LinkedList(object):
    def __init__(self,head=None,prev=None):
        self.head=head
        self.prev=None

    def insert(self,x,y):
        if(self.head==None):
            new_node=Node(x,y)
            new_node.next_node=None
            self.head=new_node
            self.prev=new_node
        else:
            new_node=Node(x,y)
            new_node.next_node=None
            self.prev.next_node=new_node
            self.prev=new_node

    def delete(self):
        self.head=self.head.next_node

    def getmaxima(self):
        tmp=self.head
        max=(0,0)
        while tmp!=None:
            if max[1]<tmp.y:
                max=tmp.x,tmp.y
            tmp=tmp.next_node
        return max  

    def getminima(self):
        tmp=self.head
        min=(0,9999999)
        while tmp!=None:
            if min[1]>tmp.y:
                min=tmp.x,tmp.y
            tmp=tmp.next_node
        return min    

    def getmid(self,window_size):
        tmp=self.head
        for i in range(window_size/2):
            tmp=tmp.next_node
        return tmp.x,tmp.y

    def display(self):
        tmp=self.head
        while tmp!=None:
            print tmp.x,tmp.y
            tmp=tmp.next_node
        print ""
        
    def exists(self,value):
        tmp=self.head
        if value[0]<tmp.x:
            return False
        else:
            return True

    def last_item(self):
        tmp=self.head
        while tmp.next_node!=None:
            tmp=tmp.next_node
        return tmp.x,tmp.y        