import sys
sys.setrecursionlimit(10 ** 6)


vertex, edge, current = map(int, input().split())

edges = [[] for _ in range(vertex+1)]

for i in range(edge):
  edge_from, edge_to = map(int,sys.stdin.readline().split())
  edges[edge_from].append((edge_to))
  edges[edge_to].append((edge_from))
  

edges = [sorted(i) for i in edges]

visited = [False] * (vertex+1)


result = [0] * (vertex+1)
count = 0

print(edges)
def dfs(edges, current, visited):
  global count
  
  # 시작 정점 R을 방문 했다고 표시한다.
  # list는 0인덱스부터 시작하므로 1뺌

  visited[current] = True  
  count =  count + 1
  result[current] = count
  # print("이웃",current)
  # print("카운트",count)
  # print(current)

  
   # edge(current) : 정점 start_vertex의 인접 정점 집합 (정점 번호를 오름차순으로 방문한다)
  for close_vertex in edges[current]:

    if visited[close_vertex] == False:
      # print("기준정점",current)
      # print("방문",visited)
      # print("여기서는",count)
      dfs(edges, close_vertex, visited)

          

dfs(edges, current, visited)
for i in range(1,len(result)):
        print(result[i])
