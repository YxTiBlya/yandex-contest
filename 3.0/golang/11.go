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

func (stack *stack) clear() {
	stack.arr = stack.arr[:0]
	stack.ln = 0
}

func main() {
	var slice []int
	stack := stack{arr: slice, ln: 0}

	in := bufio.NewReader(os.Stdin)

Loop:
	for true {
		cmdb, _, _ := in.ReadLine()
		cmd := strings.Split(string(cmdb), " ")

		switch {
		case cmd[0] == "push":
			num, _ := strconv.Atoi(cmd[1])
			stack.append(num)
			fmt.Println("ok")

		case cmd[0] == "pop":
			if stack.ln == 0 {
				fmt.Println("error")
				continue
			}
			fmt.Println(stack.pop())

		case cmd[0] == "back":
			if stack.ln == 0 {
				fmt.Println("error")
				continue
			}
			fmt.Println(stack.arr[stack.ln-1])

		case cmd[0] == "size":
			fmt.Println(stack.ln)

		case cmd[0] == "clear":
			stack.clear()
			fmt.Println("ok")

		case cmd[0] == "exit":
			fmt.Println("bye")
			break Loop
		}
	}
}
