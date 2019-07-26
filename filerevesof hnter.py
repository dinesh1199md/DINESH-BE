d1,d2=list(map(int,input().split()))
d3=list(map(int,input().split()))
d3.sort()
d3=d3[::-1]
print(d3[d2-1])
