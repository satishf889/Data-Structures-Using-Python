#Class for creating Node with data and pointing to Null
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

#Class for performing LinkedList operations
class DoubleLinkedList:
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
            self.size+=1
            return

        temp=self.head
        while(temp):
            if(temp.next==None):
                node=Node(value)
                self.tail.next=node
                node.prev=temp
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
            temp.prev=node
            self.head=node
            self.size+=1
            print("\nInsertion at location "+str(location)+" successful")
            return

        #Inserting Node at the end of LinkedList
        if(location==self.size):
            node=Node(value)
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
            temp.next.prev=None
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
                    self.tail.prev=None
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
        temp=self.head
        while(temp):
            temp.prev=None
            temp=temp.next
        self.head=None
        self.tail=None
        print("Linked List deleted successfully !")

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
            if(temp.prev!=None):
                print("=>",end="")
            temp=temp.prev

if __name__ == "__main__":
    doublellst=DoubleLinkedList(0)
    # singlellst.traverse()
    doublellst.insertElement(1)
    doublellst.insertElement(2)
    doublellst.insertElement(3)
    doublellst.insertElement(4)
    doublellst.insertElement(5)
    doublellst.insertElement(6)
    doublellst.insertElement(7)
    doublellst.insertElement(8)
    doublellst.traverse()
    print()
    doublellst.insertElementLocation(10,4)
    # doublellst.insertElementLocation(11,1)
    doublellst.insertElementLocation(12,1)
    doublellst.insertElementLocation(11,10)   
    print()
    doublellst.traverse()
    print("\n")

    doublellst.reverseTraverse()
    print("\n")

    doublellst.searchNode(6)
    doublellst.searchNode(20)
    print()
    doublellst.traverse()
    print("\n")
    doublellst.deleteElement(1)
    doublellst.traverse()
    print()
    doublellst.deleteElement(7)
    doublellst.traverse()
    print()
    doublellst.deleteElement(9)
    doublellst.traverse()
    print()
    doublellst.deleteElement(7)
    doublellst.traverse()
    print()
    doublellst.reverseTraverse()
    print("\n")
    doublellst.deleteLinkedList()
    doublellst.deleteLinkedList()

    doublellst.traverse()