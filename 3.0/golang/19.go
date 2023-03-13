package main

import "fmt"

func main() {
	var N int
	fmt.Scanln(&N)
	var heap []int

	for i := 0; i < N; i++ {
		var cmd, num int
		fmt.Scanf("%d %d\n", &cmd, &num)

		if cmd == 0 {
			heap = append(heap, num)
			pos := len(heap) - 1
			for pos > 0 && heap[pos] > heap[(pos-1)/2] {
				heap[pos], heap[(pos-1)/2] = heap[(pos-1)/2], heap[pos]
				pos = (pos - 1) / 2
			}
		} else {
			ans := heap[0]
			heap[0] = heap[len(heap)-1]
			pos := 0
			for pos*2+2 < len(heap) {
				max_son_i := pos*2 + 1
				if heap[max_son_i] < heap[max_son_i+1] {
					max_son_i++
				}

				if heap[pos] < heap[max_son_i] {
					heap[pos], heap[max_son_i] = heap[max_son_i], heap[pos]
					pos = max_son_i
				} else {
					break
				}
			}
			heap = heap[:len(heap)-1]
			fmt.Println(ans)
		}
	}
}
