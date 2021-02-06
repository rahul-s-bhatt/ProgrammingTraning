# https://www.codechef.com/LRNDSA02/problems/NOTALLFL
for _ in range(int(input())):
    n ,k = map(int,input().split())
    A = list(map(int,input().split()))
    queue = []
    count = k
    length = []
    memory = {i:0 for i in range(1,k+1)}
    for i in A:
        if memory[i] == 0:
            count -= 1
        queue.append(i)
        memory[i] += 1
        if count == 0:
            length.append(len(queue) -1) 
            while count == 0:
                x = queue.pop(0)
                memory[x] -= 1
                if memory[x] == 0:
                    count += 1
    length.append(len(queue))
    print(max(length))
    

