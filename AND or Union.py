try:
    for k in range(int(input())):
        p=int(input())
        l=list(map(int,input().split()))
        bit=0
        c=[]
        for i in range(p):
            for j in range(i+1,p):
                bit=l[i]&l[j]
                c.append(bit)
            if(len(c)==1):
                break
            else:
                continue
        print(*c)
except EOFError as e:
    pass

