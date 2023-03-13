package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var queue []int
	ln := 0
	in := bufio.NewReader(os.Stdin)

	i := 0
Loop:
	for true {
		cmdb, _, _ := in.ReadLine()
		cmd := strings.Split(string(cmdb), " ")

		switch cmd[0] {
		case "push":
			num, _ := strconv.Atoi(cmd[1])
			queue = append(queue, num)
			ln += 1
			fmt.Println("ok")
		case "pop":
			if ln-i > 0 {
				fmt.Println(queue[i])
				i += 1
			} else {
				fmt.Println("error")
				continue
			}
		case "front":
			if ln-i > 0 {
				fmt.Println(queue[i])
			} else {
				fmt.Println("error")
				continue
			}
		case "size":
			fmt.Println(ln - i)
		case "clear":
			queue = queue[:0]
			ln, i = 0, 0
			fmt.Println("ok")
		case "exit":
			fmt.Println("bye")
			break Loop
		}
	}
}
