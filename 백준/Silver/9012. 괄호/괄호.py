import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    arr_origin = list(input().strip())
    arr_stack = []
    flag = True

    for i in arr_origin:
        if '(' == i :
            arr_stack.append(i)
        elif ')' == i :
            if len(arr_stack) == 0:
                flag = False
                break
            else :
                arr_stack.pop()

    if flag == False or len(arr_stack) != 0:
        print("NO")
    else:
        print("YES")