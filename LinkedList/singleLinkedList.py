#Class for creating Node with data and pointing to Null
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

#Class for performing LinkedList operations
class LinkedList:
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
            self.head=node
            self.tail=node
            self.size=1
            return

        temp=self.head
        while(temp):
            if(temp.next==None):
                node=Node(value)
                temp.next=node
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
            node.next=temp
            self.head=node
            self.size+=1
            print("\nInsertion at location "+str(location)+" successful")
            return

        #Inserting Node at the end of LinkedList
        if(location==self.size):
            node=Node(value)
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
                node.next,temp.next=temp.next,node
                self.size+=1
                print("\nInsertion at location "+str(location)+" successful")
                return
            index+=1
            temp=temp.next

    #Method for Deleting Node from LinkedList
    def deleteElement(self,location):

        #Checking weather LinkedList exists
        if(self.head==None):
            print("Current length of Linked List is 0. No Node to delete")
            return

        #Checking weather user given location should not be greater than Size
        if(location>self.size):
            print("Please enter correct location currently we have "+str(self.size-1)+" elements")
            return

        temp=self.head

        #Deleting Node at the start of LinkedList
        if(location-1==0):
            self.head=temp.next
            self.size-=1
            if(self.size==0):
                self.head=None
                self.tail=None
            print("\nDeletion at location "+str(location)+" successful")
            return

        #Deleting a node at end
        if(location==self.size):
            temp=self.head
            while(temp):
                if(temp.next==self.tail):
                    temp.next=None
                    self.tail=temp
                    self.size-=1
                    if(self.size==0):
                        self.head=None
                        self.tail=None
                    print("\nDeletion at location "+str(location)+" successful")
                    return
                temp=temp.next

        #Deleting Node at any other location of LinkedList
        index=0
        while(temp):
            if(index==location-1):
                temp.next=temp.next.next
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
        self.head=None
        self.tail=None
        print("Linked List deleted successfully !")

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
            if(temp.next!=None):
                print("=>",end="")
            temp=temp.next

if __name__ == "__main__":
    singlellst=LinkedList(0)
    # singlellst.traverse()

    singlellst.insertElement(1)
    singlellst.insertElement(2)
    singlellst.insertElement(3)
    singlellst.insertElement(4)
    singlellst.insertElement(5)
    singlellst.insertElement(6)
    singlellst.insertElement(7)
    singlellst.insertElement(8)
    singlellst.traverse()
    print()
    singlellst.insertElementLocation(10,4)
    singlellst.insertElementLocation(11,1)
    singlellst.insertElementLocation(12,12)
    singlellst.insertElementLocation(11,10)   
    print()
    singlellst.traverse()
    print()
    singlellst.deleteElement(1)
    singlellst.traverse()
    print()
    singlellst.deleteElement(7)
    singlellst.traverse()
    print()
    singlellst.deleteElement(9)
    singlellst.traverse()
    print()

    singlellst.searchNode(10)

    singlellst.deleteLinkedList()
    singlellst.deleteLinkedList()
