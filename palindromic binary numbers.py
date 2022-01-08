# cook your dish here
try:
    sum=0
    n=int(input())
    if(n>=1 and n<=10**4):
        for i in range(n):
            p=int(input())
            p1=p
            m=12
            l=[]
            if(p>=1 and p<=1000):
                while(m>=1 and m<=12):
                    num=int("{0:b}".format(p1))
                    temp=num
                    print(num)
                    rev=0
                    while(num>0):
                        dig=num%10
                        rev=rev*10+dig
                        n=n//10
                    if(temp==rev):
                        l.append(p1)
                        p-=p1
                        m-=1
                    p1-=1
                    print(l)
 
except EOFError as e:
    pass