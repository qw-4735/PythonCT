from collections import deque

v, e = map(int, input().split())

graph = [[] for i in range(v+1)]

indegree = [0] * (v+1)

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    

    while q:
        node = q.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 1:
                q.append(i)
    
    for i in result:
        print(i, end=' ')