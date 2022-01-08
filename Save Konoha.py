try:
    n=int(input())
    for i in range(n):
        p=list(map(int, input().split()))
    for k in range(p[0]):
        q=list(map(int, input().split()))

except EOFError as e:
    pass
