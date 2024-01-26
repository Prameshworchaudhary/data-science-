#List in python 
a=[10,20,30,40,50]
print(type(a)) #output:list
print(a)
print(a[0]) #output:10
#we can change the value with help of index number
a[0]=500
print (a[0]) #output:500
#silicing in list
print(a[1:4]) #output:[20,30,40]
#method for list : use dir(a) to see the method
a.append("abc") #use to add "abc" string in list
a.append(2.5)
print(a)

#dictionaries: key with values
d={"name":"hari","age":20,"address":"koteshwor,kathmandu"}
print(type(d))
print(d)
print(d.values())
print(d.items())

#seta: to remove duplicate values
s=set("aaabbbcccddddeeefff")
print(type(s))
print(s)
s={10,10,20,20,"abc","abc"}
print(s)

#tuples
a=(10,30,20,40,50)
print (a[0])
#we cannot change the tuple values : a[0]=100
print(type(a))
print(a)