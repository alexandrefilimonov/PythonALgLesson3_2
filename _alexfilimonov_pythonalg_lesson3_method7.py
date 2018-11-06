#7.В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), 
#так и различаться.

from random import *
n = int(input("Enter qty of elements of array:"))
i = 0
list = []
print("Array:")
while  (i<n) :
    list.append(randint(1,100))
    print("Element ",(i+1),":",list[i])
    i+=1

min1=min([n for n in list])
j = list.index(min1)

list = list[:j] + list[j+1 :]

min2=min([n for n in list])

print("min 1 is:", min1)
print("min 2 is:", min2)


