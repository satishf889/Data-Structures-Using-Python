#Class for creating Node with data and pointing to Null
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.head=None
    
    def push(self,value):
        node=Node(value)
        node.next=self.head   
        self.head=node
        # print("Pushed "+str(value)+" in stack")
    
    def pop(self):
        if(self.head==None):
            print("No element found")
            return
        # print("Deleting "+str(self.head.data))
        deleted_node=self.head.data
        self.head=self.head.next
        return deleted_node

    def peek(self):
        if(self.head==None):
            print("No element found")
            return
        print("Value on the top is "+str(self.head.data))

    def delete(self):
        print("Deleting Stack.....")
        self.head=None
        print("Stack Deleted.")
    
    def isEmpty(self):
        if(self.head==None):
            return True

        return False

if __name__ == "__main__":
    stack=Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.delete()
    stack.pop()
    stack.pop()
    stack.pop()

    stack.peek()
    