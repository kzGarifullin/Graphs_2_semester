y=["b","d","c","a","b","a"]
x=["a","b","c","b","d","a","b"]
k=["h","a","r","b","o","u","r"]
B=["h","a","b","r","a","h","a","b","r"]
s=[1, 5, 7, 8, 9, 2, 4,5, 6,5,5,5,5]
def lis(s):
    
  s2=s[:]
  cach=[]
  s.sort()
  N=len(s)
  
  i=0
  while i<N-1:
    if(s[i]==s[i+1]):
      del s[i]
      N=N-1
      i=i-1
    i=i+1
  N=len(s2)
  
  M=len(s) 
  F = [0]*(M+2)

  for i in range(M+2):
            
    F[i]=[0]*(N+2)

  for i in range(1,len(s)+1):
    for j in range(1,len(s2)+1):
      if s2[j-1]==s[i-1]:
        F[i][j]=F[i-1][j-1]+1
          
      else:
        F[i][j]=max(F[i][j-1],F[i-1][j])

  i=len(s)
  j=len(s2)

 
  while i>=0 and j>=0:
    if s2[j-1]==s[i-1] and i!=0 and j!=0:
        
      cach.append(s[i-1])
      i=i-1
      j=j-1
        
    elif F[i-1][j]==F[i][j]:
      i=i-1
        
    else :
      j=j-1
  v=cach[::-1]
  return v

print(lis(s))
