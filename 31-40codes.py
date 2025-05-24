#31.GCD
num1=int(input())
num2=int(input())
for i in range(1,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)

#32.Binary to decimal
num=int(input())
val=0
base=1
while num>0:
    rem=num%10
    val=val+rem*base
    num//=10
    base=base*2
print(val)

num=input()
val=int(num,2)
print(val)

#33. Octal to decimal
num=int(input())
val=0
base=1
while num>0:
    rem=num%10
    val=val+rem*base
    num//=10
    base=base*8
print(val)

num=input()
val=int(num,8)
print(val)

#34.Hexadecimal to decimal
num=input()
val=int(num,16)
print(val)

#35,36,37 Decimal to all bin,oct,hex
num=int(input())
print(bin(num)[2:])
print(oct(num)[2:])
print(hex(num)[2:])

#38.Binary to octal
num=int(input())
val=0
base=1
while num>0:
    rem=num%10
    val=val+rem*base
    num//=10
    base=base*2
print(oct(val)[2:])

#39.Octal to binary
num=int(input())
val=0
base=1
while num>0:
    rem=num%10
    val=val+rem*base
    num//=10
    base=base*8
print(bin(val)[2:])

#40. find out the quadrant in which the given co-ordinate lie
x,y=list(map(int,input().split()))
if x>0 and y>0:
    print("Ist Quadrant")
elif x<0 and y>0:
    print("IInd Quadrant")
elif x<0 and y<0:
    print("IIIrd Quadrant")
elif x>0 and y<0:  
    print("IVth Quadrant")
elif x!=0 and y==0:
    print("x-axis")
elif x==0 and y!=0:
    print("y-axis")
else:
    print("Origin")




