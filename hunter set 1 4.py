input1=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    if(i==arr[i]):
        print(arr[i],end=" ")
count=0
for i in range(0,len(arr)):    
    if (i!=arr[i]):
        count+=1
if(count==len(arr)):
    print(-1)
