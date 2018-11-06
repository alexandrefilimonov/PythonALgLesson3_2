#4. Определить, какое число в массиве встречается чаще всего.
from random import *
n = int(input("Enter qty of elements of array:"))
i = 0
list = []
nTheMostShown=-1
qtyofMaxShown=0
while  (i<n) :
    list.append(randint(0,10))
    print("Element ",(i+1),":",list[i])
    if (qtyofMaxShown<list.count(list[i])) :
        nTheMostShown=list[i]
        qtyofMaxShown=list.count(list[i])
    i+=1
print("The most shown element is ", nTheMostShown, ". It's shown ",qtyofMaxShown," times.")

