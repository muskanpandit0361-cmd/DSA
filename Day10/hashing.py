class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)       


t = HashTable(10)
t.insert(23)
t.insert(43)
t.insert(50)
t.insert(25)
t.insert(89)
t.insert(67)
t.insert(92)

t.display()