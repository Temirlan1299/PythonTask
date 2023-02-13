from random import random, randrange, randint
#use range
x = range(25,31)
for n in x:
  print(n)
print(type(range(1)))
print(list(range(1,25,10)))
print(sum(range(5,100)))
print(len(range(4,85,10)))

#use function random,randint...
print(randint(5,300))
print(randrange(6, 12))
print(randrange(5, 100, 5))
x = random()
print(x)
#use enumerate
list = [5 , 16 , 25, 700]
for i in enumerate(list):
    print(i)
a = [10, 30, 50, 70]
for val1,val2 in enumerate(a):
    a[val1] = val2 + 6
print(a)
#to solve problems
#1
a = int(input())
b = int(input())
for i in range(a, b):
    if(a<=b):
        print(i)
    else:
        print("a > b")
#2
a = int(input())
b = int(input())
if a<b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
#3
a = 30
b = 6
for i in range(a - int((a % 2) == 0), b - 1, -2):
        print(i)
#4
n = int(input())

s = sum(range(1, n + 1))

for i in range(n - 1):

   s -= int(input())

print(s)



