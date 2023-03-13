package main

import "fmt"

func main() {
	var M, N int
	fmt.Scanln(&M)
	fmt.Scanln(&N)
	var os [][]int

	for i := 0; i < N; i++ {
		var a, b int
		fmt.Scanf("%v %v\n", &a, &b)

		for j := len(os) - 1; j >= 0; j-- {
			if os[j][1] >= a && os[j][0] <= a || os[j][0] <= b && os[j][1] >= b || os[j][0] >= a && os[j][1] <= b {
				copy(os[j:], os[j+1:])
				os = os[:len(os)-1]
			}
		}

		os = append(os, []int{a, b})
	}

	fmt.Println(len(os))
}
