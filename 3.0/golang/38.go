package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var N, M, S, T, Q int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanf(in, "%d %d %d %d %d\n", &N, &M, &S, &T, &Q)
	S, T = S-1, T-1

	field := make([][]int, N)
	for i := range field {
		for j := 0; j < M; j++ {
			field[i] = append(field[i], -1)
		}
	}
	field[S][T] = 0
	res := make(map[int][][]int)
	res[0] = [][]int{{T, S}}

	dx := []int{-2, -2, -1, -1, 1, 1, 2, 2}
	dy := []int{1, -1, 2, -2, 2, -2, 1, -1}

	for i := 1; i < N*M; i++ {
		res[i] = [][]int{}
		for _, coords := range res[i-1] {
			for delta := 0; delta < 8; delta++ {
				x := coords[0] + dx[delta]
				y := coords[1] + dy[delta]
				if 0 <= x && x < M && 0 <= y && y < N {
					if field[y][x] == -1 {
						field[y][x] = i
						res[i] = append(res[i], []int{x, y})
					}
				}
			}
		}
	}

	ans := 0
	var y, x int
	for i := 0; i < Q; i++ {
		fmt.Fscanf(in, "%d %d\n", &y, &x)
		x--
		y--
		if field[y][x] == -1 {
			ans = -1
			break
		}
		ans += field[y][x]
	}
	fmt.Println(ans)
}
