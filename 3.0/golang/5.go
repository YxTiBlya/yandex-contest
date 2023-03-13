package main

import "fmt"

func main() {
	slc := input()
	ans := 0

	for i := 0; i < len(slc)-1; i++ {
		if slc[i] <= slc[i+1] {
			ans += slc[i]
		} else {
			ans += slc[i+1]
		}
	}

	fmt.Println(ans)
}

func input() []int {
	var N int
	fmt.Scanln(&N)

	slc := make([]int, N)
	for i := 0; i < N; i++ {
		var num int
		fmt.Scanln(&num)
		slc[i] = num
	}

	return slc
}
