g,h=(map(int,input().split()))
g=g^h
h=h^g
g=g^h
print(g,h)
