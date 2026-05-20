class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
    
def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)    
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue) 

def searchNode(rootNode,nodeValue):
    if rootNode is None:
        print("Tree is empty.")
        return
    
    elif rootNode.data == nodeValue:
        print("The value is found.")

    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
            print("Value not found.")
            return
        searchNode(rootNode.leftChild,nodeValue)    

    else:
        if rootNode.rightChild is None:
            print("Value not found.")
            return
        searchNode(rootNode.rightChild,nodeValue) 

         


#newBST=None  # to test empty tree

newBST=BSTNode(None)

insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
insertNode(newBST,10)

searchNode(newBST,80)
searchNode(newBST,99)