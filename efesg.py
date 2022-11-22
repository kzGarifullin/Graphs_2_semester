k=[]
arr=[]
count=0
SumS=0
while True:
    a=input().split()
    if a[0]=="add":
        count+=1
        if count==1:
            arr.append(a)

        c=int(a[1])
        
        if count>=2:
            k=arr[:c]
            k.append(a)
            k=k+arr[c:]
            
        
            
            arr=k
           
    if a[0]=="area":
        x1=float(arr[0][2])
        y1=float(arr[0][3])
        for i in range(len(arr)-2):
        
            x2=float(arr[i+1][2])
            y2=float(arr[i+1][3])
            x=float(arr[i+2][2])
            y=float(arr[i+2][3])
            xa=x1-x
            ya=y1-y
                  
            xb=x2-x
            yb=y2-y
                    
            S=xa*yb-ya*xb
            S=S/2
                          
            if S<0:
                S=-S
            SumS=SumS+S
            
        print(SumS)
        SumS=0


    if a[0]=="end":
        break
