#Class for creating Node with data and pointing to Null
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

#Class for performing LinkedList operations
class CircularDoubleLinkedList:
    #Initialisation of head pointer,tail pointer and size for further reference
    def __init__(self,value):
        self.head=None
        self.tail=None
        self.size=0
        self.insertElement(value)
    
    #Method for inserting Element at the end of LinkedList
    def insertElement(self,value):
        if(self.head==None):
            node=Node(value)
            node.next=node
            node.prev=node
            self.head=node
            self.tail=node
            self.size+=1
            return

        temp=self.head
        while(temp):
            if(temp.next==self.tail):
                node=Node(value)
                node.next=self.head
                node.prev=self.tail
                self.tail.next=node
                self.tail=node
                self.size+=1
                return
            temp=temp.next
    
    #Method for inserting Element at the particular location of LinkedList
    def insertElementLocation(self,value,location):
        
        #Checking weather LinkedList exists
        if(self.head==None):
            print("Current length of Linked List is zero inserting as starting node")
            self.insertElement(value)
            return

        #Checking weather user given location should not be greater than Size+1
        if(location>self.size):
            print("Please enter correct location currently we have "+str(self.size)+" elements")
            return

        temp=self.head

        #Inserting Node at the start of LinkedList
        if(location-1==0):
            node=Node(value)
            node.next=self.head
            node.prev=self.tail
            self.head.prev=node
            self.head=node
            self.tail.next=node
            self.size+=1
            print("\nInsertion at location "+str(location)+" successful")
            return

        #Inserting Node at the end of LinkedList
        if(location==self.size):
            node=Node(value)
            node.next=self.head
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
            self.size+=1
            print("\nInsertion at location "+str(location)+" successful")
            return

        #Inserting value at any location other than Start and End
        index=0
        while(temp):
            if(index==location-1):
                node=Node(value)
                node.next,temp.next,node.prev=temp.next,node,temp
                node.next.prev=node
                self.size+=1
                print("\nInsertion at location "+str(location)+" successful")
                return
            index+=1
            temp=temp.next

#Method for traversing LinkedList
    def traverse(self):
        temp=self.head
        #Checking weather LinkedList exists
        if(temp==None):
            print("Single Linked List is empty")
            return
        print("Printing Single LinkedList ")
        while(temp):
            print(temp.data,end="")
            if(temp==self.tail):
                return
            print("=>",end="")
            if(temp==self.tail):
                return
            temp=temp.next

    #Method for searching a node
    def searchNode(self,value):
        #Checking weather LinkedList exists
        if(self.head==None):
            print("LinkedList is empty")
            return
        
        temp=self.head
        index=0
        found=False
        while(temp):
            if(temp.data==value):
                print("Found the node with value: "+str(value)+" at location: "+str(index+1))
                found=True
            if(temp==self.tail):
                if(found==False):
                    print("No Node with value "+str(value)+" found.")
                return
            temp=temp.next
            index+=1

    #Method for Deleting Node from LinkedList
    def deleteElement(self,location):

        #Checking weather LinkedList exists
        if(self.head==None):
            print("Current length of Linked List is 0. No Node to delete")
            return

        #Checking weather user given location should not be greater than Size
        if(location>self.size):
            print("Please enter correct location currently we have "+str(self.size)+" elements")
            return

        temp=self.head

        #Deleting Node at the start of LinkedList
        if(location-1==0):
            self.head=temp.next
            temp.prev=None
            self.tail.next=self.head
            temp.next.prev=None
            self.size-=1
            if(self.size==0):
                self.head=None
                self.tail=None
            print("\nDeletion at location "+str(location)+" successful")
            return

        if(location==self.size):
            temp=self.head
            while(temp):
                if(temp.next==self.tail):
                    temp.next=None
                    self.tail.prev=None
                    self.tail=temp
                    self.size-=1
                    self.tail.next=self.head
                    self.head.prev=self.tail
                    if(self.size==0):
                        self.head=None
                        self.tail=None
                    print("\nDeletion at location "+str(location)+" successful")
                    return
                temp=temp.next

        #Deleting Node at any other location of LinkedList
        index=0
        while(temp):
            if(index+1==location-1):
                temp.next,temp.next.prev=temp.next.next,temp
                # temp.next.prev=temp
                # temp.next.prev=None
                self.size-=1
                if(self.size==0):
                    self.head=None
                    self.tail=None
                print("\nDeletion at location "+str(location)+" successful")
                return
            index+=1
            temp=temp.next

    #Method for Deleting Complete LinkedList
    def deleteLinkedList(self):
        #Checking weather LinkedList exists
        if(self.head==None):
            print("No LinkedList exists")
            return
        print("Deleting LinkedList........")
        self.tail.next=None
        temp=self.head
        while(temp):
            temp.prev=None
            temp=temp.next
        self.head=None
        self.tail=None
        print("Linked List deleted successfully !")

    #Method for reverse traversing LinkedList
    def reverseTraverse(self):
        temp=self.tail
        #Checking weather LinkedList exists
        if(self.head==None):
            print("Single Linked List is empty")
            return
        print("Printing Single LinkedList in Reverse Order ")
        while(temp):
            print(temp.data,end="")
            if(temp==self.head):
                return
            print("=>",end="")
            temp=temp.prev

if __name__ == "__main__":
    circularDoublellst=CircularDoubleLinkedList(0)
    # singlellst.traverse()

    circularDoublellst.insertElement(1)
    circularDoublellst.insertElement(2)
    circularDoublellst.insertElement(3)
    circularDoublellst.insertElement(4)
    circularDoublellst.insertElement(5)
    circularDoublellst.insertElement(6)
    circularDoublellst.insertElement(7)
    circularDoublellst.insertElement(8)

    circularDoublellst.traverse()
    print()
    circularDoublellst.reverseTraverse()
    print()
    circularDoublellst.insertElementLocation(10,4)
    circularDoublellst.insertElementLocation(11,1)
    circularDoublellst.insertElementLocation(12,11)
    circularDoublellst.insertElementLocation(15,7)   
    circularDoublellst.traverse()
    print()
    circularDoublellst.reverseTraverse()
    print()
    circularDoublellst.searchNode(11)
    circularDoublellst.deleteElement(1)
    circularDoublellst.traverse()
    print()
    circularDoublellst.deleteElement(12)
    circularDoublellst.traverse()
    print()
    circularDoublellst.deleteElement(9)
    circularDoublellst.traverse()
    print()
    circularDoublellst.reverseTraverse()
    print()
    circularDoublellst.deleteLinkedList()
    circularDoublellst.deleteLinkedList()