package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var k int
	var S string

	scanner := bufio.NewScanner(os.Stdin)
	const maxCapacity = 1000 * 1024
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	if scanner.Scan() {
		k, _ = strconv.Atoi(scanner.Text())
	}
	if scanner.Scan() {
		S = scanner.Text()
	}

	lns := len(S)
	alp := []rune{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

	ans := 0
	for _, letter := range alp {
		right := 0
		t := k
		count := 0
		for left := 0; left != lns-k; left++ {
			for right < lns && t >= 0 {
				if S[right] != byte(letter) {
					t--
				}
				right++
				count++
			}

			if t < 0 {
				count--
			}

			if S[left] != byte(letter) {
				t++
			}

			if count > ans {
				ans = count
			}
		}
	}

	fmt.Println(ans)
}
