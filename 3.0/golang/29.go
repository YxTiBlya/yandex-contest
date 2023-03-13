package main

import (
	"fmt"
	"math"
)

var max int = 30100

func main() {
	var N int
	var num int
	fmt.Scanln(&N)

	if N == 0 {
		fmt.Println(0)
		fmt.Println(0, 0)
	} else if N == 1 {
		fmt.Scanln(&num)
		fmt.Println(num)
		if num > 100 {
			fmt.Println(1, 0)
		} else {
			fmt.Println(0, 0)
		}
	} else {
		a := make([]int, N)
		for i := 0; i < N; i++ {
			fmt.Scanln(&num)
			a[i] = num
		}

		dp := make([][]int, N)
		for i := 0; i < N; i++ {
			for j := 0; j < N+2; j++ {
				dp[i] = append(dp[i], max)
			}
		}

		if a[0] > 100 {
			dp[0][2] = a[0]
		} else {
			dp[0][1] = a[0]
		}

		for i := 1; i < N; i++ {
			for j := 1; j < N; j++ {
				if a[i] > 100 {
					dp[i][j] = int(math.Min(float64(dp[i-1][j-1]+a[i]), float64(dp[i-1][j+1])))
				} else {
					dp[i][j] = int(math.Min(float64(dp[i-1][j]+a[i]), float64(dp[i-1][j+1])))
				}
			}
		}

		ans := max
		k1, k2 := 0, 0
		for j := 0; j < N; j++ {
			if dp[N-1][j] <= ans {
				ans = dp[N-1][j]
				k1 = j
			}
		}
		var days []int
		tmp := k1
		for i := N - 1; i > 0; i-- {
			if dp[i][tmp] == dp[i-1][tmp+1] {
				k2++
				days = append(days, i+1)
				tmp++
			} else if dp[i][tmp] == dp[i-1][tmp]+a[i] {

			} else if dp[i][tmp] == dp[i-1][tmp-1]+a[i] {
				tmp--
			}
		}

		fmt.Println(ans)
		fmt.Println(k1-1, k2)
		for i := len(days) - 1; i >= 0; i-- {
			fmt.Print(days[i], " ")
		}
	}
}
