#data as key and pand value pair
#{key:value}
#No duplicate
#growable
#mutable
#unordered data

#mydict={
#    101:"prashant",
#    102:"ashish",
#    "103":"mohini",
#    "104":"trivani",
#    101:"ashish",
#    104:"ashish"  #will update the value of 101
#}
#print(mydict)

#a=mydict[102]
#print(a)                #to print values

#mydict[102]="peter"        #to change values
#print(mydict)

#for x in mydict:
#    print(x)                #to print the keys by default

#for x in mydict.values():         #to print values
#    print(x)    

#for x in mydict.items():          #to print values and keys
#    print(x)     

#mydict["mobil_no"]=9876543221
#print(mydict)              #adding new key-value

#mydict.pop(101)
#print(mydict)     #removes pair


#-----------MCQs-------------

#a={(1,2):1,(2,3):2,(4,5):3}
#print(a[4,5])        #returns 3 because it internally takes [4,5] as key

#-----------------
#a={'a':1,'b':2,'c':3}
#print(a['a','b'])        #KeyError: ('a', 'b')  because two keys cannot be passed like this

#------------------
#arr={}
#arr[1]=1
#arr['1']=2
#arr[1]+=1
#sum=0
#for j in arr:
#    sum+=arr[j]
#print(sum)          #returns 4
#-----------------------

#dist={}
#dist[1]=1
#dist['1']=2
#dist[1.0]=4         #updates the value of 1
#sum=0
#for k in dist:
#    sum+=dist[k]
#print(sum)           #returns 6
#----------------------------

#dict={}
#dict[(1,2,4)]=8
#dict[(4,2,1)]=10
#dict[(1,2)]=12
#sum=0
#for k in dict:
#    sum+=dict[k]
#print(sum)
#print(dict)    #30  {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}

#-----------------------------

#box={}
#jars={}
#crates={}
#box['biscuit']=1
#box['cake']=2
#ars['jam']=4
#crates['box']=box
#crates['jars']=jars
#print(len(crates[box]))     #TypeError  because box is considered as dict rather than key

#---------------------

#dict={'c':97,'a':96,'b':98}
#for _ in sorted(dict):
#    print(dict[_])             #96 98 97

#----------------------   
# rec ={"Name":"Python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec))         #returns false
#print(id(rec))               #to print address
#--------------------

# rec={"Name":"Python","Age":"20","Address":"NJ"}
# id1=id(rec)
# print(id1)
# del rec
# print(id1)
# rec={"Name":"Python","Age":"20","Address":"NJ"}
# id2=id(rec)
# print(id2)
# print(id1==id2)           #returns true since all the keypair are same so assign same address

#------------------------------------------------

# dict={
#     "A":50,
#     "B":30,
#     "C":70
# }
# max=0
# maxid=" "
# for k in dict:
#     if dict[k]>max:
#         max=dict[k]
#         maxid=k

# print(maxid)     #return C

#-----------------------------------------

# dict={
#     "X":20,
#     "Y":10,
#     "Z":30
# }
# min=100
# minid=" "
# for k in dict:
#     if dict[k]<min:
#         min=dict[k]
#         minid=k

# print(minid)       #returns Y
 
#----------------------------------------

# input_list = [1, 2, 2, 3, 4, 3, 5]

# output_dict = {}
# for value in input_list:
#     key = str(value)
#     output_dict[key] = output_dict.get(key, 0) + 1

# print(output_dict)  # {'1': 1, '2': 2, '3': 2, '4': 1, '5': 1} 

#----------------------------------------

# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1

# addone('Apple')          #{'Apple':1}
# addone('Banana')         #{'Apple':1,'Banana':1}
# addone('apple')          #{'Apple':1,'Banana':1,'apple':1}
# print(len(fruit))        #len=3    

#----------------------------------------