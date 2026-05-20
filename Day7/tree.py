# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]

#     def __str__(self,level =0):
#         ret="  "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret    

#     def addChild(self,object):
#         self.child.append(object)
#         print("Tree node added")    

# rootNode=Tree("Drinks")
# hot = Tree("Hot")
# cold = Tree("Cold")
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# nonalcoholic = Tree("Nonalcoholic")
# alcoholic = Tree("Alcoholic")        

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(nonalcoholic)
# cold.addChild(alcoholic)

# print(rootNode)

#output:
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# Drinks
#   Hot
#     Tea
#     Coffee
#   Cold
#     Nonalcoholic
#     Alcoholic



#--------------------------------------------------

class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[]

    def __str__(self,level =0):
        ret="  "*level+str(self.data)+"\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret    

    def addChild(self,object):
        self.child.append(object)
        print("Tree node added") 


N1=Tree("N1")
N2=Tree("N2")
N3=Tree("N3")
N4=Tree("N4")
N5=Tree("N5")
N6=Tree("N6")
N7=Tree("N7")
N8=Tree("N8")

N1.addChild(N2)
N1.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N6)
N4.addChild(N7)
N4.addChild(N8)

print(N1)

#output:
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# Tree node added
# N1
#   N2
#     N4
#       N7
#       N8
#     N5
#   N3
#     N6

