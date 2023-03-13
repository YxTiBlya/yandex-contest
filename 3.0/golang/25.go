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
	g := make([]int, N)
	for i := range g {
		fmt.Scan(&x)
		g[i] = x
	}
	sort.Ints(g)

	dp := make([]int, N+1)
	dp[2] = g[1] - g[0]

	if N > 2 {
		dp[3] = g[2] - g[0]
		for i := 4; i < N+1; i++ {
			dp[i] = int(math.Min(float64(dp[i-1]), float64(dp[i-2]))) + g[i-1] - g[i-2]
		}
	}

	fmt.Println(dp[N])
}
