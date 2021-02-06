# cook your dish here
t=int(input())
a=list(map(int,input().split()))
s=0
posi=0
pos1=0
end=0
first=0
pos=0
p=0
b=0
tot=0
stack=[]
for i in a:
    posi+=1
    if i==1:
        stack.append(i)
        s+=1
        b+=1
        if s>tot:
            tot=s
            pos1=posi
        if s==1:
            p=posi
    else:
        stack.pop()
        s-=1
        b+=1
        if s==0:
            if b>end:
                end=b
                pos=p
            b=0
print(tot,pos1,end, pos)