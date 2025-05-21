# Number Is Positive Or Negative
num=int(input())
if num>0:
    print("Positive")
else:
    print("Negative")

#  Number is Even or Odd
num=int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")

#sum of N natural numbers
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Sum of First N Natural Numbers
num=int(input())
sum=(n*(n+1))/2
print(int(sum))

# Sum of Numbers in a given Range in Python
start,end=list(map(int,input().split()))
sum=0
for i in range(start,end+1):
    sum+=i
print(sum)

#Greatest of Two Numbers
num1,num2=list(map(int,input().split()))
print(num1 if num1>num2 else num2)

#Greatest of the Three Numbers
num1,num2,num3=list(map(int,input().split()))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

#Leap Year Program
year=int(input())
if year%4==0 or year%400==0 and year%100!=0:
    print("Its a leap year")
else:
    print("Not a leap year")

#Prime Number or not
num=int(input())
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print("Its a prime")
else:
    print("not a prime")
    
#Prime Numbers In a Given Range
low,high=list(map(int,input().split()))
arr=[]
for i in range(low,high+1):
    if i<2:
        continue
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        arr.append(i)
print(*arr)
    