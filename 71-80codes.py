#75.largest in an array
def largest(arr):
    max_val=arr[0]
    for i in arr:
        if i>max_val:
            max_val=i
    return max_val
arr=list(map(int,input().split()))
print(largest(arr))

arr=list(map(int,input().split()))
print(max(arr))

arr=list(map(int,input().split()))
arr.sort()
print(arr[-1])


#76.Smallest Element in an Array
def smallest(arr):
    min_val=arr[0]
    for i in arr:
        if i<min_val:
            min_val=i
    return min_val
arr=list(map(int,input().split()))
print(smallest(arr))

arr=list(map(int,input().split()))
print(min(arr))

arr=list(map(int,input().split()))
arr.sort()
print(arr[0])

77.#Smallest and largest element in an array 
def large_small(arr):
    min_val=arr[0]
    max_val=arr[0]
    for i in arr:
        if i<min_val:
            min_val=i
        else:
            max_val=i
    return [min_val,max_val]
arr=list(map(int,input().split()))
print(large_small(arr))

#78.Second Smallest Element in an Array
def sec_smallest(arr):
    first_small=min(arr)
    min_val=arr[0]
    for i in arr:
        if i<min_val and i!=first_small:
            min_val=i
    return min_val
arr=list(map(int,input().split()))
print(sec_smallest(arr))

#79.sum of elements in an array 
def add(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
arr=list(map(int,input().split()))
print(add(arr))

arr=list(map(int,input().split()))
print(sum(arr))

#80.Reverse an Array
def reverse(arr):
    return (arr[::-1])
arr=list(map(int,input().split()))
print(reverse(arr))

def reverse(arr):
    i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
arr=list(map(int,input().split()))
print(reverse(arr))