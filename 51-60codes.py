'''#51.count the number of days in a given month of a year
month=int(input())
year=int(input())
if month==2 and year%400==0 or year%4==0 and year%100!=0:
    print("29 days")
elif month==2:
    print("28 days")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31 days")
else:
    print("30 days")

#52.finding the occurrence of a digit in a given number
num=int(input())
digit =int(input())
num_str=str(num)
count=0
for i in num_str:
    if i==str(digit):
        count+=1
print(count)

#53. find number of integers which has exactly x divisors
def integer(num,x):
    arr=[]
    for i in range(1,num+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==x:
            arr.append(i)
    return len(arr)
num=int(input())
x=int(input())
print(integer(num,x))

#54.find roots of a quadratic equation
import math
def find_roots(a,b,c):
    d = (b**2)-(4*a*c)
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    return root1,root2

a=float(input())
b=float(input())
c=float(input())
r1,r2=find_roots(a,b,c)
print(r1,r2)

#recursions
#55.Power of a Number
base=int(input())
power=int(input())
result=base
for i in range(power-1):
    result=base*result
print(result)

#56. Prime using recursion
def prime(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return prime(n,i+1)
n=int(input())
if prime(n):
    print("Its a prime")
else:
    print("Its not a prime")

#57.Largest in a array using recursion
def largest(A,n):
    if n==1:
        return A[0]
    return max(A[n-1],largest(A,n-1))
A=[1,4,45,6,-50,10,2]
n=len(A)
print(largest(A,n))

#58 Smallest in a array using recursion
def smallest(A,n):
    if n==1:
        return A[0]
    return min(A[n-1],smallest(A,n-1))
A=[1,4,3,-5,-4,8,6]
n=len(A)
print(smallest(A,n))

#59 Reversing a number using recursion
def reverse(n):
    A=[]
    if n==0:
        return ""
    return str(n%10)+reverse(n//10)
n=int(input())
print(reverse(n))

#60 HCF using recursion
def hcf(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    return hcf(n2,n1%n2)
n1=27
n2=18
print(hcf(n1,n2))

#61 LCM using recursion
def hcf(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    return hcf(n2,n1%n2)
def lcm(n1,n2):
    return (n1*n2)//hcf(n1,n2)
n1=23
n2=69
print(lcm(n1,n2))'''

#Length of string using recursion
def length(str):
    if str=="":
        return 0
    return 1+length(str[1:])
str="programming"
print(length(str))











