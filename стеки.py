s=input().split()
stack=[]


k=0
summ=0
count=0
flag=False
for c in s:
    count+=1
    if c=="#":
        
        stack.append(c)
        if stack[0]=="#":
            flag=True
        for i in range(count-1):
            summ=float(stack[i])+float(summ)
           
        for i in range(count):
            stack.pop(-1)
           
        stack.append(summ)
        count=1
        summ=0
    elif c=="%":
        count=1
        stack.append(c)
        if len(stack)==3:
            stack.pop(-1)
            b=stack.pop(-1)
            a=stack.pop(-1)
			
            f=int(b)*int(a)/100
         
            stack.append(f)
            
        elif len(stack)==2:
            
            flag=True
            break
            stack.pop(-1)
            stack.pop(-1)
            stack.append(0)
        elif len(stack)==1:
            flag=True
            break
            stack.pop(-1)
            stack.append(0)
			
		
		
          
	
    else:
       
        stack.append(int(c))
		
		
   
d=0
if flag==False:
    if len(stack)>1 :
        for i in range(len(stack)):
            d=d+stack[i]
        print(d)
    else:
        print(stack[0])
else:
    k=1.1
    c=1.1
    print(k-c)



