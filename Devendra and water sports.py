try:
    for i in range(int(input())):
        p=list(map(int, input().split()))
        if((p[0]-p[1])-(p[2]+p[3]+p[4])>=0):
            print("YES")
        else:
            print("NO")
except EOFError as e:
    pass
           