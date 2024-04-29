n = int(input())
vector = str(input())
array = vector.split() # split the string into a list separated by space

for i in range(0, n):
    array[i] = int(array[i]) # convert the string to integer
    
array.sort()
array.reverse()
    
for i in range(0, n):
    if array[i] < array[0]:
        print(array[i])
        break
