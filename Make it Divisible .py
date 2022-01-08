import math

try:
    n = int(input())
    for i in range(1,n+1):
        A = []
        q = []
        sum = 0
        flag1 = 0
        flag2 = 0

        s = int(input())

        # if(sum <= 2*(10**5)):
        # if(s >= 2 and s <= 10**5):
        p = list(map(int, input().split()))
        # print(p)
        # p = list(input().split())
        for k in range(len(p)):
            sum += p[k]
            q.append(int(p[k]))
        if(sum % 3 != 0):
            print(-1)
        else:
            for o in range(0, len(q)):
                # if(q[o] >= 1 and q[o] <= 10**9):
                if(q[o] % 3 == 1):
                    flag1 += 1
                if(q[o] % 3 == 2):
                    flag2 += 1
            if(flag1 == flag2):
                print(flag1)
            else:
                if flag1 > flag2:
                    ans = flag2
                    ans += ((flag1-flag2)//3)*2
                    print(ans)
                else:
                    ans = flag1
                    ans += ((flag2-flag1)//3)*2
                    print(ans)
                # elif(flag1 != flag2):
                    # if(flag1 == 0 and flag2 == 0):
                    #     print("0")
                    # else:
                #     print("-1")
except EOFError as e:
    pass