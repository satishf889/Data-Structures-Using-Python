from queue import Queue 

#Class for creating node
class Node:

    #Method for initializing Node
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=0

#Class for creating Binary Search Tree
class AVLTree:
    #List for storing inorder traversal
    inorder=[]
    #Method for initializing avl
    def __init__(self):
        self.root=None

    #Method for pre-order Traversal
    def preOrderTraversal(self,root):
        if(root==None):
            return

        else:
            print(str(root.value)+" ",end="")
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    #Method for In-order traversal
    def inOrderTraversal(self,root):
        if(root==None):
            return None
        
        if(self.root==root):
            self.inorder=[]

        self.inOrderTraversal(root.left)
        print(str(root.value)+" ",end="")
        self.inorder.append(root.value)
        self.inOrderTraversal(root.right)

    #Method for Post-Order traversal
    def postOrderTraversal(self,root):
        if(root==None):
            return
        
        else:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(str(root.value)+" ",end="")

    #Method for Level Order Traversal
    def levelOrderTraversal(self,root):
        if(self.root==None):
            print("Binary Tree is Empty")
            return

        print("\nLevel Order Traversal for current Binary Tree is")
        q = Queue()
        q.put(root)
        count=0
        while(not q.empty()):
            node=q.get()
            print(str(node.value)+" ",end="")
            if(node.left!=None):
                q.put(node.left)
                
            if(node.right!=None):
                q.put(node.right)
    
    #Method for searching in avl
    def searchNode(self,root,value):
        if self.root==None:
            print("avl is empty")
            return
    
        if root==None:
            print("Value {} not present".format(value))
            return

        elif root.value==value:
            print("Value {} found".format(value))            
            return
        
        elif value<=root.value:
            self.searchNode(root.left,value)
        
        elif value>root.value:
            self.searchNode(root.right,value)

    #Method for inserting new Node
    def insert(self,root,value):
        if(self.root==None):
            node=Node(value)
            self.root=node
            print("Value {} inserted successfully".format(value))
            return 

        if(root==None):
            node=Node(value)
            root=node
            print("Value {} inserted successfully".format(value))

        elif(value<=root.value):
            root.left=self.insert(root.left,value)
        
        elif(value>root.value):
            root.right=self.insert(root.right,value)
        
        balance_factor=self.maxHeight(root.left)-self.maxHeight(root.right)
        # print(f'Balance factor at {root.value} is {balance_factor}')
        if(balance_factor>1):
            if self.maxHeight(root.left.left)-self.maxHeight(root.left.right)>=1:
                print("===============================================================")
                print("Left Left Rotation")
                print("Calling right rotation")
                root=self.rightRotation(root)
            else:
                print("===============================================================")
                print("Left Right Rotaion")
                print("Calling left rotation first")
                root.left=self.leftRotation(root.left)
                print("Calling right rotation")
                root=self.rightRotation(root)

        elif(balance_factor<-1):
            if(self.maxHeight(root.right.right)>self.maxHeight(root.right.left)):
                print("===============================================================")
                print("Right Right Rotation")
                print("Calling left rotation")
                root=self.rightRightRotation(root)
            else:
                print("===============================================================")
                print("Right Left Rotation")
                print("Calling right rotation")
                root.right=self.rightRotation(root.right)
                print("Calling right rotation")
                root=self.rightRightRotation(root)
        # root.height=self.maxHeight(root)
        return root

    #Method for right rotation
    def rightRotation(self,currentDisbalancedNode):
        new_root=currentDisbalancedNode.left
        currentDisbalancedNode.left=currentDisbalancedNode.left.right
        new_root.right=currentDisbalancedNode
        if(currentDisbalancedNode==self.root):
            self.root=new_root
        return new_root
    
    #Method for left rotation
    def leftRotation(self,root):
        new_root=root.right
        root.right=root.right.left
        new_root.left=root
        if(root==self.root):
            self.root=new_root
        return new_root
    
    #Method for right right roration
    def rightRightRotation(self,root):
        new_root=root.right
        root.right=root.right.left
        new_root.left=root
        if(root==self.root):
            self.root=new_root
        return new_root

    #Method for height of tree
    def maxHeight(self,node):
        if node==None:
            return 0

        lheight=self.maxHeight(node.left)
        rheight=self.maxHeight(node.right)

        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1        

    #Method to delete avl
    def deleteavl(self):
        if(self.root==None):
            print("avl does not exist.")
            return
        print("Deleting avl..... ")
        self.root=None
        print("avl deleted")

    #Method to delete a node
    def deleteNode(self,root,value):
        if(self.root==None):
            print("No value to delete. avl is empty")
            return None

        elif(root==None):
            print("Value {} not present in avl".format(value))
            return

        elif(value<root.value):
            root.left=self.deleteNode(root.left,value)
        
        elif(value>root.value):
            root.right=self.deleteNode(root.right,value)
        
        else:
            if(root.left!=None and root.right!=None):
                successor=self.successor(root.value)
                # root.value=successor
                self.deleteNode(self.root,successor)
                root.value=successor
            elif(root.left!=None):
                root=root.left
            elif(root.right!=None):
                root=root.right
            else:
                root=None
        # print("Root value is {}".format(root.value))
        if root==None:
            return root
        balance_factor=self.maxHeight(root.left)-self.maxHeight(root.right)
        # print(f'Balance factor at {root.value} is {balance_factor}')
        if(balance_factor>1):
            if self.maxHeight(root.left.left)-self.maxHeight(root.left.right)>=1:
                print("===============================================================")
                print("Left Left Rotation")
                print("Calling right rotation")
                root=self.rightRotation(root)
            else:
                print("===============================================================")
                print("Left Right Rotaion")
                print("Calling left rotation first")
                root.left=self.leftRotation(root.left)
                print("Calling right rotation")
                root=self.rightRotation(root)

        elif(balance_factor<-1):
            if(self.maxHeight(root.right.right)>self.maxHeight(root.right.left)):
                print("===============================================================")
                print("Right Right Rotation")
                print("Calling left rotation")
                root=self.rightRightRotation(root)
            else:
                print("===============================================================")
                print("Right Left Rotation")
                print("Calling right rotation")
                root.right=self.rightRotation(root.right)
                print("Calling left rotation")
                root=self.rightRightRotation(root)
        return root

    #Method for finding successor
    def successor(self,value):
        print("Successor of {} is {}".format(self.inorder[self.inorder.index(value)],self.inorder[self.inorder.index(value)+1]))
        index=self.inorder.index(value)+1
        return self.inorder[index]

