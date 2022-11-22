



a=input()

n=len(a)
for i in range(1,n+1):
    s1=a[:i]
    f=False
    k=s1[::-1]
    s=s1+"#"+k
    
  
    n=len(s)
    pi=[0]*n
    for i in range(1,n) :
        j=pi[i-1]
        while j>0 and s[i]!=s[j]:
            j=pi[j-1]
        if s[i]==s[j]:
            j+=1
        pi[i]=j
        
     
    for i in range(len(k)+1,len(s)):
        
        if pi[i]==0 :
            if i==len(k)+1:
                print(0,end=" ")
                f =True
            else:
                print(pi[i-1],end=" ")
                f=True
            break
    if f==False:
        print(pi[-1],end=" ")
        

