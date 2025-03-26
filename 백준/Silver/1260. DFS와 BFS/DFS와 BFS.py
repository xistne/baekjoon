from collections import deque

def dfs(v):
  print(v,end=' ')
  visited[v] = True
  for e in adj[v]:
    if not visited[e]:
      dfs(e)

def bfs(v):
  q= deque([v])
  while q:
    v = q.popleft()
    if not visited[v]:
      visited[v] = True
      print(v,end=' ')
      for e in adj[v]:
        if not visited[e]:
          q.append(e)

n,m,v = map(int,input().split())
adj=[[]for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  adj[a].append(b)
  adj[b].append(a)

for e in adj:
  e.sort()

visited=[False]*(n+1)
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)