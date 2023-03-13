package main

import (
	"fmt"
	"math"
)

func main() {
	var first, second []float64
	for i := 0; i < 10; i++ {
		var x float64
		fmt.Scan(&x)
		if i < 5 {
			first = append(first, x)
		} else {
			second = append(second, x)
		}
	}
	lenf := len(first)
	lens := len(second)

	i := 0
	for i <= 1000000 {
		if math.Min(first[i], second[i]) == 0 && math.Max(first[i], second[i]) == 9 {
			if first[i] == 0 {
				first = append(first, first[i])
				first = append(first, second[i])
				lenf += 2
			} else {
				second = append(second, first[i])
				second = append(second, second[i])
				lens += 2
			}
		} else {
			if first[i] > second[i] {
				first = append(first, first[i])
				first = append(first, second[i])
				lenf += 2
			} else {
				second = append(second, first[i])
				second = append(second, second[i])
				lens += 2
			}
		}

		i++
		if float64(i) > math.Min(float64(lenf), float64(lens))-1 {
			break
		}
	}

	if i == lenf {
		fmt.Println("second", i)
	} else if i == lens {
		fmt.Println("first", i)
	} else {
		fmt.Println("botva")
	}
}
