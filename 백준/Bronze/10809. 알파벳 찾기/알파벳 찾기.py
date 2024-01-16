word = input();
arr = [];
for i in 'abcdefghijklmnopqrstuvwxyz':
  arr.append(word.find(i));

for i in arr :
  print(i,end=' ');