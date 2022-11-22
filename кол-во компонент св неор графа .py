def dfs(vertex,G,used):
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour,G,used)
M=int(input())
N=int(input())
G={i:set() for i in range(M)}#коприхеншэн

for i in range(N):
    v1,v2=input().split()
    v=v1
    u=v2
    
   
    G[int(v)].add(int(u))
    G[int(u)].add(int(v))
    
print(G)
N=0
used=set()
for vertex in G:
    if vertex not in used:
        dfs(vertex,G,used)
        N+=1
print(N)
        
