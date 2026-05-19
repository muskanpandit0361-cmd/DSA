import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,value):
        self.node=Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.tail.next=self.node
            self.tail=self.node

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, "|", "->", end="")
            current = current.next
        print()

    def find_node(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return current
            current = current.next
        return None

    def addBeg(self,value):
        print("Add Node in Beggining")
        self.node=Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node    

    def addBetween(self, target, value):
        node = self.find_node(target)
        if node is None:
            return False
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        if node is self.tail:
            self.tail = new_node
        return True



if __name__=='__main__':
    object=Linkedlist()
    while True:
        print("1. Add node to end: ")
        print("2. Add node in beginning: ")
        print("3. Insert new node after a given node: ")
        print("4. Display linkedlist: ")
        print("5. Find node in linkedlist: ")
        print("6. Exit ")
        ch=int(input("Enter your choice: "))
        if ch==1:
            value=int(input("Enter value for node: "))
            object.addNode(value)
            print("Node added successfully in single linkedlist.")

        elif ch==2:
            value=int(input("Enter value for node: "))
            object.addBeg(value)

        elif ch==3:
            target=int(input("Enter value of node to insert after: "))
            value=int(input("Enter value for new node: "))
            success = object.addBetween(target, value)
            if success:
                print("New node inserted after", target)
            else:
                print("Target node not found.")

        elif ch==4:
            object.display()

        elif ch==5:
            value=int(input("Enter value to find: "))
            node = object.find_node(value)
            if node is not None:
                print("Found node with value:", node.data)
            else:
                print("Node not found.")
        
        elif ch==6:
            sys.exit()

        else:
            print("Invalid Option.")    




