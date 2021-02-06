N=int(input())
h=[list(map(int,input().split())) for _ in range(N)]
dp=[[0 for _ in range(3)] for _ in range(N)]

dp[0]=h[0]

for i in range(1,N):
    dp[i][0]=max(dp[i-1][1], dp[i-1][2]) + h[i][0]
    dp[i][1]=max(dp[i-1][0], dp[i-1][2]) + h[i][1]
    dp[i][2]=max(dp[i-1][0], dp[i-1][1]) + h[i][2]

print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))