if __name__ == "__main__":
    avl=AVLTree()
    avl.insert(avl.root,30)
    avl.insert(avl.root,20)
    avl.insert(avl.root,40)
    avl.insert(avl.root,10)
    avl.insert(avl.root,5)
    avl.insert(avl.root,3)
    avl.insert(avl.root,4)
    avl.insert(avl.root,50)
    avl.insert(avl.root,60)
    avl.insert(avl.root,70)
    avl.insert(avl.root,65)
    avl.levelOrderTraversal(avl.root)
    print("\n")
    print(f'Height is {avl.maxHeight(avl.root)}')
    print("\nIn-order sequence for current Binary Tree is")
    avl.inOrderTraversal(avl.root)
    print()
    avl.deleteNode(avl.root,10)
    avl.deleteNode(avl.root,5)
    avl.deleteNode(avl.root,3)
    print()
    avl.levelOrderTraversal(avl.root)
    # # print("\nIn-order sequence for current Binary Tree is")
    # avl.inOrderTraversal(avl.root)
    print("\npre-order sequence for current Binary Tree is")
    avl.preOrderTraversal(avl.root)
    print("\n")
    avl.searchNode(avl.root,14)
    avl.searchNode(avl.root,15)
    avl.searchNode(avl.root,13)
    avl.deleteavl()