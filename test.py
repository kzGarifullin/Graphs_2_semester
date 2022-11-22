

a=list(map(int,input().split()))
n=len(a)
f=True
i=0

while f :
    f=False
    b=a[:]
    for j in range (n-i-1) :
        b=a[:]
        if(a[j]>a[j+1]) :
            a[j],a[j+1]=a[j+1],a[j]
            f=True
        
        if a!=b :
            
            for o in range(n) :
                print(a[o],end = " ")
            print(" ")
        
    
    i+=1
      
