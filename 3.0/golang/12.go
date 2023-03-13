package main

import (
	"fmt"
	"strings"
)

type stack struct {
	arr []rune
	ln  int
}

func (stack *stack) append(x ...rune) {
	for _, v := range x {
		stack.arr = append(stack.arr, v)
		stack.ln += 1
	}
}

func (stack *stack) pop() rune {
	c := stack.arr[stack.ln-1]
	stack.arr = stack.arr[:stack.ln-1]
	stack.ln -= 1

	return c
}

func (stack *stack) last() rune {
	return stack.arr[stack.ln-1]
}

func main() {
	var slice []rune
	stack := stack{arr: slice, ln: 0}

	var input string
	fmt.Scanln(&input)

Loop:
	for _, v := range input {
		if strings.ContainsRune("([{", v) {
			stack.append(v)
		} else {
			if stack.ln == 0 {
				stack.ln = -1
				break
			} else {
				switch {
				case v == ')' && stack.last() == '(':
					stack.pop()
				case v == ']' && stack.last() == '[':
					stack.pop()
				case v == '}' && stack.last() == '{':
					stack.pop()
				default:
					stack.ln = -1
					break Loop
				}
			}
		}
	}

	if stack.ln == 0 {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}
}
