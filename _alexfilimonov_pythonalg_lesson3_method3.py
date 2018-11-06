#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import *
n = int(input("Enter qty of elements of array:"))
i = 0
list = []
print("Array before min and max elements replacement:")
iMin=0
iMax=0
Min=101
Max=-1
while  (i<n) :
    list.append(randint(0,100))
    print("Element ",(i+1),":",list[i])
    if (list[i]<Min) :
        iMin=i
        Min=list[i]
    if (list[i]>Max) :
        iMax=i
        Max=list[i]
    i+=1
c=list[iMin]
list[iMin]=list[iMax]
list[iMax]=c
print("Array after min and max elements replacement:", list)