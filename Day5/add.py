import sys
class Queue:
    def __init__(self,size):
        self.myQueue=[]  #creating queue
        self.queueSize=size  #queue size defined

    def isFull(self):
        if len(self.myQueue) == size:
            return True 
        else:
            return False 

    def enQueue(self,value):
        if self.isFull():
            print("Queue is full")   
        else:
            self.myQueue.append(value)        

    def display(self):
        print(self.myQueue)    

    def isEmpty(self):
        if self.myQueue==[]:
            return True
        else:
            return False
        
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty.") 
        else:
            self.myQueue.pop(0)      
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print(self.myQueue[0])    

    def delQueue(self):
        self.myQueue=None
    
    
size=int(input("Enter the size of queue: "))
obj=Queue(size)
print("Queue has created:")
while True:
    print("1. Enqueue: ")     
    print("2. Display Queue: ")
    print("3. DeQueue operation: ")
    print("4. Peek operation: ")
    print("5. Delete queue: ")
    print("6. Exit")
    choice=int(input("Enter Your Choice: "))   

    if choice==1:
        value=int(input("Enter element to add: "))
        obj.enQueue(value)
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.deQueue()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.delQueue()
    elif choice==6: 
        sys.exit()     
    else:
        print("Invalid option")              
            

