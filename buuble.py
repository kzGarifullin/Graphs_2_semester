import math


def bin_search(a,x) :
    left = -1
    right = len(a)
    while left<right-1:
            m=(left+right)//2
            if a[m]<x :
                left=m
            elif a[m]<x :
                return m
            else:
                right=m
    
    if right<len(a) and a[right]>=x:
        return(right)
    else:
        return(-1)
        
        
n = int(input()) 
a = [[j for j in input().split()] for i in range(n)]

minn=float(a[0][0])
for i in range(n):
    if float(a[i][0])<=minn:
        minn=float(a[i][0])
        k=i

xa=0
ya=-1
xui=[]
kond=input().split()
xb=float(kond[0])-minn
yb=float(kond[1])-float(a[k][1])

pr=xa*xb+ya*yb
    
kor=((xa*xa+ya*ya)*(xb*xb+yb*yb))**0.5
   

if kor==0:
    print("YES")
else:
    cos= pr/kor
    arcos=math.acos(cos)*90/1.5707963267
    
    arcoskond=round(arcos,3)
    flag=False
    print("arcoskond",arcoskond)
    sup=-1
    for i in range(n):
        xb=float(a[i][0])-minn
        yb=float(a[i][1])-float(a[k][1])
        
        pr=xa*xb+ya*yb
        
        kor=((xa*xa+ya*ya)*(xb*xb+yb*yb))**0.5
        if kor!=0:
            cos=pr/kor
            arcos=math.acos(cos)*90/1.5707963267
            
            xui.append(round(arcos,3))
           
    
    rer=xui[:]
    rer.sort()
    
    print(xui)
    print(rer)
    if arcoskond<rer[0] or arcoskond>rer[-1]:
        print("NO")
    else:
        otv=bin_search(rer,arcoskond)
        print('otv',otv)
        
        for i in range(len(xui)):
            
            if rer[otv-1]==xui[i]:
                w1=i
            if rer[otv]==xui[i]:
                w2=i
                


        print(rer[otv-1],"x",rer[otv])

        sup=2
        if sup!=-1:
            x1=float(a[w1][0])
            y1=float(a[w1][1])
            x3=float(a[w2][0])
            y3=float(a[w2][1])
            x2=float(kond[0])
            y2=float(kond[1])
           

            
            a1=x1-x2
            a2=y1-y2
            b1=x3-x2
            b2=y3-y2
            S=a1*b2-a2*b1
            print(S)
            if S<=0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
