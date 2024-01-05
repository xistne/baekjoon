import sys
input=sys.stdin.readline

def mergesplit(data) :
  if len(data) <= 1:
    return data;
  medium = int(len(data) // 2);
  left = mergesplit(data[:medium]);
  right = mergesplit(data[medium:]);

  return merge(left,right);

def merge(left,right):
  merged = list();
  left_point, right_point = 0, 0;

  while left_point < len(left) and right_point < len(right):
    if left[left_point] < right[right_point]:
      merged.append(left[left_point]);
      left_point +=1;
    else:
      merged.append(right[right_point]);
      right_point +=1;

  while left_point < len(left):
    merged.append(left[left_point]);
    left_point +=1;

  while right_point < len(right):
    merged.append(right[right_point]);
    right_point +=1;

  return merged;

n = int(input());
data = [int(input()) for _ in range(n)];
sortedlist = mergesplit(data);
for i in range(n):
    print(sortedlist[i]);
