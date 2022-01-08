# cook your dish here
try:
    for i in range(int(input())):
        row=0
        seat=0
        p=list(map(int, input().split()))
        if(p[0]%2==0):
            row=p[0]/2
            if(p[1]%2==0):
                seat=p[1]/2
            else:
                seat=(p[1]+1)/2
        else:
            row=(p[0]+1)/2
            if(p[1]%2==0):
                seat=p[1]/2
            else:
                seat=(p[1]+1)/2
        
        print(int(row*seat))
except EOFError as e:
    pass
           