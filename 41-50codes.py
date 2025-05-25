#41.Permutations In Which N People Can Occupy R Seats In A Classroom
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
students=int(input())
seats=int(input())
output=fact(students)//fact(students-seats)
print(output)

#42.Maximum Number Of Handshakes
persons=int(input())
handshakes=(persons*(persons-1))//2
print(handshakes)

#43.Addition of two factors
def gcd(num1,num2):
    for i in range(1,min(num1,num2)):
        if num1%i==0 and num2%i==0:
            gcd=i
    return gcd   
n1,d1,n2,d2=list(map(int,input().split()))
denominator=d1*d2
numerator=n2*d1+n1*d2
g=gcd(numerator,denominator)
numerator//=g
denominator//=g
print(f"{numerator}/{denominator}")

#44.Replace 0's with 1
nums=int(input())
for i in str(nums):
    if int(i)==0:
        nums=str(nums).replace('0','1')
print(nums)

#45.Can A Number Be Expressed As A Sum Of Two Prime Numbers
def primes(num):
    arr=[]
    for i in range(2,num):
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            arr.append(i)
    for k in range(0,len(arr)):
        for l in range(k+1,len(arr)):
            if arr[k]+arr[l]==num:
                print(arr[k],arr[l])
num=int(input())
primes(num)

#46.Python Code to Count Possible Decoding Of A Given Digit Sequence
def decoding(s):
    n=len(s)
    if not s or s[0]==0:
        return 0
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        one_digit=int(s[i-1:i])    
        two_digit=int(s[i-2:i])
        if 1<=one_digit<=9:
            dp[i]+=dp[i-1]
        if 10<=two_digit<=26:
            dp[i]+=dp[i-2]
    return dp[n]

s=input()
print(decoding(s))

#47.Area of circle
from math import pi
radius=int(input())
print("{:.2f}".format(pi*radius**2))

#48. Prime Numbers between 1 to 100.
arr=[]
for i in range(2,101):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
    if is_prime:
        arr.append(i)
print(*arr)

#49.number of digits in an integer
num=int(input())
count=0
temp=num
while temp>0:
    digit=temp%10
    count+=1
    temp//=10
print(count)

#50.Converting digit/number to words
def number_to_words(n):
    ones=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens=["ten", "eleven", "twelve", "thirteen", "fourteen", 
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens=["", "", "twenty", "thirty", "forty", 
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n==0:
        return "zero"
    result=""
    if n>=1000:
        result+=ones[n//1000]+ " thousand "
        n%=1000
    if n>=100:
        result+=ones[n//100]+ " hundred "
        n%=100
    if n>=20:
        result+=tens[n//10]+ " "
        n %=10
    elif n>=10:
        result+=teens[n-10]+ " "
        n=0
    if n>0:
        result+=ones[n]+" "
    return result.strip()
num=int(input())
print(number_to_words(num))

