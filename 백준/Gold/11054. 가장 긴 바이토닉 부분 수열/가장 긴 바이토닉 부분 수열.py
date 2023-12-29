n = int(input());
arr = list(map(int,input().split()));
arr_reverse = arr[::-1];
increase = [1] * n;
decrease = [1] * n;

for i in range(1,n):
  for j in range(i):
    if arr[j] < arr[i]:
      increase[i] = max(increase[i], increase[j] + 1);
    if arr_reverse[j] < arr_reverse[i]:
      decrease[i] = max(decrease[i], decrease[j] + 1);

decrease.reverse();
result = [0 for i in range(n)];
for i in range(n):
  result[i] = increase[i] + decrease[i] -1;

print(max(result));