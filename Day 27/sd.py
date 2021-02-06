# table = [[0 for i in range(k+1)]for i in range(n+1)]
    # # s1.append(arr[n-1])

    # for i in range(n+1):
    #     for j in range(k+1):
    #         if i == 0 or j == 0:
    #             table[i][j] = 0
    #         elif arr[i-1] <= k:
    #             table[i][j] = max(arr[i-1]+table[i-1][k-arr[i-1]], table[i-1][j])
    #         else:
    #             table[i][j] = table[i-1][j]

    # return table[n][k]