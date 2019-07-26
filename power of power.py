k1,k2=list(map(int,input().split()))
for i in range(1,k1):
  ds=k2**i
  if(k1==ds):
    print("yes")
    break
else:

  print("no")  
