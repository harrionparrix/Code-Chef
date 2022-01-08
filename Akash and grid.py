# cook your dish here
try:
    for i in range(int(input())):
        x=0
        p=list(map(int, input().split()))
        x=(p[0]+1)/2
        if(p[1]%2==1 and p[2]%2==1):
            print(0)
        else:
            if(p[1]%2==0 and p[2]%2==0):
                print(0)
            else:
                print(1)
except EOFError as e:
    pass