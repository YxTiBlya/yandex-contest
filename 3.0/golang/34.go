package main

import (
	"bufio"
	"fmt"
	"os"
)

func dfs(graph [][]int, colors []int, now int) {
	colors[now] = 1

	for _, neig := range graph[now] {
		if colors[neig] == 0 {
			dfs(graph, colors, neig)
		} else if colors[neig] == 1 {
			flag = false
			break
		}
	}

	colors[now] = 2
	ans = append(ans, now)
}

var flag = true
var ans []int

func main() {
	var N, M int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanf(in, "%d %d\n", &N, &M)

	graph := make([][]int, N+1)
	colors := make([]int, N+1)

	var v, e int
	for i := 0; i < M; i++ {
		fmt.Fscanf(in, "%d %d\n", &v, &e)
		graph[v] = append(graph[v], e)
	}

	fmt.Println(graph)
	for i := 1; i < N+1; i++ {
		if colors[i] == 0 {
			dfs(graph, colors, i)
		}
	}

	if flag {
		for i := len(ans) - 1; i >= 0; i-- {
			fmt.Print(ans[i], " ")
		}
	} else {
		fmt.Println(-1)
	}
}
