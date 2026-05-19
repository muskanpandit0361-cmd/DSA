class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

ll=Linkedlist()

ll.head=Node(5)
second=Node(18)
third=Node(15)
fourth=Node(20)

#connecting nodes
ll.head.next=second
second.next=third
third.next=fourth

while ll.head!=None:
    print(ll.head.data,"|",ll.head.next,"->",end="")   #prints node+address
    ll.head=ll.head.next

