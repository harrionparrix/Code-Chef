try:
    for i in range(int(input())):
        maxi=0
        m=int(input())
        for j in range(m):
            p=list(map(int, input().split()))
            l=int(p[1]/(p[0]+1))
            if(l>=0):
                temp=int(p[2]*l)
            if(temp>=maxi):
                maxi=temp
        print(maxi)
except EOFError as e:
    pass
           