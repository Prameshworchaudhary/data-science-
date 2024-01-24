#operation (a+b)
a=10
b=20
c=30
#addition
add=a+b
print("addition is ",add) #output:addition is 30
add=b+c 
#the value of add is change as same memory location but value different
print("addition is ",add) #output:addition is 50


#subtraction (a-b)
sub=b-a
print("subtraction is ",sub) #output:subtraction is 10
sub=c-b 
#the value of sub is change as same memory location but value different
print("subtraction is ",sub) #output:subtraction is 10

#multiplication (a*b)
mul=a*b
print("multiplication is ",mul) #output:multiplication is 200
mul=b*c 
#the value of mul is change as same memory location but value different
print("multiplication is ",mul) #output:multiplication is 600

#division (a/b)
div=b/a
print("division is ",div) #output:division is 2.0
div=c/b
#the value of div is change as same memory location but value different
print("division is ",div) #output:division is 1.5

#modulus (a%b)
mod=b%a
print("modulus is ",mod) #output:modulus is 0
mod=c%b 
#the value of mod is change as same memory location but value different
print("modulus is ",mod) #output:modulus is 10

#floor division (a//b)
div=b//a
print("division is ",div) #output:division is 2
div=c//b
#the value of div is change as same memory location but value different
print("division is ",div) #output:division is 1

#power (a**b)
a=2
b=3
power=a**b
print("output is ",power) #output is 8








