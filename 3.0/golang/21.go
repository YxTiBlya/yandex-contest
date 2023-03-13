package main

import "fmt"

func function(x int) int {
	res := map[int]int{1: 2, 2: 4, 3: 7}
	if _, ok := res[x]; ok {
		return res[x]
	}
	for i := 4; i < x+1; i++ {
		res[i] = res[i-1] + res[i-2] + res[i-3]
	}
	return res[x]
}

func main() {
	var N int
	fmt.Scanln(&N)
	fmt.Println(function(N))
}
