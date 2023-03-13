package main

import (
	"fmt"
	"sort"
)

func main() {
	var word string
	fmt.Scanln(&word)

	mp := make(map[rune]int)
	for i, v := range word {
		if _, ok := mp[v]; !ok {
			mp[v] = 0
		}
		mp[v] += len(word[:i+1]) * len(word[i:])
	}

	keys := make([]rune, 0, len(mp))
	for k := range mp {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		return keys[i] < keys[j]
	})

	for _, v := range keys {
		fmt.Printf("%v: %d\n", string(v), mp[v])
	}
}
