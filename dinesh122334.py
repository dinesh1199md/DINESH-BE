o=int(input())
e=list(map(int,input().split()))
d1=[]
for i in e:
  if e.count(i)>1:
    if i not in d1:
      d1.append(i)
if len(d1)>=1:
  print(d1[0])
else:
  print("unique")

    
      
