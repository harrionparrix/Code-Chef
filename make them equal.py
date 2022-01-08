try:
    sum=0
    n=int(input())
    if(n>=1 and n<=10**4):
        for i in range(n):
            q=[]
        s=int(input())
        p=list(map(int, input().split()))
        for k in range(len(p)):
            sum+= p[k]
            q.append(int(p[k]))
        m=max(q)
        n=min(q)
        print(m-n) 
except EOFError as e:
    pass