package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var n, m, k int
	fmt.Fscanln(in, &n, &m, &k)

	var x int
	prefixMatrix := make([][]int, n+1)
	prefixMatrix[0] = make([]int, m+1)
	for i := 1; i < n+1; i++ {
		prefixMatrix[i] = make([]int, m+1)
		for j := 1; j < m+1; j++ {
			fmt.Fscan(in, &x)
			prefixMatrix[i][j] = prefixMatrix[i][j-1] + prefixMatrix[i-1][j] - prefixMatrix[i-1][j-1] + x
		}
		in.ReadLine()
	}

	var x1, y1, x2, y2 int
	for i := 0; i < k; i++ {
		fmt.Fscanln(in, &x1, &y1, &x2, &y2)
		res := prefixMatrix[x2][y2] - prefixMatrix[x1-1][y2] -
			prefixMatrix[x2][y1-1] + prefixMatrix[x1-1][y1-1]
		fmt.Println(res)
	}
}
