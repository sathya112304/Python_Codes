#81.Sort first half in ascending order and second half in descending
def sorting(arr):
    mid=len(arr)//2
    half1=arr[:mid]
    half2=arr[mid:]
    for i in range(len(half1)):
        for j in range(i+1,len(half1)):
            if half1[i]>half1[j]:
                half1[i],half1[j]=half1[j],half1[i]
    for i in range(len(half2)):
        for j in range(i+1,len(half2)):
            if half2[i]<half2[j]:
                half2[i],half2[j]=half2[j],half2[i]
           
    half1.extend(half2)
    return half1
arr=list(map(int,input().split()))
print(sorting(arr))

#82.sort the elements of an array
arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

#83.frequency of elements in an array
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key,values in freq.items():
    print(key,values)

#84.Sorting elements of an array by frequency
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

def sort_key(x):
    return (freq[x], x)
sorted_arr = sorted(arr, key=sort_key)
print(sorted_arr)

#85.
#86.Counting Distinct Elements in an Array
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
count=0
for key,values in freq.items():
    if values==1:
        count+=1
print(count)

#87.Repeating elements in an Array
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
arr=[]
for key,values in freq.items():
    if values>1:
        arr.append(key)     
print(arr)

#88.Non Repeating elements in an Array
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
arr=[]
for key,values in freq.items():
    if values==1:
        arr.append(key)     
print(arr)
    
#89.Duplicates elements from an array
arr=list(map(int,input().split()))
dup=[]
for i in arr:
    if i not in dup:
        dup.append(i)     
print(dup)

#90.minimum scalar product of two vectors
arr1=[1,2,6,3,7]
arr2=[10,7,45,3,7]
arr1.sort()
arr2.sort(reverse=True)
if len(arr1)!=len(arr2):
    print("Not possible")
sum=0
for i in range(len(arr1)):
    sum+=arr1[i]*arr2[i]
print(sum)


