package main

import "fmt"

type stack struct {
	arr []int
	ln  int
}

func (stack *stack) append(x ...int) {
	for _, v := range x {
		stack.arr = append(stack.arr, v)
		stack.ln += 1
	}
}

func (stack *stack) pop() int {
	num := stack.arr[stack.ln-1]
	stack.arr = stack.arr[:stack.ln-1]
	stack.ln -= 1

	return num
}

func main() {
	var slice1, slice2 []int
	stack1 := stack{arr: slice1, ln: 0}
	stack2 := stack{arr: slice2, ln: 0}

	var N int
	fmt.Scanln(&N)
	var x int
	for i := 0; i < N; i++ {
		fmt.Scan(&x)

		if stack1.ln > 0 {
			for j := stack1.ln - 1; j >= 0; j-- {
				if x > stack1.arr[j] {
					stack2.append(stack1.pop())
				} else {
					break
				}
			}
			stack1.append(x)
		} else {
			stack1.append(x)
		}
	}

	for i := stack1.ln - 1; i >= 0; i-- {
		if stack2.ln > 0 {
			if stack1.arr[i] < stack2.arr[stack2.ln-1] {
				break
			}
		}
		stack2.append(stack1.pop())
	}

	for i := 1; i < stack2.ln; i++ {
		if stack2.arr[i] < stack2.arr[i-1] {
			stack2.arr[0] = -1
		}
	}

	if stack2.ln == N && stack2.arr[0] == 1 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
