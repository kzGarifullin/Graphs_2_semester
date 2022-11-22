def bubble_sort2d(matrix,N,M) :
    a=[]
    for i in range (N):
        for j in range(M):
            a.append(matrix[i][j])
    
    f=True
    flag=True
    i=0
    n=N*M
    for o in range(n) :
        print(a[o],end = " ")
        if o==n/2-1:
            print(" ")
    print()
    print()
    while f :
        f=False
        
        for j in range (n-i-1) :
            	
            if(a[j]>a[j+1]) :

                a[j],a[j+1]=a[j+1],a[j]
                f=True
			
			
            	
            for o in range(n) :
                print(a[o],end = " ")
                if o==n/2-1:
                    print(" ")
            print()
            print()
			
		
        i+=1
		  
matrix=[[0,3,4],
        [1,0,2]

    ]
N=2
M=3
bubble_sort2d(matrix,N,M)
