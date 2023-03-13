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

func bfs(lines [][]int, end int) int {
	for queue.head != nil {
		v, path := queue.pop()
		visited[v] = struct{}{}
		for _, node := range lines[v] {
			if _, ok := visited[node]; !ok {
				if node == end {
					path = append(path, end)
					return len(path) - 2
				}
				var tmp []int
				tmp = append(tmp, path...)
				tmp = append(tmp, node)
				queue.add(node, tmp)
			}
		}
	}
	return -1
}

var queue = new_queue()
var visited = make(map[int]struct{})

func main() {
	var N, M, start, end int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanln(in, &N)
	fmt.Fscanln(in, &M)

	lines := make([][]int, N+1)

	var c, x int
	for i := 0; i < M; i++ {
		var line []int
		fmt.Fscan(in, &c)
		for j := 0; j < c; j++ {
			fmt.Fscan(in, &x)
			line = append(line, x)
		}

		for _, i := range line {
			for _, j := range line {
				if i != j {
					lines[i] = append(lines[i], j)
				}
			}
		}
	}
	fmt.Fscanf(in, "\n%d %d\n", &start, &end)
	queue.add(start, []int{start})

	ans := bfs(lines, end)
	if ans != -1 {
		fmt.Println(ans)
	} else {
		fmt.Println(-1)
	}
}
