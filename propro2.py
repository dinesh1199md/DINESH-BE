
a123=int(input())
b123=list(map(int,input().split()))
d123=0
for m in range(0,a123):
	for p in range(0,m):
		if b123[p]<b123[m]:
			d123=d123+b123[p]
print(d123)
