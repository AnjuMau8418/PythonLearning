# Factorial number
"""num = int(input("enter the number:"))
fact=1
ans=1
while fact<=num:
    ans=ans*fact
    fact=fact+1

print(ans)
# Armstrong Number
num=int(input("Enter number:"))
temp=num
sum=0
while temp>0:
    count=temp%10
    sum=sum+count*count*count
    temp=temp//10


if sum==num:
    print(num,"is Armstrong number")
else:
    print(num,"is not a Armstrong number")

# star pattern
row=int(input("Enter the row:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print('x',end=' ')
    print()

for i in range(1, row+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print('')

for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print('')

Tuple = (1, 3, 'Python', "Hello")
x = 0
while x < len(Tuple):
    print(Tuple[x])
    x = x + 1

a = ['A', 'B', 'C', 'D']
b = ['A', 'B', 'C', 'D']
print(a)
print(a is b)#lists are identical but not similar because they don't differ the same object

list = [1, 'x', 4, 5, 6, 'z', 9, 'a', 0, 4]
list2 = [x for x in list if type(x) == int]
list3 = [x for x in list if type(x) == str]
print(list2)
print(list3)

N1 = "Anju Maurya"
N2 = "Anju Maurya"
print(str, id(N1))
print(str, id(N2))

S = "AnjuMaurya"
for ch in range(0, len(S), 2):
    print(S[ch])


Word1="USA North America"
Word2="USA South America"
for letter in Word1:
    if letter in Word2:
        print(letter,end='')"""


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


answer = fib(8)
print(answer)
