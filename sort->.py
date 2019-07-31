d4=int(input())
d1=list(map(int,input().split()))
d1.sort()
j=d1[::-1]
print(*j,sep="->")
