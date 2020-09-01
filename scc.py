
def reverseGraph(graph_dict):
    reversed=dict()
    for vertex in graph_dict:
        reversed[vertex]=list()
    for vertex in graph_dict:
        current=graph_dict[vertex]
        for v in current:
            reversed[v].append(vertex)
    return reversed

def dfsrecursive(input_dict,start,visited,ordering):
    if not start or start in visited:
        return
    stack=list()
    temp=list()
    stack.append(start)
    temp.append(start)
    while(stack):
        vertex=stack.pop()
        #print(vertex)
        if(vertex not in visited):
            visited.add(vertex)
            for element in input_dict[vertex]:
                if element and element not in visited:
                    stack.append(element)
                    temp.append(element)
    #print(temp)
    temp.reverse()
    ordering.extend(temp)        
    
            

def dfs(input_dict,vertex,visited_set,ordering_stack):
    if(vertex in visited):
        return
    visited.add(vertex)
    for element in input_dict[vertex]:
        if element not in visited:
            dfs(input_dict,element,visited_set,ordering_stack)
    ordering_stack.append(vertex)

input=dict()
file=open('scc.txt')
for line in file:
    curr=line.strip()
    eles=curr.split()
    input.setdefault(int(eles[0]),[])
    input[int(eles[0])].append(int(eles[1]))
    if int(eles[1]) not in input:
        input.setdefault(int(eles[1]),[])

#print(input)
visited=set()
ordering=[]
for vertex in input:
    if(vertex not in visited):
        dfsrecursive(input,vertex,visited,ordering)
visited.clear()
graph_reversed=reverseGraph(input)
#print("ordering",ordering)
#print("reversed",graph_reversed)
result=list()
visited=set()

while ordering:
    current=list()
    curr_vertex=ordering.pop()
    if (curr_vertex not in visited):
        dfsrecursive(graph_reversed,curr_vertex,visited,current)
    result.append(current)

#print(result)
sizes=list()
for e in result:
    sizes.append(len(e))

sizes.sort(reverse = True)
print(sizes[:5])
