#91. Find Maximum Scalar Product of Two Vectors
arr1=[1,2,6,3,7]
arr2= [10,7,45,3,7]
arr1.sort()
arr2.sort()
if len(arr1)!=len(arr2):
    print("Not possible")
sum=0
for i in range(len(arr1)):
    sum+=arr1[i]*arr2[i]
print(sum)

#92.count numbers of even and odd elements in an array
arr=list(map(int,input().split()))
even_count=0
odd_count=0
for i in arr:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count,odd_count)

#93.symmetric pairs in an array 
def symmetric(pairs):
    s=set()
    for (x,y) in pairs:
        s.add((x,y))
        if (y,x) in s:
            print((x,y))
pairs=[(3,4),(1,2),(5,2),(7,10),(4,3),(2,5)]
symmetric(pairs)
