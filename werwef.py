
from math import ceil
from math import log2
def sift_up(heap, i):
    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        heap[i], heap[(i - 1)// 2] = heap[(i - 1) // 2], heap[i]
        i=(i-1) //2
def add(heap,x):
    heap.append(x)
    sift_up(heap,len(heap)-1)




def sift_down(heap, i):
    n = len(heap)
    while (i*2+1)<n:
        left=2*i+1
        right=2*i+2
        j=left
        if right<n and heap[right]>heap[left]:
            j=right
        if heap[i]>=heap[j]:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i=j
def extract_min(heap):
    x = heap[0]
    heap[0] = heap. pop()
    sift_down(heap, 0)
    return x
def build_heap(heap) :
    n=len(heap)
    for i in range(ceil(n/ 2), -1, -1):
        sift_down(heap, i)
        

def pretty_print (heap):
    height = int (log2(len(heap)))
    node_width = len(str(max (heap) ))
    str_width = (2 ** (height + 1) - 1) * node_width
    interval = node_width
    result = []
    for i in range(height, -1, -1):
        start = 2 ** i- 1
        nums_in_line = 2 ** i
        args = heap[start:start + nums_in_line]
        line = (" " * interval).join(["{:" + "{}".format(node_width) + "}"] *min(nums_in_line, len(args))).format (*args)
        if i != height:
            line =" " * ((str_width - len(line)) // 2) + line
        result .append(line)
        interval = interval * 2 + node_width
    print ("\n". join(reversed(result)))

def heapsort(heap):
    n=len(heap)
    for i in range(n):
        print("heap[:n-i]",heap[:n-i])
        for l in range(ceil((n-i)/ 2), -1, -1):
            
            
            while (l*2+1)<n-i:
                left=2*l+1
                right=2*l+2
                j=left
                if right<n-i and heap[right]>heap[left]:
                    j=right
                if heap[l]>=heap[j]:
                    break
                heap[l], heap[j] = heap[j], heap[l]
                l=j
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",heap)
        pretty_print(heap[:(n-i)])
        print("heap[n-i-1]",heap[n-i-1])
        heap[n-i-1],heap[0]=heap[0],heap[n-i-1]
        print("heap end",heap)
        print("#########heap otv",heap[n-i-3::-1],heap[n-i-2:n:1])


        print("     ")

n=int(input())

heap=input().split()
for i in range (len(heap)):
    heap[i]=int(heap[i])




build_heap(heap)
print(heap)
print(heapsort(heap))
