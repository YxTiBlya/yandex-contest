package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	cards, interests := Input()

	ln := len(cards)
	mx := cards[ln-1]

	for _, interest := range interests {
		if interest > mx {
			fmt.Println(ln)
		} else {
			fmt.Println(binary_search(cards, interest))
		}
	}
}

func Input() ([]int, []int) {
	in := bufio.NewReader(os.Stdin)

	_, _ = in.ReadString('\n')

	cardss, _ := in.ReadString('\n')
	cardsarr := strings.Split(strings.TrimSpace(cardss), " ")
	set := make(map[int]struct{})
	for _, v := range cardsarr {
		num, _ := strconv.Atoi(v)
		set[num] = struct{}{}
	}

	cards := make([]int, len(set))
	i := 0
	for k := range set {
		cards[i] = k
		i++
	}
	sort.Ints(cards)

	ks, _ := in.ReadString('\n')
	k, _ := strconv.Atoi(strings.TrimSpace(ks))

	interests := make([]int, k)
	interestss, _ := in.ReadString('\n')
	interestsarr := strings.Split(strings.TrimSpace(interestss), " ")
	for i, v := range interestsarr {
		num, _ := strconv.Atoi(v)
		interests[i] = num
	}

	return cards, interests
}

func binary_search(arr []int, x int) int {
	low := 0
	high := len(arr) - 1
	mid := 0

	for low <= high {
		mid = (high + low) / 2
		if arr[mid] < x {
			low = mid + 1
		} else if arr[mid] > x {
			high = mid - 1
		} else {
			return mid
		}
	}

	if arr[mid] < x {
		return mid + 1
	}
	return mid
}
