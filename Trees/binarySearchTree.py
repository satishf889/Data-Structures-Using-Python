from queue import Queue 

#Class for creating node
class Node:

    #Method for initializing Node
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

#Class for creating Binary Search Tree
class BinarySearchTree:
    #List for storing inorder traversal
    inorder=[]
    #Method for initializing BST
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
    
    #Method for searching in BST
    def searchNode(self,root,value):
        if self.root==None:
            print("BST is empty")
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

        return root

    #Method to delete BST
    def deleteBST(self):
        if(self.root==None):
            print("BST does not exist.")
            return
        print("Deleting BST..... ")
        self.root=None
        print("BST deleted")

    #Method to delete a node
    def deleteNode(self,root,value):
        if(self.root==None):
            print("No value to delete. BST is empty")
            return None

        elif(root==None):
            print("Value {} not present in BST".format(value))
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
        return root

    #Method for finding successor
    def successor(self,value):
        print("Successor of {} is {}".format(self.inorder[self.inorder.index(value)],self.inorder[self.inorder.index(value)+1]))
        index=self.inorder.index(value)+1
        return self.inorder[index]

if __name__ == "__main__":
    bst=BinarySearchTree()
    bst.insert(bst.root,8)
    bst.insert(bst.root,3)
    bst.insert(bst.root,12)
    bst.insert(bst.root,1)
    bst.insert(bst.root,6)
    bst.insert(bst.root,9)
    bst.insert(bst.root,14)
    bst.levelOrderTraversal(bst.root)
    print("\nIn-order sequence for current Binary Tree is")
    bst.inOrderTraversal(bst.root)
    print("\npre-order sequence for current Binary Tree is")
    bst.preOrderTraversal(bst.root)
    print("\n")
    bst.searchNode(bst.root,14)
    bst.searchNode(bst.root,15)
    bst.deleteNode(bst.root,8)
    print("BST after deletion is")
    bst.levelOrderTraversal(bst.root)
    print()
    bst.deleteBST()
    bst.searchNode(bst.root,13)