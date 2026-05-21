#stack using linkedlist implementation

import time
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode                #yield is used to get value faster than loop
            curNode = curNode.next    

class Stack:
    def __init__(self):
        self.Linkedlist = Linkedlist()

    def __str__(self):
        values = [str(x.value) for x in self.Linkedlist] 
        return '\n'.join(values)   

    def isEmpty(self):
        if self.Linkedlist.head == None:
            return True
        else:
            return False    

    def push(self,value):
        node = Node(value)    
        node.next = self.Linkedlist.head
        self.Linkedlist.head = node

    def pop(self):
        if self.isEmpty():
            print("Stack id Empty")
        else:     
            nodeValue = self.Linkedlist.head.value     #to store the popping value
            self.Linkedlist.head = self.Linkedlist.head.next   
            return nodeValue 
        
    def peek(self): 
        if self.isEmpty():
            return"Stack is empty"    
        else:
            nodeValue = self.Linkedlist.head.value
            return nodeValue
        
    def delete(self):
        self.Linkedlist.head = None


     

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)

customStack.pop()
print()
print("Stack after pop operation: ")
print(customStack)
 
print("Top element is: ")
print(customStack.peek())