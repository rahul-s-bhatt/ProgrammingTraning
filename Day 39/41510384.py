t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    flvr_lst = list(map(int, input().split()))
    flvr_cnt_dict = {i: 0 for i in range(1, k+1)}
    types_enctrd = 0
    max_sub_len = [0]*n
    x = 0
    for i in range(n):
        flvr = flvr_lst[i]
        # Increment the count for that flavour
        flvr_cnt_dict[flvr] += 1
        # Check if it's new type
        if flvr_cnt_dict[flvr] == 1:
            types_enctrd += 1
        # If types encountered exceed all - 1, check index where one type is vanished
        while types_enctrd >= k:
            ex_flvr = flvr_lst[x]
            x += 1
            flvr_cnt_dict[ex_flvr] -= 1
            if flvr_cnt_dict[ex_flvr] == 0:
                types_enctrd -= 1
                break
        max_sub_len[i] = i - x + 1
    print(max(max_sub_len))
