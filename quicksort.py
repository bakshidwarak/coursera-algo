def quickSort(input,start,end):
    if(start >= end):
        return 0
    pivot_index=getPivot(input,start,end)
    print(pivot_index, input[pivot_index])
    swap(input,pivot_index,start)
    pindex=partition(input,start,end)
    count=end- start
    leftcount=quickSort(input,start,pindex-1)
    rightcount=quickSort(input,pindex+1,end)
    return count+leftcount+rightcount

def getPivot(input,start,end):
    mid=int((start+end+1)/2)
    if((end-start+1)%2==0):
        return median(input,start,end,mid-1)
    else:
        return median(input,start,end,mid)

def median(input,start,end,mid):
    arr=[input[start],input[mid],input[end]]
    arr.sort()
    if(arr[1]==input[start]):
        return start
    if(arr[1]==input[mid]):
        return mid
    return end

    #return end

def partition(input,start,end):
    pval=input[start]
    i=start+1
    j=start+1
    while( j <= end):
        if(input[j]<pval):
            swap(input,j,i)
            i=i+1
        j=j+1
    swap(input,start,i-1)
    return i-1


def swap(input,i,j):
    temp=input[i]
    input[i]=input[j]
    input[j]=temp

input=list()
file=open('qsinput.txt')
for line in file:
    input.append(int(line.strip()))

#input=[2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
cnts=quickSort(input,0,len(input)-1)
print(input)
print(cnts)
