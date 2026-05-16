#order wise data
#heterogenous data
#represented by ()
#growable
#immutable

#which to choose? List or tupple???
#if the client requirement is fixed and will not change in future then choose  tuple for example phone no
#for unfixed requirements choose list

#mytuple=("prashant","Ashish","Rahul","sandip","komal","ankush","rajesh",23,3.15,77,"sandip")
#print(mytuple)
#print(type(mytuple))
#mytuple[2]="sunil"  #error because of immutability
#print(mytuple)

#init_tuple=()
#print(init_tuple.__len__()) #returns 0

init_tuple_a= 'a','b'
init_tuple_b= ('a','b')
print(init_tuple_a==init_tuple_b)  #returns true

init_tuple_a='1','2'
init_tuple_b=('3','4')
print(init_tuple_a+init_tuple_b)  #returns ('1', '2', '3', '4')

l=[1,2,3]
init_tuple=('python',)*(l.__len__()-l[::-1][0])
print(init_tuple)   #returns()

init_tuple=("python",)*3
print(type(init_tuple))  #class tuple

tuple=((1,2)) *7
print(tuple)
print(len(tuple[3:8]))