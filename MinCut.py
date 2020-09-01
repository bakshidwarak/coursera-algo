import random

def countInAList(inputlist,element):
    count=0
    for item in inputlist:
        if(item==element):
            count=count+1
    return count

def combine(input,a,b):
    if(a==b):
        return input
    #print("fusing vertex",a,"and",b)
    #print(input)
    #get edges of b
    second=input[b]
    first= input[a]

    #replace one occurance of b in a with b's list and delete the others
    for item in list(first):
        if(item==b):
            first.extend(second)
            break
    input[a]= list(filter((b).__ne__, first))

    # replace b with a in other vertices' edges
    vertices=input.keys()
    for item in list(vertices):
        if( item !=a):
            currentlist=input[item]
            for ele in list(currentlist):
                if(ele==b):
                    currentlist.append(a)
            input[item]=list(filter((b).__ne__, currentlist))

    # remove self edges
    for item in vertices:
        currentlist=input[item]
        for ele in list(currentlist):
            if(ele==item):
                currentlist.remove(item)


    #delete b
    input.pop(b,None)
    #print(" After fusing")
    #print(input)
    return input


def mincut(input):
    #print(input)
    #print("===========")
    #print(len(input))
    if(len(input)==2):
        return len(next(iter(input.values())))

    ans=len(input)
    vertices=list(set(input.keys()))

    #for u in vertices:
    #    print("processing vertex",u)
    #    for v in input[u]:
    #        print("(",u,v,")")
    #        if(u!=v):
    #            print(input)
    #            print("Merging vertices",u,v)
    #            nextgraph=combine(input.copy(),u,v)
    #            print(nextgraph)
    #            if(len(nextgraph)>2):
    #                newcut=mincut(nextgraph.copy())
    #                ans=min(ans,newcut)
    #return ans




    #pick an vertex from current graph
    randomnumber=random.randint(0,len(vertices)-1)
    vertex1=vertices[randomnumber]

    randomnumber=random.randint(0,len(input[vertex1])-1)
    vertex2=input[vertex1][randomnumber]

    nextgraph=combine(input,vertex1,vertex2)
    return mincut(nextgraph)

input=dict()
file=open('mincutinput.txt')
for line in file:
    curr=line.strip()
    eles=curr.split()
    input[int(eles[0])]=list(int(num) for num in eles[1:])

minval=len(input)
for item in range(1,50):
    print(item)
    val=mincut(dict(input))
    minval=min(minval,val)

print("Minimum cuts from 10 rounds is",minval)
