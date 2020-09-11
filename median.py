import heapq

def peekMax(maxheap):
    n=heapq.heappop(maxheap)
    heapq.heappush(maxheap,n)
    return -1*n

def peekMin(minheap):
    n=heapq.heappop(minheap)
    heapq.heappush(minheap,n)
    return n

def addNumber(num,minheap,maxheap):
    if len(maxheap)==0 or num < peekMax(maxheap):
        print("pushing",-1*num,"to maxheap")
        heapq.heappush(maxheap,-1*num)
    else:
        heapq.heappush(minheap,num)
        print("pushing",num,"to minheap")
    

def rebalance(minheap,maxheap):
    if(len(minheap)-len(maxheap)>1):
        n=heapq.heappop(minheap)
        heapq.heappush(maxheap,-1*n)
    elif(len(maxheap)-len(minheap)>1):
        n=heapq.heappop(maxheap)
        heapq.heappush(minheap,-1*n)

def getMedian(minheap,maxheap):
    if(len(minheap)== len(maxheap) or len(minheap)==0):
        return peekMax(maxheap)
    else:
        if(len(maxheap)> len(minheap)):
            return peekMax(maxheap)
        return peekMin(minheap)

file=open("median.txt")
minheap=[]
maxheap=[]
heapq.heapify(minheap)
heapq.heapify(maxheap)
medians=[]
for line in file:
    num=int(line.strip())
    addNumber(num,minheap,maxheap)
    rebalance(minheap,maxheap)
    print('minheap',minheap)
    print('maxheap',maxheap)
    m=getMedian(minheap,maxheap)
    medians.append(m)
    print(m)

print(medians)
print(sum(medians)%10000)
