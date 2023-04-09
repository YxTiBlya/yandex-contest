package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var N, M, x int
	in := bufio.NewReader(os.Stdin)

	fmt.Fscanln(in, &N)
	np := make([]int, N+1)
	for i := 1; i < N+1; i++ {
		fmt.Fscan(in, &x)
		np[i] = x
	}
	fmt.Fscanln(in)

	fmt.Fscanln(in, &M)
	mp := make([]int, M+1)
	for i := 1; i < M+1; i++ {
		fmt.Fscan(in, &x)
		mp[i] = x
	}

	dp := make([][]int, N+1)
	for i := range dp {
		dp[i] = make([]int, M+1)
	}

	for i := 1; i < N+1; i++ {
		for j := 1; j < M+1; j++ {
			if np[i] == mp[j] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = int(math.Max(float64(dp[i-1][j]), float64(dp[i][j-1])))
			}
		}
	}

	var cert []int
	i, j := N, M
	for dp[i][j] != 0 {
		if dp[i][j-1] == dp[i][j] {
			j--
		} else if dp[i-1][j] == dp[i][j] {
			i--
		} else {
			cert = append(cert, np[i])
			i--
			j--
		}
	}

	for i := len(cert) - 1; i >= 0; i-- {
		fmt.Print(cert[i], " ")
	}
}
