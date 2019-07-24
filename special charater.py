m=str(input())
count2=0
for x in m:
  if(x.isdigit() or x.isalpha() or x.isspace()):
    continue
  count2+=1
else:
  print(count2)   
