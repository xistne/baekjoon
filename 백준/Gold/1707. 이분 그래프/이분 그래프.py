import sys
from collections import deque

def bfs(v):
    que = deque([v])
    visited[v] = 1
    while que:
        e = que.popleft()
        for i in graph[e]:
            if visited[i] == False:
                visited[i] = -visited[e]
                que.append(i)
            elif visited[i] == visited[e]:
                return False
        
    return True
            
input = sys.stdin.readline
k = int(input())

for _ in range(k):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V+1)
    for i in range(1,V+1):
        if visited[i] == False:
            result = bfs(i)
            if result == False:
                break

    print("YES" if result else "NO")
    
