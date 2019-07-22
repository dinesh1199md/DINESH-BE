from statistics import median
z=int(input())
y=list(map(int,input().split()))
y.sort()
if(len(y)==z):
  print(median(y))
