try:
    n=int(input())
    sum=0
    if(sum<10**6):
        if(n>=1 and n<=10**4):
            for i in range(n):
                p=int(input())
                sum+=p
                l=[]
                flag=0
                if(p>=1 and p<=10**6):
                    for j in range(2):
                        q=list(input())
                        l.append(q)
                    for x in range(p):
                        if(l[0][x]<l[1][x]):
                            flag+=1
                    print(flag)                
except EOFError as e:
    pass