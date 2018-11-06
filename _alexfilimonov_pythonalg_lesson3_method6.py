#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.
from random import *
n = int(input("Enter qty of elements of array:"))
i = 0
list = []
print("Array:")
while  (i<n) :
    list.append(randint(1,100))
    print("Element ",(i+1),":",list[i])
    i+=1
max=max([n for n in list])
i = list.index(max)
min=min([n for n in list])
j = list.index(min)
#print("min is:", min)
#print("max is:", max)

#print("i is:", i)
#print("j is:", j)
s = sum(list[i:j+1])
if (s==0) :
    s = sum(list[j:i+1])
s-=(min+max)
print("Sum is:", s)