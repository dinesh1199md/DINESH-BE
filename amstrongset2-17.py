x=int(input())
sum=0
d=x
while x>0:
  s=x%10
  sum=sum+s**3
  x=x//10
if (sum==d):
  print("yes")
else:
  print("no")
