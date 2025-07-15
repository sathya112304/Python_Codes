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
print(lcm(n1,n2))

#62 Length of string using recursion
def length(str):
    if str=="":
        return 0
    return 1+length(str[1:])
str="programming"
print(length(str))

