d4=int(input())
d1=list(map(int,input().split()))
kd=1
for i in d1:
  kd*=i
for j in d1:
  j=kd/j
  print(int(j),end=" ")
