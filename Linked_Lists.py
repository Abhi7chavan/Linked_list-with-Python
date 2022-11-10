#Linked List
# 1) Add Node at the Beginning.
# 2) Add Node at the Last.
# 3) Find the length of Linked_list.
# 4) Add Node at the given Index.
# 5) Delete Node of given node.
# @abhishek Chavan

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linked_list:
    def __init__(self):
        self.head=None

    def at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def at_end(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=node
    def delete_node(self,key):
        temp=self.head
        if temp.data==key:
            self.head=temp.next
            temp=None
            return
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
            if (key==None):
                return
            prev.next=temp.next
            temp=None
    def insert_at(self, index, data):
        if index<0 :
            raise Exception("Invalid Index")
        elif str(index) > str(self.length()):
            raise Exception("Invalid Index")


        if index==0:
            self.at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
    def print(self):
        if self.head is None:
            return 
        itr=self.head
        linked_list=''
        while(itr):
            linked_list+=str(itr.data)+'-->'
            itr=itr.next
        print(linked_list,'End')

    def length(self):
        count=0
        itr=self.head
        while(itr):
            itr=itr.next
            count+=1
        return count


if __name__=='__main__':
    li=Linked_list()
    li.at_beginning(5)
    li.at_beginning(20)
    li.at_beginning(10)
    li.at_end(40)
    li.length()     
    li.insert_at(0,99)
    li.print()
            
            


        
        