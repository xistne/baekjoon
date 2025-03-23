arr = list(input())

arr_stack = []
result = 0
for i in range(len(arr)):
    if arr[i] == '(':
        arr_stack.append('(')
    else:
        arr_stack.pop()
        if arr[i-1] == '(':
            result += len(arr_stack)
        else:
            result += 1

print(result)
    
