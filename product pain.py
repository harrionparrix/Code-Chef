t=int(input())
if(t>=1 and t<=1000):
    for i in range(t):
        n=int(input())
        q=[]
        sum=0
        if(n>=3 and n<=3000):
            p=list(input().split())
            for k in range(len(p)):
                q.append(int(p[k]))
                for o in range(n):
                    if(q[o]>=1 and q[o]<=10**6):
                        for a in range(0,n//2):
                            for c in range((n//2)+1,n):
                                for b in range(a+1,c):
                                    sum+=(q[a]-q[b])*(q[b]-q[c])
                print(sum) 