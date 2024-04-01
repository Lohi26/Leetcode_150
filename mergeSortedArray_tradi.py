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

for i in range(n):
    arr1[m+i]=arr2[i]

print(sorted(arr1,reverse=False))