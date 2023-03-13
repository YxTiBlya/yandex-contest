package main

import (
	"bufio"
	"fmt"
	"os"
)

func dfs(graph [][]int, visited map[int]bool, now int) {
	visited[now] = true
	for _, neig := range graph[now] {
		if visited[neig] == false {
			dfs(graph, visited, neig)
		}
	}
}

func main() {
	var N, M int

	in := bufio.NewReader(os.Stdin)
	fmt.Fscanf(in, "%d %d\n", &N, &M)

	graph := make([][]int, N+1)
	visited := make(map[int]bool)
	for i := 0; i < N+1; i++ {
		visited[i] = false
	}

	var v, e int
	for i := 0; i < M; i++ {
		fmt.Fscanf(in, "%d %d\n", &v, &e)
		graph[v] = append(graph[v], e)
		graph[e] = append(graph[e], v)
	}

	dfs(graph, visited, 1)

	var ans []int
	for i := 0; i < N+1; i++ {
		if visited[i] {
			ans = append(ans, i)
		}
	}

	fmt.Println(len(ans))
	for _, v := range ans {
		fmt.Print(v, " ")
	}
}
