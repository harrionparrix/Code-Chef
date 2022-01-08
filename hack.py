
try:
    n=int(input())
    if(n>=1 and n<=10**4):
        q=[]
        for i in range(n):
            p=list(map(int, input().split()))
        for k in range(len(p)):
            z=int(p[k])
            if(z>=1 and z<=10**6):
                q.append(z)
except EOFError as e:
    pass

n=int(input())
if(n>=1 and n<=1000):
    for i in range(n):
        p,q=list(map(int, input().strip().split()))

l=[]
print(*l)

try:
    for i in range(int(input())):
        p=list(map(int,input().split()))
    
           
except EOFError as e:
    pass