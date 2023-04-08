package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	var N int
	fmt.Scanln(&N)

	var x int
	nums := make([]int, N)
	for i := range nums {
		fmt.Scan(&x)
		nums[i] = x
	}
	sort.Ints(nums)

	dp := make([]int, N+1)
	dp[2] = nums[1] - nums[0]

	if N > 2 {
		dp[3] = nums[2] - nums[0]
		for i := 4; i < N+1; i++ {
			dp[i] = int(math.Min(float64(dp[i-1]), float64(dp[i-2]))) + nums[i-1] - nums[i-2]
		}
	}

	fmt.Println(dp[N])
}
