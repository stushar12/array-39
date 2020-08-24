m=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,m):
        z=int(input())
        arr.append(z)

arr.sort()
i=0
while(i<m-1) :
    flag=0
    while((i+1)<m and arr[i]==arr[i+1]):
        i=i+1
        flag=1
    if flag:
        print(arr[i],end=" ")
    else:
        i=i+1


    