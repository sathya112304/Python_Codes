#21.Prime factor of a number
n1 = int(input())
lst = []
def find_factors(n1):
    if n1<4:
        lst.append(n1)
        return lst
    for i in range(2,n1):
        while(n1%i==0):
            lst.append(i)
            n1 = n1/i
    return lst

print(*set(find_factors(n1)))

#22.Strong Number Program
def fact(num):
    fact=1
    if num<0:
        return "No Negative numbers"
    elif num==0 or num==1:
        return 1
    else:
        for i in range(1,num+1):
            fact=i*fact
    return fact

def strong(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum+=fact(digit)
        temp//=10
    if sum==n:
        print("Strong number")
    else:
        print("Not a strong number")
n=int(input())
strong(n)

#23.Perfect number
num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Its a perfect number")
else:
    print("Not a perfect number")

#24.Perfect square
def per_square(num):
    root=int(num**0.5)
    if root*root==num:
        return "Its a perfect sqaure"
    else:
        return "Not a perfect square"
num=int(input())
print(per_square(num))

#25.Automorphic number
num=int(input())
square=num*num
power=10**len(str(num))
if square%power==num:
    print("Its Automorphic")
else:
    print("Not a automorphic")

#26.Harshad number
def harshad(num):
    str_num=str(num)
    sum=0
    for i in str_num:
        sum+=int(i)
    if num%sum==0:
        print("Its a harshad number")
    else:
        print("Not a harshad number")
num=int(input())
harshad(num)

#27.Abundant number
num=int(input())
total=0
for i in range(1,num):
    if num%i==0:
        total+=i
if total>num:
    print("Its a abundant number")
else:
    print("not a abundant number")

#28.Frienddly pair
def friendly(num):
    total=0
    for i in range(1,num):
        if num%i==0:
            total+=i
    return total
def friendly_pair(num1,num2):
    total1=friendly(num1)
    total2=friendly(num2)
    ratio1=total1/num1
    ratio2=total2/num2
    if ratio1==ratio2:
        print("Friendly pairs")
    else:
        print("Not a Friendly pair")
num1,num2=list(map(int,input().split()))
friendly_pair(num1,num2)

