package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

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
	var slice []int
	stack := stack{arr: slice, ln: 0}

	in := bufio.NewReader(os.Stdin)
	inps, _ := in.ReadString('\n')
	input := strings.Split(strings.TrimSpace(inps), " ")

	for _, v := range input {
		num, err := strconv.Atoi(v)
		if err == nil {
			stack.append(num)
		} else {
			switch v {
			case "+":
				stack.append(stack.pop() + stack.pop())
			case "*":
				stack.append(stack.pop() * stack.pop())
			case "-":
				num2 := stack.pop()
				stack.append(stack.pop() - num2)
			}
		}
	}
	fmt.Println(stack.arr[stack.ln-1])
}
