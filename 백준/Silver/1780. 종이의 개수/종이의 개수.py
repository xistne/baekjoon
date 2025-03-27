import sys
input = sys.stdin.readline

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().split())))

result = {-1:0,0:0,1:0}

def divide(x, y, n):
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        divide(x+(n//3)*a,y+(n//3)*b,n//3)
                return
    
    result[color] +=1

divide(0,0,n)

for i in result.values():
    print(i)
