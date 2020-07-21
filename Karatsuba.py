def multiply(X,Y):
    n1=len(X)
    n2=len(Y)
    if(n1==1 or n2==1):
        return int(X)*int(Y)

    maxl=max(n1,n2)
    while(len(X)<maxl):
        X='0'+X
    while(len(Y)<maxl):
        Y='0'+Y



    print('numbers after padding')
    print(X)
    print(Y)
    a=X[0:int(len(X)/2)]
    b=X[int(len(X)/2):]
    c=Y[0:int(len(Y)/2)]
    d=Y[int(len(Y)/2):]
    nby2=len(b)
    n=nby2*2
    print('a',a)
    print('b',b)
    print('c',c)
    print('d',d)
    ac=multiply(a,c)
    print('ac',ac)

    bd=multiply(b,d)
    print('bd',bd)
    aplusb=int(a)+int(b)
    cplusd=int(c)+int(d)
    print('(a+b)',aplusb)
    print('(c+d)',cplusd)
    AplusBTimeCPlusD=multiply(str(aplusb),str(cplusd))
    print('(a+b)(c+d)',AplusBTimeCPlusD)
    diff=AplusBTimeCPlusD-ac-bd
    print('3-2-1',diff)
    first=pow(10,n)*ac
    second=pow(10,nby2)*diff
    print(first)
    print(second)
    sum=first + bd+ second
    print('returning',sum)
    return sum


n=multiply('3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627')
print(n)
