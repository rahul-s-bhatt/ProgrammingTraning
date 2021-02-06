# cook your dish here
def fun(t):    
    l=0
    max1=0
    for i in range(len(s)):
        if s[i]=='<':
            l+=1
        else:
            l-=1
            if l<0:
                break
        if l==0:
            max1=i+1
    return (max1) 
    

for _ in range(int(input())):
    s=input()
    print(fun(s))
           