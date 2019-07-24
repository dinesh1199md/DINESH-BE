k12=int(input())
k13=list(map(int,input().split()))
x=0
jj=0
for i in k13:
  if(i==jj):
    print(i,end=" ")
    x+=1
  jj+=1
if(x==0):
  print(-1)
