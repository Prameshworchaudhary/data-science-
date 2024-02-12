#Random number in numpy
#What is a Random Number?
#Random number does NOT mean a different number every time. Random means something that can not be predicted logically.


#Generate Random Number
#NumPy offers the random module to work with random numbers.
#
from numpy import random
x=random.randint(100)
print(x)

#Generate Random Float
#The random module's rand() method returns a random float between 0 and 1.
x = random.rand(5)
print(x)

#Integers
#The randint() method takes a size parameter where you can specify the sxhape of an array.
x=random.randint(100,size=(10))
print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5))
print(x)

#choice
x = random.choice([3, 5, 7, 9])
print(x)