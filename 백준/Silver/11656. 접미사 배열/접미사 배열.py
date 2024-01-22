word = input();
arr = [];
for i in range(len(word)):
  arr.append(word[i:]);

for i in sorted(arr):
  print(i);