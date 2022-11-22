b=91
m=100
N=10
def poly_hash(s):
    h=0
    for c in s:
        h=((h*91)+ord(c))%100
    return h
def insert(table, key, value):
    a=[]
    a.append(key)
    a.append(value)
    table[key%10]=a
    return table
t=[[] for _ in range(N)]
M=int(input())
for i in range(M):
    s=input()
    x,y=s.split()
    key=poly_hash(x)
    value=s
    insert(t, key, value)
print(t)
for i in range(10):
    if t[i]!=[]:
        print(i)
        for c in t[i]:
            print(c[0],c[1])
