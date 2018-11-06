#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import *
n = int(input("Enter qty of elements of array:"))
i = 0
list = []
print("Array:")
while  (i<n) :
    list.append(randint(-100,100))
    print("Element ",(i+1),":",list[i])
    i+=1
print("The largest negative number:", max([n for n in list if n<0]))


