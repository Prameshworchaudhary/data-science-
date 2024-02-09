# how to create a function
def my_function():
    print("this is my function")
my_function() #calling function
# a function is a block of code which only run when it is called.
# function is creted by def keyword.

#passing arguments
def new_function(fname):
    print(fname)
#calling function
new_function("ram")
new_function('hari')
#we have 2 parameter then we have to also give 2 , if we give 1,3 parameter then it will show the error

#if we donot know the parameter then we can use * 
#If the number of arguments is unknown, add a * before the parameter name:
def name(*kids):
    print("the name of his young son is ",kids[2])
    
name("ram","hari","gopal")

#key aruguments
#You can also send arguments with the key = value syntax.

def function(name1,name2,name3):
    print("my name is ",name2)
function(name3="ram",name2="hari",name1="shyam")

# default parameter

def country(country="napal"):
    print("i am from ",country)
country("india")
country("china")
country()
country("USA")

#PASSING A LIST AS ARGUMENT
def my_function(food):
    for x in food:
        print(x)
        
fruits={"apple","banana","orange"}
my_function(fruits)


    

