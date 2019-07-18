c=list(input())
q=len(c)
for k in range(0,q,2):
  c[k],c[k+1]=c[k+1],c[k]
print(*c,sep="")
