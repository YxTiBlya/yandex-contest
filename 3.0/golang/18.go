package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type node struct {
	data int
	next *node
	prev *node
}

type dequeue struct {
	len  int
	head *node
	tail *node
}

func create_deq() *dequeue {
	return &dequeue{}
}
func (d *dequeue) push_front(x int) string {
	newNode := &node{data: x}
	if d.head == nil {
		d.head = newNode
		d.tail = newNode
	} else {
		currentNode := d.head
		newNode.next = currentNode
		currentNode.prev = newNode
		d.head = newNode
	}
	d.len++
	return "ok"
}
func (d *dequeue) push_back(x int) string {
	newNode := &node{data: x}
	if d.head == nil {
		d.head = newNode
		d.tail = newNode
	} else {
		currentNode := d.tail
		newNode.prev = currentNode
		currentNode.next = newNode
		d.tail = newNode
	}
	d.len++
	return "ok"
}
func (d *dequeue) pop_front() (int, error) {
	if d.head == nil {
		return 0, errors.New("error")
	}
	currentNode := d.head
	if currentNode.next != nil {
		newCurrentNode := currentNode.next
		newCurrentNode.prev = nil
		d.head = newCurrentNode
	} else {
		d.head = nil
		d.tail = nil
	}
	d.len--
	return currentNode.data, nil
}
func (d *dequeue) pop_back() (int, error) {
	if d.tail == nil {
		return 0, errors.New("error")
	}
	currentNode := d.tail
	if currentNode.prev != nil {
		newCurrentNode := currentNode.prev
		newCurrentNode.next = nil
		d.tail = newCurrentNode
	} else {
		d.head = nil
		d.tail = nil
	}
	d.len--
	return currentNode.data, nil
}
func (d *dequeue) front() (int, error) {
	if d.head == nil {
		return 0, errors.New("error")
	}
	currentNode := d.head
	return currentNode.data, nil
}
func (d *dequeue) back() (int, error) {
	if d.head == nil {
		return 0, errors.New("error")
	}
	currentNode := d.tail
	return currentNode.data, nil
}
func (d *dequeue) size() int {
	return d.len
}
func (d *dequeue) clear() string {
	d.len = 0
	d.head = nil
	d.tail = nil
	return "ok"
}

func main() {
	deq := create_deq()
	in := bufio.NewReader(os.Stdin)

Loop:
	for true {
		cmdb, _, _ := in.ReadLine()
		cmd := strings.Split(string(cmdb), " ")

		switch cmd[0] {
		case "push_front":
			num, _ := strconv.Atoi(cmd[1])
			fmt.Println(deq.push_front(num))
		case "push_back":
			num, _ := strconv.Atoi(cmd[1])
			fmt.Println(deq.push_back(num))
		case "pop_front":
			ans, err := deq.pop_front()
			if err != nil {
				fmt.Println(err)
				continue
			}
			fmt.Println(ans)
		case "pop_back":
			ans, err := deq.pop_back()
			if err != nil {
				fmt.Println(err)
				continue
			}
			fmt.Println(ans)
		case "front":
			ans, err := deq.front()
			if err != nil {
				fmt.Println(err)
				continue
			}
			fmt.Println(ans)
		case "back":
			ans, err := deq.back()
			if err != nil {
				fmt.Println(err)
				continue
			}
			fmt.Println(ans)
		case "size":
			fmt.Println(deq.size())
		case "clear":
			fmt.Println(deq.clear())
		case "exit":
			fmt.Println("bye")
			break Loop
		}
	}
}
