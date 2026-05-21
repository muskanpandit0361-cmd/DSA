# queue implementation using linkedlist

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)    
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next        
    
class Queue:
    def __init__(self):
        self.Linkedlist = Linkedlist()
    
    def __str__(self):
        values = [str(x) for x in self.Linkedlist]
        return  ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.Linkedlist.head == None:
            self.Linkedlist.head = newNode
            self.Linkedlist.tail = newNode
        else:
            self.Linkedlist.tail.next = newNode
            self.Linkedlist.tail = newNode

    def isEmpty(self):
        if self.Linkedlist.head == None:
            return True
        else:
            return False
            
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            nodeValue = self.Linkedlist.head
            if self.Linkedlist.head == self.Linkedlist.tail:
                self.Linkedlist.head = None
                self.Linkedlist.tail = None
            else:    
                self.Linkedlist.head = self.Linkedlist.head.next    
            return nodeValue            

    def peek(self): 
        if self.isEmpty():
            return"Queue is empty"    
        else:
            nodeValue = self.Linkedlist.head.value
            return nodeValue
        
    def delete(self):
        self.Linkedlist.head = None
        self.Linkedlist.tail = None
    


custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)


print("Queue:")
print(custQueue)

print("Deleted item: ",custQueue.dequeue())
print("Queue after deletion:")
print(custQueue)

print("First item in queue: ",custQueue.peek())


print("Deleted item: ",custQueue.dequeue())
print("Queue after deletion:")
print(custQueue)

print("Deleted item: ",custQueue.dequeue())
print("Queue after deletion:")
print(custQueue)

print("Deleted item: ",custQueue.dequeue())
print("Queue after deletion:")
print(custQueue)

print(custQueue.delete())