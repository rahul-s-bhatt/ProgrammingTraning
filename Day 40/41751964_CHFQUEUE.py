# cook your dish here
n,k=map(int,input().split())
chefs=list(map(int,input().split()))
f=1
stack=[]
chefs=chefs[::-1]
for i in range(n):
    if(len(stack)==0):
        stack.append([chefs[i],i])
    else:
        while(len(stack)>0 and stack[-1][0]>=chefs[i]):
            stack.pop()
        if(len(stack)==0):
            f*=1
        else:
            f*=(i-stack[-1][1]+1)
            f=f%(10**9+7)
    stack.append([chefs[i],i])

print(f)