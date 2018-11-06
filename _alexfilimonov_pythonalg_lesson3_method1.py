#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
i = 2
N=0
while  (i<=99) :
    for j in range(2,9):
        if (i%j==0) :
            N+=1
            break
    i+=1
print("Between 2 and 99 ",N," numbers are divided by some digits in (2..9)")

