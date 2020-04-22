from queue import Queue 

#Class for creating node to be inserted in Tree
class Node:

    #Initialization of Node
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

#Class creating and performing Binary Tree Operations
class BinaryTree:

    #Initialization of Binary Tree Class
    def __init__(self):
        print("Creating Empty Binary Search Tree!!")
        self.root=None
        self.size=0

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
            return
        
        else:
            self.inOrderTraversal(root.left)
            print(str(root.value)+" ",end="")
            self.inOrderTraversal(root.right)
    
    #Method for Post-Order traversal
    def postOrderTraversal(self,root):
        if(root==None):
            return
        
        else:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(str(root.value)+" ",end="")

    def rootValue(self):
        if(self.root==None):
            print("Binary Tree is Empty")
            return
        print("Value of root node is "+str(self.root.value))

    #Method for finding all the leaf nodes
    def leafNodes(self):
        if(self.root==None):
            print("Binary Tree is Empty")
            return

        print("\nLeaf Nodes for crrent Binary Tree are:")
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            node=q.get()
            if(node.left!=None):
                q.put(node.left)
            if(node.left==None and node.right==None):
               print(str(node.value)+" ",end="")
            if(node.right!=None):
                q.put(node.right)
    
    #Method for finding siblings
    def siblings(self):
        if(self.root==None):
            print("Binary Tree is Empty")
            return

        print("\nSiblings for crrent Binary Tree are:")
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            node=q.get()
            if(node.left!=None):
                q.put(node.left)
            if(node.left!=None and node.right!=None):
               print("("+str(node.left.value)+","+str(node.right.value)+") ",end="") 
            if(node.right!=None):
                q.put(node.right)
    
    #Method for Level Order Traversal
    def levelOrderTraversal(self,root):
        if(self.root==None):
            print("Binary Tree is Empty")
            return

        print("\nLevel Order Traversal for crrent Binary Tree is")
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
                
        # print("Count: "+str(count))    
    #Method for inserting Node in Tree
    def insert(self,value):
        nodeToInsert=Node(value)
        if(self.root==None):
            self.root=nodeToInsert
            print("Inserted node with value "+str(value))
            self.size+=1
            return
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            node=q.get()
            if(node.left==None):
                node.left=nodeToInsert
                print("Inserted node with value "+str(value))
                self.size+=1
                return

            if(node.right==None):
                node.right=nodeToInsert
                print("Inserted node with value "+str(value))
                self.size+=1
                return

            if(node.left!=None):
                q.put(node.left)
            if(node.right!=None):
                q.put(node.right)
    
    #Method for searching an element
    def searchNode(self,value):
        if(self.root==None):
            print("Binary Tree is empty")
            return
    
        else:
            q = Queue()
            q.put(self.root)
            while(not q.empty()):
                node=q.get()
                if(node.value==value):
                    print("Value "+str(value)+" present in tree")
                    return

                if(node.left!=None):
                    q.put(node.left)
                if(node.right!=None):
                    q.put(node.right) 

            print("Value "+str(value)+" not present in Tree")

    #Method for deleting complete queue
    def deleteTree(self):
        if(self.root==None):
            print("No tree exists.")
            return
        print("Deleting Tree....")
        self.root=None
        print("Tree deleted successfully!!")
    
    #Delete any Node
    def deleteNode(self,value):
        if(self.root==None):
            print("Binary Tree is empty")
            return
    
        else:
            q = Queue()
            q.put(self.root)
            while(not q.empty()):
                node=q.get()
                if(node.value==value):
                    print("\nValue "+str(value)+" present in tree.Deleting the Node")
                    deepestNode=self.getDeepestNode()
                    node.value=deepestNode.value
                    self.deleteDeepestNode()
                    print("Node deleted successfully!")
                    return

                if(node.left!=None):
                    q.put(node.left)
                if(node.right!=None):
                    q.put(node.right) 

            print("Value "+str(value)+" not present in Tree")

    #Method for deleting deepest node
    def deleteDeepestNode(self):
        if(self.root==None):
            print("No node found.")
            return False
        prev,pres=None,None
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            prev=pres
            pres=q.get()
            if(pres.left==None):
                prev.right=None
                return
            elif(pres.right==None):
                prev.left=None
                return
            if(pres.left!=None):
                q.put(pres.left)
            if(pres.right!=None):
                q.put(pres.right)

    #Method for getting deepest node
    def getDeepestNode(self):
        if(self.root==None):
            print("Tree is empty.")
            return
        q = Queue()
        q.put(self.root)
        node=None
        while(not q.empty()):
            node=q.get()
            if(node.left!=None):
                q.put(node.left)
            if(node.right!=None):
                q.put(node.right) 
        # print("Deepest node is "+str(node.value))
        return node

if __name__ == "__main__":
    binaryTree=BinaryTree()

    binaryTree.insert(1)
    binaryTree.insert(2)
    binaryTree.insert(3)
    binaryTree.insert(4)
    binaryTree.insert(5)
    binaryTree.insert(6)
    binaryTree.insert(7)
    binaryTree.insert(8)
    binaryTree.insert(9)
    print("\nIn-Order Traversal for crrent Binary Tree is")
    binaryTree.inOrderTraversal(binaryTree.root)
    print("\nPre-Order Traversal for crrent Binary Tree is")
    binaryTree.preOrderTraversal(binaryTree.root)
    print("\nPost-Order Traversal for crrent Binary Tree is")
    binaryTree.postOrderTraversal(binaryTree.root)
    binaryTree.levelOrderTraversal(binaryTree.root)
    print()
    binaryTree.searchNode(7)
    binaryTree.deleteNode(1)
    binaryTree.levelOrderTraversal(binaryTree.root)
    binaryTree.leafNodes()
    print("\n")
    binaryTree.rootValue()
    binaryTree.siblings()
    print("\n")
    binaryTree.deleteTree()