
z=int(input())
y=list(map(int,input().split()))
y.sort()
if (len(y)==z):
  print(*y)
