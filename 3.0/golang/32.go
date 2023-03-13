package main

import (
	"bufio"
	"fmt"
	"os"
)

var components = make(map[int]map[int]struct{})

func dfs(graph [][]int, visited map[int]bool, now, compc int) {
	visited[now] = true

	if _, ok := components[compc]; ok == false {
		components[compc] = map[int]struct{}{}
	}

	if len(graph[now]) > 0 {
		for _, v := range graph[now] {
			components[compc][v] = struct{}{}
		}
	} else {
		components[compc][now] = struct{}{}
	}

	for _, neig := range graph[now] {
		if visited[neig] == false {
			dfs(graph, visited, neig, compc)
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

	compc := 0
	for i := 1; i < N+1; i++ {
		if visited[i] == false {
			compc++
			dfs(graph, visited, i, compc)
		}
	}

	fmt.Println(compc)
	for _, v := range components {
		fmt.Println(len(v))
		for k := range v {
			fmt.Print(k, " ")
		}
		fmt.Print("\n")
	}
}
