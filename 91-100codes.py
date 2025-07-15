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

#94.maximum product sub-array in a given array
arr=list(map(int,input().split()))
result=arr[0]
for i in range(len(arr)):
    mul=arr[i]
    for j in range(i+1,len(arr)):
        result=max(result,mul)
        mul*=arr[j]
        result=max(result,mul)
print(result)

#95.whether arrays or disjoint or not 
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
disjoint=True
for i in arr1:
    if i in arr2:
        disjoint=False
if disjoint:
    print("Disjoint")
else:
    print("Not Disjoint")

#96. whether array is subset of another array
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
is_subset=True
for i in arr2:
    if i not in arr1:
        is_subset=False
if is_subset:
    print("Arr2 is subset of Arr1")
else:
    print("Arr2 is not subset of Arr1")

#97.
#98.Sum of Minimum Absolute Difference of Array
arr=list(map(int,input().split()))
min_diff=arr[0]
result=0
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        sum+=(abs(arr[i]-arr[j]))
        result=min(result,sum)
print(result)  


