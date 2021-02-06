t = int(input())
for i in range(t):
    n = int(input())
    exp = input().strip()
    prec = {}
    prec["^"] = 3
    prec["*"] = 2
    prec["/"] = 2
    prec["+"] = 1
    prec["-"] = 1

    opS = []
    postF = []
    
    for op in exp:
        if op.isalnum():
            postF.append(op)

        elif op == '(':
            opS.append(op)

        elif op == ')':
            top = opS.pop()

            while top != '(':
                postF.append(top)
                top = opS.pop()

        else:
            while (len(opS) > 0 and opS[-1] != '(' and (prec[opS[-1]] >= prec[op])):
                postF.append(opS.pop())

            opS.append(op)

    while len(opS) > 0:
        postF.append(opS.pop())

    s = "".join(postF)
    print(s)
