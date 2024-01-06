n = int(input())
result=[]
for i in range(n):
  x,y = map(int,input().split())
  result.append(((x,y)))
result.sort()
for i in result:
  print(i[0],i[1])