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

	board := make([][]int, N)
	for i := range board {
		board[i] = make([]int, M)
	}
	board[0][0] = 1

	dy := []int{1, 2}
	dx := []int{2, 1}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if board[i][j] > 0 {
				for delta := 0; delta < 2; delta++ {
					if i+dy[delta] < N && j+dx[delta] < M {
						board[i+dy[delta]][j+dx[delta]] += board[i][j]
					}
				}
			}
		}
	}

	fmt.Println(board[N-1][M-1])
}
