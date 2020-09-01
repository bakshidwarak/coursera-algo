import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

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
    if(vertex in visited_set):
        return
    visited_set.add(vertex)
    for element in input_dict[vertex]:
        if element not in visited_set:
            dfs(input_dict,element,visited_set,ordering_stack)
    ordering_stack.append(vertex)

def main():
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
    graph_reversed=reverseGraph(input)
    for vertex in input:
        if(vertex not in visited):
            dfs(graph_reversed,vertex,visited,ordering)
    visited.clear()
   
    #print("ordering",ordering)
    #print("reversed",graph_reversed)
    result=list()
    visited=set()
    processed=set()
    while ordering:
        current=list()
        curr_vertex=ordering.pop()
        if(curr_vertex not in processed):
            processed.add(curr_vertex)
            if (curr_vertex not in visited):
                 dfs(input,curr_vertex,visited,current)
                 result.append(current)

    #print(result)
    sizes=list()
    for e in result:
        sizes.append(len(e))

    sizes.sort(reverse = True)
    print(sizes[:5])

thread = threading.Thread(target=main)
thread.start()