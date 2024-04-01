len1=int(input("Enter the size of the array1="))
len2=int(input("Enter the size of the array2="))

arr1=[]
arr2=[]
for i in range(len1):
    arr1.append(int(input()))
for j in range(len2):
    arr2.append(int(input()))

m=int(input("Enter the number of elements to be merged in array="))
n=int(input("Enter the number of elements to be merged in array="))

i=m-1
j=n-1
len=n+m-1

while i>=0 and j>=0:
    if arr1[i]>arr2[j]:
        arr1[len]=arr1[i]
        i-=1
        len-=1
    else:
        arr1[len]=arr2[j]
        j-=1
        len-=1

while j>=0:
    arr1[len]=arr2[j]
    j-=1
    len-=1

print(arr1)