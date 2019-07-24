    
#a
nn=int(input())
tt=3
ss=3
l=[]
l.append(3)
for i in range(1,nn+1):
    if tt==1:
        tt=2*ss
        ss=tt
        l.append(tt)
    else:
        tt=tt-1
        l.append(tt)
print(l[nn-1])
