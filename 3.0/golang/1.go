package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	in := bufio.NewReader(f)

	mp := make(map[rune]int)
	mx := 1

	for {
		lineb, _, err := in.ReadLine()
		if err != nil {
			break
		}
		words := strings.Split(string(lineb), " ")
		line := strings.Join(words, "")

		for _, c := range line {
			if val, ok := mp[c]; ok {
				mp[c] = val + 1
				if mp[c] > mx {
					mx = mp[c]
				}
			} else {
				mp[c] = 1
			}
		}
	}

	var s []string
	for i := range mp {
		s = append(s, string(i))
	}

	sort.Strings(s)
	for i := mx; i > 0; i-- {
		str := ""
		for _, v := range s {
			if mp[[]rune(v)[0]] >= i {
				str += "#"
			} else {
				str += " "
			}
		}
		fmt.Println(str)
	}
	fmt.Println(strings.Join(s, ""))
}
