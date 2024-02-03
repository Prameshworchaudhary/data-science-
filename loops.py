# while loops
i=1
while i<6:
    print(i)
    i=i+1

# output: 1 2 3 4 5

#break statement
i=1
while i<6:
    print(i)
    if(i==3):
        break
    i=i+1
# output: 1 2 3 

#continue
i=0
while i<6:
    i=i+1
    if(i==3):
        continue
    print(i)
    
# output: 1 2 3 4 5

#for loops
i=0
for i in range(0,10):
    print(i)
    
fruits=["apple","banana","cherry","mango"]
for x in fruits:
    print(x)
    
for y in range(1,10): #output: from 1 to 9
    print(y)


for z in range(2,20,3): #(2,20,3)=2,2+3=5,5+3=8,11,14,17
    print(z)
