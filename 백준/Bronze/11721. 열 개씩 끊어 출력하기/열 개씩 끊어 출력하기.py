str = input()

for i in range(0,len(str),10):
  if i+10 > len(str):
    print(str[i:])
  else:
    print(str[i:i+10])