a=[]

n,pravda=map(int,input().split())

for i in range(n):
    name,ist=input().split()
    ist=int(ist)
    a.append([name,ist])


M=int(input())


count=0

for i in range(M):
    if n==0:
        break

    else:
        count=count%n


    if a[count][1]==0 and pravda==1:
        pravda=0


    elif a[count][1]==0 and pravda==0:
        pravda=1

        a[count][1]=1
        
    elif a[count][1]==1 and pravda==0:
        del a[count]
        n-=1
        count-=1

    count+=1




for i in a:
    print(*i)
