#string is a sequence of alphabet,digits or special character enclosed withiin single or double quote
msg="hello world"
#we can print a single alphabet with index value
print(msg[0]) #output:h
print(msg[4]) #output:o
#to know th data type of msg use: type()
print(type(msg)) #output: str =>string


#to find the length of  string use: len()
print(len(msg)) #output:11

#slicing operation in string
a="education"
#slicing is an operation to get substring from given  string
print(a[1:4]) #output:duc
#we can have a negative value also
print(a[-3:-1]) #output:io

