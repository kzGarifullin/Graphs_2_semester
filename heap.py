from math import ceil
from math import log2
def sift_up(heap, i):
    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        heap[i], heap[(i - 1)// 2] = heap[(i - 1) // 2], heap[i]
        i=(i-1) //2
def add(heap,x):
    heap.append(x)
    sift_up(heap,len(heap)-1)


def build_heap(heap) :
    for i in range(ceil(len(heap) / 2), -1, -1):
        sift_down(heap, i)


def sift_down(heap, i):
    n = len(heap)
    while i*2+1<n:
        j=i
        if heap[i] > heap[i * 2 + 1]:
            j=i*2+1
        if i * 2 + 2 <n and heap[j] > heap[i * 2 + 2]:
            j=i*2+2
        if i == j:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i=j
def extract_min(heap):
    x = heap[0]
    heap[0] = heap. pop()
    sift_down(heap, 0)
    return x

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


heap = []
while True:
    cmd = input().strip()
    if cmd.find(' ') != -1:
        cmd, v = cmd.split()
        v = int(v)

     

    if cmd == "exit":
        break
    elif cmd == "add":
        add(heap, v)
    elif cmd == "min":
        print (extract_min(heap) )
    elif cmd == "print":
        pretty_print (heap)
    else:

        print("incorrect command")



