N = int(input())

nums = [i for i in range(N+1)]
dp = [0] * (N + 1)
prev = [-1] * (N + 1)

def rewrite(j, i):
    if j <= N:       
        if prev[j] != -1:  
            if dp[i] + 1 <= dp[j]: 
                dp[j] = dp[i] + 1
                prev[j] = nums[i]
        else:                  
            dp[j] = dp[i] + 1   
            prev[j] = nums[i]

for i in range(1, N):
    rewrite(i*3, i)
    rewrite(i*2, i)
    rewrite(i+1, i)

ansnums = []
i = N  
while i >= 1:                
    ansnums.append(nums[i])
    i = prev[i] 

print(dp[N])
print(*reversed(ansnums))