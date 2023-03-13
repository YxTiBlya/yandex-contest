package main

import (
	"bufio"
	"fmt"
	"os"
)

type node struct {
	value int
	arr   []int
	next  *node
}
type Queue struct {
	head *node
	tail *node
}

func new_queue() *Queue {
	return &Queue{}
}

func (q *Queue) add(x int, arrx []int) {
	newNode := &node{value: x, arr: arrx}
	if q.tail == nil {
		q.head = newNode
		q.tail = newNode
	} else {
		currentNode := q.tail
		currentNode.next = newNode
		q.tail = newNode
	}
}
func (q *Queue) pop() (int, []int) {
	currentNode := q.head
	if currentNode.next != nil {
		q.head = currentNode.next
	} else {
		q.head = nil
		q.tail = nil
	}
	return currentNode.value, currentNode.arr
}

func bfs(graph [][]int, start, end int) (int, []int) {
	if start == end {
		return -1, nil
	}

	for queue.head != nil {
		v, path := queue.pop()
		visited[v] = struct{}{}
		for _, node := range graph[v] {
			if _, ok := visited[node]; !ok {
				if node == end {
					path = append(path, end)
					return len(path) - 1, path
				}
				var tmp []int
				tmp = append(tmp, path...)
				tmp = append(tmp, node)
				queue.add(node, tmp)
			}
		}
	}
	return -2, nil
}

var queue = new_queue()
var visited = make(map[int]struct{})

func main() {
	var N, start, end int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanln(in, &N)

	graph := make([][]int, N+1)

	var x int
	for i := 1; i < N+1; i++ {
		ln := make([]int, N)
		for i := 0; i < N; i++ {
			fmt.Fscan(in, &x)
			ln[i] = x
		}
		for j := i; j < len(ln); j++ {
			if ln[j] == 1 {
				graph[i] = append(graph[i], j+1)
				graph[j+1] = append(graph[j+1], i)
			}
		}
	}
	fmt.Fscanf(in, "\n%d %d\n", &start, &end)

	queue.add(start, []int{start})
	l, ans := bfs(graph, start, end)
	if l != -2 {
		if l == -1 {
			fmt.Println(0)
		} else {
			fmt.Println(l)
			for _, v := range ans {
				fmt.Print(v, " ")
			}
		}
	} else {
		fmt.Println(-1)
	}
}
