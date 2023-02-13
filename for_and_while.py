import random
#for example
x = range(1,100)
print(list(x))
total=0
for i in range(1,100):
    if i % 3 == 0 :
        total += i
    elif i % 5 == 0:
        total += i
print(total)
#while example
arr = [9, 5, 3, 3, 1, -1, -2, -5, -8]
total2 = 0
j = len(arr) - 1
while arr[j] < 0:
    total2 += arr[j]
    j -= 1
print(total2)