package main

import "fmt"

func main() {
	var N, K int
	fmt.Scanf("%d %d", &N, &K)

	dp := make([]int, N)
	for i := range dp {
		dp[i] = -1
	}
	dp[0] = 1

	for i := 1; i < N; i++ {
		c := 0

		if i >= K {
			for j := i - K; j < i; j++ {
				c += dp[j]
			}
		} else {
			for j := 0; j < i; j++ {
				c += dp[j]
			}
		}
		dp[i] = c
	}
	fmt.Println(dp[N-1])
}
