F=[[0]*10 for i in range(10)]
A=[[0]*10 for i in range(10)]


s=input()
h=s[1]
y1=int(h)

if s[0]=="a":
    x=1
if s[0]=="b":
    x=2
if s[0]=="c":
    x=3
if s[0]=="d":
    x=4
if s[0]=="e":
    x=5
if s[0]=="f":
    x=6
if s[0]=="g":
    x=7
if s[0]=="h":
    x=8
y=9-y1
    
F[y][x]=-1
if y-2>-1:
    if x-1>-1:
        F[y-2][x-1]=-1
    if x+1<11:
        F[y-2][x+1]=-1
if y+2<10:
    if x-1>-1:
        F[y+2][x-1]=-1
    if x+1<11:
        F[y+2][x+1]=-1
if x-2>-1:
    if y-1>-1:
        F[y-1][x-2]=-1
    if y+1<11:
        F[y+1][x-2]=-1
if x+2<10:
    if y-1>-1:
        F[y-1][x+2]=-1
    if y+1<11:
        F[y+1][x+2]=-1
        
    
        
    
        
    
    

s="a1"
h=s[1]
y1=int(h)

if s[0]=="a":
    x=1
if s[0]=="b":
    x=2
if s[0]=="c":
    x=3
if s[0]=="d":
    x=4
if s[0]=="e":
    x=5
if s[0]=="f":
    x=6
if s[0]=="g":
    x=7
if s[0]=="h":
    x=8
y=9-y1

F[y][x]=1
A[y][x]=1

for i in range (10):
    
        print(F[i])
print()

f=1

for i in range (8,0,-1):
    for j in range(1,9,1):
        if F[i][j]!=-1 and f!=1:
            
            if F[i][j-1]!=-1:
                
                A[i][j]=A[i][j-1]+A[i][j]
            if F[i+1][j-1]!=-1:
              
                A[i][j]=A[i+1][j-1]+A[i][j]
            if F[i+1][j]!=-1:
               
                A[i][j]=A[i+1][j]+A[i][j]
        f+=1        
      
     

for i in range (10):
    
        print(A[i])
        

