#51.count the number of days in a given month of a year
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



