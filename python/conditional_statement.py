# two types of operator
#1. relational operator
# <,>,<=,>=,==,!=
a=10
b=20
print(a>b) #output:false
print(b>a) #output:true
print(a<=b) #output:true
print(a>=b)#output:false
print(a==b)#output:false
print(a!=b) #output:true
 # 2. logical operator
 # and (&&) , or (||) , not (!)
x=10
y=20
z=30
print((x>y)and(y>z)) #output: false
print((x<y)or(y<z)) #output: true

#if else condition
number=20
if(number%2==0):
    print(number,"is a even.")
else:
    print(number,"is a odd.")

#if elseif elseif .... else
num1=30
num2=40
if(num1<num2):
    print(num1,"is less than",num2)
elif(num1>num2):
    print(num1,"is greater than",num2)
else:
    print(num1,"is equal to",num2)
    
    