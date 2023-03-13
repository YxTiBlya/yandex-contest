package main

import "fmt"

type stack struct {
	arr [][]int
	ln  int
}

func (stack *stack) append(x ...[]int) {
	for _, v := range x {
		stack.arr = append(stack.arr, v)
		stack.ln += 1
	}
}

func (stack *stack) pop() []int {
	num := stack.arr[stack.ln-1]
	stack.arr = stack.arr[:stack.ln-1]
	stack.ln -= 1

	return num
}

func main() {
	var slice [][]int
	stack := stack{arr: slice, ln: 0}

	var N int
	fmt.Scanln(&N)
	ans := make([]int, N)
	for i := range ans {
		ans[i] = -1
	}

	var x int
	for i := 0; i < N; i++ {
		fmt.Scan(&x)

		if stack.ln > 0 {
			for j := stack.ln - 1; j >= 0; j-- {
				if x < stack.arr[j][1] {
					tmp := stack.pop()
					ans[tmp[0]] = i
				} else {
					break
				}
			}
			stack.append([]int{i, x})
		} else {
			stack.append([]int{i, x})
		}
	}

	for _, v := range ans {
		fmt.Print(v, " ")
	}
}
