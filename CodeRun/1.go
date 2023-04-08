package main

import "fmt"

func main() {
	var N int
	fmt.Scanln(&N)

	dp := make([]int, N+3)
	nums := make([][]int, N+3)
	for i := range nums {
		nums[i] = []int{0, 0, 0}
	}

	var a, b, c int
	for i := 3; i < N+3; i++ {
		fmt.Scanf("%d %d %d\n", &a, &b, &c)

		mn := dp[i-1] + a
		if dp[i-2]+nums[i-1][1] != 0 && dp[i-2]+nums[i-1][1] < mn {
			mn = dp[i-2] + nums[i-1][1]
		}
		if dp[i-3]+nums[i-2][2] != 0 && dp[i-3]+nums[i-2][2] < mn {
			mn = dp[i-3] + nums[i-2][2]
		}

		dp[i] = mn
		nums[i] = []int{a, b, c}
	}

	fmt.Println(dp[N+2])
}
