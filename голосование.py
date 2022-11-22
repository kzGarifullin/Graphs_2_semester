a=dict()
b=dict()
n=0
for i in range (10):
    k=input()
    
    if k in a:
        val=a.get(k)
        val=val+1
        a[k]=val
    else:
        a.setdefault(k,1)
for i in a.keys():
   
    if a.get(i) in b.keys():
        k=b[a.get(i)]
        
        k.append(i)
        b[a.get(i)]=k
    else:
        c=[]
        c.append(i)
        b[a.get(i)]=c


vs=a.values()
vs=list(vs)
vs.sort()

vs=set(vs)
vs=list(vs)


for i in range(len(vs)):
    print(vs[len(vs)-i-1],*b.get(vs[len(vs)-i-1]))
        

