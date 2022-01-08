import math


for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    result=min((b-a)%math.gcd(c,d),(a-b)%math.gcd(c,d))
    print(result)