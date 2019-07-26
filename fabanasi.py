d=int(input())
s=0
f=1
w=1
for i in range(d):
  print(w,end=" ")
  w=f+s
  s=f
  f=w


