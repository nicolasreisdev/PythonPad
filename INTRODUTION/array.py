import math as m
import random as r 

vector = [] #array in c++
for i in range(0,5):
    x = int(input("Enter a number: "))
    vector.append(x) #method for add a element in the array

print("The vector is: ")    
for i in vector:
    print(i)

#method for know the size of array
print("The size of vector is: ")
y = vector.__len__() #method for know the size of array
print(y)

#method for reverse the array
print("The vector reverse is: ")
vector.reverse() #method for reverse the array
for i in range(0,5):
    print(vector[i]) 

#method for sort the array
print("The vector sort is: ")
vector.sort() #method for sort the array
for i in range(0,5):
    print(vector[i])



print("The vector is: ")
vector.insert(0, 0) #method for insert a element in the array
vector.append(6) #method for insert a element in the end of array
for i in range(0,vector.__len__()):
    print(vector[i])
    
    