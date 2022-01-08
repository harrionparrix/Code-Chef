try:
    n=int(input())
    if(n>=1 and n<=10**4):
        for i in range(n):
            days=0
            p,q=list(map(int, input().strip().split()))
            if(p>=1 and p<=100 and q>=1 and q<=100):
                if(p%q==0):
                    days=p/q
                else:
                    days=p//q
                    days+=1
            print(days)
except EOFError as e:
    pass