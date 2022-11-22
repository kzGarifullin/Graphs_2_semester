SumS=0
arr=[]
count=0
k=0
povt=0
povtpred=0
chst=0
flaf=False
while True:
    a=input().split()
    if a[0]=="add":
        arr.append(a)
        
        count+=1
        k=k+1
        
        if count==3:
            x4=float(arr[1][2])
            y4=float(arr[1][3])
        if count>=3:
            
            pos=int(a[1])
            x=float(a[2])
            y=float(a[3])
           
            d=k-1
            if d==float(a[1]):
                
              
                x1=float(arr[0][2])
                y1=float(arr[0][3])
               
                xa=x1-x
                ya=y1-y
              
                xb=x4-x
                yb=y4-y
                
                S=xa*yb-ya*xb
                S=S/2
              
                if S<0:
                    S=-S
                SumS=SumS+S
                x4=float(arr[k-1][2])
                y4=float(arr[k-1][3])
                flag=True
                povtpred=povt
                povt=0
                continue
                
            else:
               
                x1=float(arr[pos][2])
                y1=float(arr[pos][3])
                
                x2=float(arr[pos-1-povtpred][2])
                y2=float(arr[pos-1-povtpred][3])
                
                povt=povt+1
            xa=x1-x
            ya=y1-y
            
            xb=x2-x
            yb=y2-y
           
            S=xa*yb-ya*xb
            S=S/2
            print(arr)
            print('arr[pos]',arr[pos],"   ","arr[k-1]",arr[k-1])
            print(arr[:k-2])
            
            m=arr[:k-2]
            m.extend(arr[-1])
            m.extend(arr[k-2:len(arr)-1])
            arr=m
            print(m)
            if S<0:
                S=-S
            SumS=SumS+S

            
    if a[0]=="end":
        break
    




    if a[0]=="area":
        print(round(SumS,5))
        
        

