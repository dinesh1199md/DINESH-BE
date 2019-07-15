x,y=map(int,input().split())
for i in range(x+1,y):
  for z in range(2,i):
    if(i%z==0):
      break
  else:
      print(i,end=" ")
    
