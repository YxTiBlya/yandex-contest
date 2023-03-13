N, M, K = map(int, input().split())
arr = []
prefix_arr = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    nums = [0] + list(map(int, input().split()))
    for j in range(1, M+1):
        prefix_arr[i][j] = prefix_arr[i][j-1] + prefix_arr[i-1][j] - prefix_arr[i-1][j-1] + nums[j]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    res = prefix_arr[x2][y2] - prefix_arr[x1-1][y2] - prefix_arr[x2][y1-1] + prefix_arr[x1-1][y1-1]
    print(res)