def poly_hash(s):
    B=5
    M=(1 << 64)-1
    u=0
    h=0
    
    for c in s:
        h=h+ord(c)*(B**u)
    
        
        u+=1
    return h

c=[]
flag=False
a=input()
b=input()
k=0
hashh=poly_hash(a)
k=poly_hash(b[0:len(a)])

if hashh==k and b[0:len(a)]==a:
        c.append(0)
        flag=True
for i in range(1,len(b)-len(a)+1):
    
    k=(k-ord(b[i-1]))//5+ord(b[i-1+len(a)])*5**(len(a)-1)
    
   
   
    
   
    
    if hashh==k and b[i:i+len(a)]==a:
        c.append(i)
        flag=True
if flag==True:
    print(" ".join(map(str, c)))
else:
    print("-1")
