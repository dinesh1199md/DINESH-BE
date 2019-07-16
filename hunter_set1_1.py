a=int(input())
b=0
list1=input()
list1=list1.split()
list1=list(map(int,list1))
new=[]
for i in range(0,a):
    if((list1.count(list1[i]))>=2):
      if list1[i] not in new:
        new.append(list1[i])
        b=1
if(b==0):
  print("unique")
else:
  for i in range(0,a):
    print(min(new),end=" ")
    new.remove(min(new))
