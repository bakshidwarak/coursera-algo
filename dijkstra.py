
def getMinimum(heapmap_dict):
    min=100000
    minkey=0
    for key in heapmap_dict.keys():
        if(heapmap_dict[key]< min):
            minkey=key
            min=heapmap_dict[key]
    return minkey


input=dict()
file=open('dijkstra.txt')
for line in file:
    curr=line.strip()
    eles=curr.split()
    edges=list()
    for edge in eles[1:]:
        e=edge.strip()
        edgetuple=e.split(',')
        edges.append((int(edgetuple[0]),int(edgetuple[1])))
    input[int(eles[0])]=edges

heapmap=dict()
distances=dict()
distances[1]=0
heapmap[1]=0
for key in input.keys():
    if key > 1:
        heapmap[key]=100000



while len(heapmap)>0:
    current=getMinimum(heapmap)
    neighbours=input[current]
    for v,l in neighbours:
        distance=distances[current]+l
        if v in heapmap.keys():
            if(heapmap[v]>distance):
                heapmap[v]=distance
                distances[v]=distance
    heapmap.pop(current,None)


print(distances[7],distances[37],distances[59],distances[82],distances[99],distances[115],distances[133],distances[165],distances[188],distances[197])


