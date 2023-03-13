package main

import (
	"fmt"
	"math"
)

func main() {
	var N, M int
	fmt.Scanf("%d %d\n", &N, &M)

	dp := make([][]int, N+1)
	for i := 0; i < M+1; i++ {
		dp[0] = append(dp[0], math.MaxInt)
	}
	dp[0][1] = 0

	var x int
	for i := 1; i < N+1; i++ {
		row := make([]int, M+1)
		row[0] = math.MaxInt
		for j := 1; j < M+1; j++ {
			fmt.Scan(&x)
			row[j] = x
		}

		for j := 1; j < M+1; j++ {
			row[j] += int(math.Min(float64(dp[i-1][j]), float64(row[j-1])))
		}
		dp[i] = row
	}
	fmt.Println(dp[len(dp)-1][M])
}
