package main

import (
	"bufio"
	"fmt"
	"os"
)

func dfs(graph [][]int, visited map[int]int, now, color int) {
	visited[now] = color
	color = 3 - color

	for _, neig := range graph[now] {
		if visited[neig] == 0 {
			dfs(graph, visited, neig, color)
		}
	}
}

func main() {
	var N, M int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanf(in, "%d %d\n", &N, &M)

	graph := make([][]int, N+1)
	visited := make(map[int]int)
	for i := 0; i < N+1; i++ {
		visited[i] = 0
	}

	var v, e int
	for i := 0; i < M; i++ {
		fmt.Fscanf(in, "%d %d\n", &v, &e)
		graph[v] = append(graph[v], e)
		graph[e] = append(graph[e], v)
	}

	color := 1
	for i := 1; i < N+1; i++ {
		if visited[i] == 0 {
			dfs(graph, visited, i, color)
			color = 3 - color
		}
	}

	flag := true
	for i := 1; i < N+1; i++ {
		for _, node := range graph[i] {
			if visited[node] == visited[i] {
				flag = false
				break
			}
		}
	}

	if flag {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
