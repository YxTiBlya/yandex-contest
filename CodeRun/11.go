package main

import (
	"bufio"
	"fmt"
	"os"
)

func dfs(graph [][]int, colors []int, now, prev int) {
	colors[now] = 1

	for _, neig := range graph[now] {
		if colors[neig] == 0 {
			if !flag {
				dfs(graph, colors, neig, now)
			}
		} else if colors[neig] == 1 && neig != prev {
			flag = true
			cyclest = neig
			break
		}
	}

	colors[now] = 2
	if flag {
		ans = append(ans, now)
	}
}

var ans []int
var flag = false
var cyclest = 0

func main() {
	var N int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanln(in, &N)

	graph := make([][]int, N+1)
	colors := make([]int, N+1)

	var x int
	for i := 1; i < N+1; i++ {
		row := make([]int, N)
		for j := 0; j < N; j++ {
			fmt.Fscan(in, &x)
			row[j] = x
		}

		for j := i; j < N; j++ {
			if row[j] == 1 {
				graph[i] = append(graph[i], j+1)
				graph[j+1] = append(graph[j+1], i)
			}
		}
	}

	for i := 1; i < N+1; i++ {
		if colors[i] == 0 {
			if flag {
				break
			}
			dfs(graph, colors, i, 0)
		}
	}

	if len(ans) > 0 {
		for true {
			find := false
			for _, v := range graph[ans[len(ans)-1]] {
				if ans[0] == v {
					find = true
				}
			}

			if find {
				break
			}
			ans = ans[:len(ans)-1]
		}
		fmt.Println("YES")
		fmt.Println(len(ans))
		for _, v := range ans {
			fmt.Print(v, " ")
		}
	} else {
		fmt.Println("NO")
	}
}
