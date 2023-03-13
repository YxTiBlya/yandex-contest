package main

import "fmt"

func main() {
	var N, M int
	fmt.Scanf("%d %d\n", &N, &M)

	dp := make([][]int, N)
	for i := range dp {
		dp[i] = make([]int, M)
	}
	dp[0][0] = 1

	for i := 0; i < N-1; i++ {
		for j := 0; j < M-1; j++ {
			if i == 0 && j == 0 || dp[i][j] != 0 {
				if i+2 < N && j+1 < M {
					dp[i+2][j+1] += dp[i][j]
				}
				if i+1 < N && j+2 < M {
					dp[i+1][j+2] += dp[i][j]
				}
			}
		}
	}

	fmt.Println(dp[N-1][M-1])
}
