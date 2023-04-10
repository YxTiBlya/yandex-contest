package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var N, M int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanf(in, "%d %d\n", &N, &M)

	dp := make([][]int, N+1)
	dp[0] = make([]int, M+1)
	prev := make([][]rune, N+1)

	var x int
	for i := 1; i < N+1; i++ {
		row := make([]int, M+1)
		prev[i] = append(prev[i], '0')

		for j := 1; j < M+1; j++ {
			fmt.Fscan(in, &x)

			if dp[i-1][j] >= row[j-1] {
				row[j] = x + dp[i-1][j]
				prev[i] = append(prev[i], 'D')
			} else {
				row[j] = x + row[j-1]
				prev[i] = append(prev[i], 'R')
			}
		}

		dp[i] = row
	}

	i, j := N, M
	var cert []rune
	for prev[i] != nil {
		cert = append(cert, prev[i][j])

		if prev[i][j] == 'D' {
			i--
		} else {
			j--
		}
	}

	fmt.Println(dp[N][M])
	for i := len(cert) - 2; i >= 0; i-- {
		fmt.Print(string(cert[i]), " ")
	}
}
