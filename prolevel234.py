import math
p12,q12=map(int,input().split())
n12=[]
v1=list(map(int,input().split()))
for i in range(0,q12):
        a12,b12=map(int,input().split())
        n12.append([a12,b12])
for i in n12:
        x1=i[0]-1
        y1=i[1]-1
        print(math.gcd(v1[x1],v1[y1]))
