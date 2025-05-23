#11.Sum of Digits
num=input()
sum=0
for i in num:
    sum+=int(i)
print(sum)

#12.Reverse of a number
num=input()
num1=num[::-1]
print(num1)

#Reverse of a number
num=int(input())
temp=num
arr=[]
while temp>0:
    rem=temp%10
    arr.append(rem)
    temp//=10
print("".join(map(str,arr)))

#13.Palindrome
num=input()
reverse=num[::-1]
if num==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#14.Armstrong Number
num=int(input())
power=len(str(num))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**power
    temp=temp//10
if sum==num:
    print("Its armstrong number")
else:
    print("Not a armstrong")

#15.Armstrong  umbers in a range
num1,num2=list(map(int,input().split()))
lst=[]
for i in range(num1,num2+1):
    power=len(str(i))
    temp=i
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**power
        temp=temp//10
    if sum==i:
        lst.append(i)
print(*lst)

#16.Fibonacci Series upto nth term
n=int(input())
a,b=0,1
for i in range(0,n):
    a,b=b,a+b
    print(a,end=" ")

#17.Nth term fibanocci
n=int(input())
a,b=0,1
count=0
while count<n:
    a,b=b,a+b
    count+=1
print(a)

#18.Factorial of a Number
num=int(input())
fact=1
if num<0:
    print("NO negative accepted")
elif num==0:
    print("1")
for i in range(1,num+1):
    fact=i*fact
print(fact)  

#19.find Power of a number
a,b=list(map(int,input().split()))
print(pow(a,b))

a,b=list(map(int,input().split()))
result=1
for i in range(b):
    result*=a
print(result)

#20.find factors of a number
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")
    continue






    