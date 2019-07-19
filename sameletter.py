asp=int(input())
sas=[]
for k in range(asp):
	c=input()
	sas.append(c)
dine=[]
for k in zip(*sas):
	if(k.count(k[0])==len(k)):
		dine.append(k[0])
	else:
		break
print("".join(dine))
