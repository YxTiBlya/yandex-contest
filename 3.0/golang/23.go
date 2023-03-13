package main

import "fmt"

var N int
var dp, prev []int

func rewrite(j, i int) {
	if j <= N {
		if prev[j] != -1 {
			if dp[i]+1 <= dp[j] {
				dp[j] = dp[i] + 1
				prev[j] = i
			}
		} else {
			dp[j] = dp[i] + 1
			prev[j] = i
		}
	}
}

func main() {
	fmt.Scanln(&N)
	dp = make([]int, N+1)
	prev = make([]int, N+1)
	for i := range prev {
		prev[i] = -1
	}

	for i := 1; i < N; i++ {
		rewrite(i*3, i)
		rewrite(i*2, i)
		rewrite(i+1, i)
	}
	var ansnums []int
	for i := N; i >= 1; i = prev[i] {
		ansnums = append(ansnums, i)
	}

	fmt.Println(dp[N])
	for i := len(ansnums) - 1; i >= 0; i-- {
		fmt.Print(ansnums[i], " ")
	}
}
