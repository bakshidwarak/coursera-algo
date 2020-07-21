def mergeAndCount(input):
    n=len(input)
    if n==1:
        return input,0
    left,leftcount = mergeAndCount(input[0:int(n/2)])
    right,rightcount= mergeAndCount(input[int(n/2):])
    merged,splitcount=mergeCount(left,right)
    return merged,leftcount+rightcount+splitcount

def mergeCount(left,right):
    n1=len(left)
    n2=len(right)
    result=list()
    i=0
    j=0
    k=0
    splitcount=0
    print(left)
    print(right)
    while( k< n1+n2):
        print(k)
        while ( i<n1 and j<n2 and left[i]<=right[j]):
            result.append(left[i])
            i=i+1
        while (j<n2 and i<n1 and right[j]<left[i]):
            result.append(right[j])
            j=j+1
            splitcount=splitcount+n1-i
        k=k+1
    while (i<n1):
            result.append(left[i])
            i=i+1
            k=k+1
    while(j<n2):
            result.append(right[j])
            j=j+1
            k=k+1


    return result,splitcount
input=list()
file=open('inversioninput.txt')
for line in file:
    input.append(int(line.strip()))

op,count=mergeAndCount(input)
print("input")
print(input)
print("final")
print(op)
print("cnt")
print(count)
