
def selection_sort(b) :
    n=len(b)
    for i in range (n-1) :
        k=i
        for j in range(i+1,n) :
            if b[k]>b[j] :
                k=j
        b[i],b[k]=b[k],b[i]


def d(s):
    summ=0
    m=s
    while m>0:
        summ+=m%10
        m=m//10
    return summ

N=int(input())


a=[]
for i in range(N) :
    a.append(int(input()))
n=len(a)



for i in range(n) : #year
    j=i-1
    while j>=0 and d(a[j])>d(a[j+1]) :
        a[j],a[j+1]=a[j+1],a[j]
        j-=1




for i in range(n) : #month
    j=i-1
    while j>=0 and a[j]>a[j+1] and d(a[j])==d(a[j+1]) :
        a[j],a[j+1]=a[j+1],a[j]
        j-=1





for i in range(len(a)):
   
    print(a[i])
    
 
