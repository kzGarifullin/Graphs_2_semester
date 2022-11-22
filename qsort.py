import collections
c = collections.Counter()
n=int(input())
a=dict()
arr=[]
for i in range(n):
    t=input().split()
    if int(t[1])>=0: 

        k=int(t[1])/int(t[0])
    else:
        k=int(t[1])/int(t[0])
        k=str(k)
        k="v"+k
    arr.append(k)

for word in arr:
    c[word] += 1
        
    


        

h=c.most_common(1)
j=dict(h)

for value in j:
    r=value

val=j.get(r)
print(val)
