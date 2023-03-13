package main

import "fmt"

func main() {
	var N int
	fmt.Scanln(&N)
	heap := make([]int, N)
	lwc := (N - 2) / 2

	var x int
	for i := 0; i < N; i++ {
		fmt.Scan(&x)
		heap[i] = x
	}

	for i := lwc; i >= 0; i-- {
		pos := i
		for pos*2+1 < N {
			max_son_i := pos*2 + 1
			if max_son_i+1 < N && heap[max_son_i] < heap[max_son_i+1] {
				max_son_i++
			}

			if heap[pos] < heap[max_son_i] {
				heap[pos], heap[max_son_i] = heap[max_son_i], heap[pos]
				pos = max_son_i
			} else {
				break
			}
		}
	}

	j := len(heap) - 1
	for i := 0; i < N; i++ {
		ans := heap[0]
		heap[0] = heap[j]
		pos := 0
		for pos*2+1 < N+j-N {
			max_son_i := pos*2 + 1
			if max_son_i+1 < N && heap[max_son_i] < heap[max_son_i+1] {
				max_son_i++
			}

			if heap[pos] < heap[max_son_i] {
				heap[pos], heap[max_son_i] = heap[max_son_i], heap[pos]
				pos = max_son_i
			} else {
				break
			}
		}
		heap[j] = ans
		j--
	}

	for i := range heap {
		fmt.Print(heap[i], " ")
	}
}
