n=str(input().casefold())
d=['a','e','o','i','u']
if n>='a' and n<='z':
  if(n in d):
    print("Vowel")
  elif(n not in d):
    print("Consonant")
else:
  print("invalid")
 
