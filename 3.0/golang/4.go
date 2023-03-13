package main

import (
	"fmt"
	"math"
)

func main() {
	N, K, series, place := input()
	var tmp []int

	pplace := series * 2
	if place == 1 {
		pplace--
	}

	pvar := pplace
	if pplace > K {
		pvar %= K
	}

	tmp = append(tmp, pplace-K)
	tmp = append(tmp, pplace+K)

	for i := len(tmp) - 1; i >= 0; i-- {
		if tmp[i] > N || tmp[i] < 1 {
			copy(tmp[i:], tmp[i+1:])
			tmp = tmp[:len(tmp)-1]
		}
	}

	var vseries int
	var vplace int
	if len(tmp) == 2 {
		if math.Abs(float64(series-(tmp[0]+1)/2)) < math.Abs(float64(series-(tmp[1]+1)/2)) {
			vseries = (tmp[0] + 1) / 2
		} else {
			vseries = (tmp[1] + 1) / 2
		}

		if vseries == (tmp[0]+1)/2 {
			vplace = tmp[0]
		} else {
			vplace = tmp[1]
		}
	} else if len(tmp) == 1 {
		vseries = (tmp[0] + 1) / 2
		vplace = tmp[0]
	} else {
		fmt.Println(-1)
		return
	}

	var vn int
	if vplace%2 == 0 {
		vn = 2
	} else {
		vn = 1
	}

	fmt.Println(vseries, vn)
}

func input() (int, int, int, int) {
	var N, K, series, place int
	fmt.Scanln(&N)
	fmt.Scanln(&K)
	fmt.Scanln(&series)
	fmt.Scanln(&place)

	return N, K, series, place
}
