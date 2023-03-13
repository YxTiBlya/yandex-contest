package main

import "fmt"

func main() {
	minx, miny := 10000000000, 10000000000
	maxx, maxy := 0, 0

	var k int
	fmt.Scanln(&k)

	for i := 0; i < k; i++ {
		var x, y int
		fmt.Scanf("%d %d\n", &x, &y)

		if x < minx {
			minx = x
		}
		if y < miny {
			miny = y
		}
		if x > maxx {
			maxx = x
		}
		if y > maxy {
			maxy = y
		}
	}

	fmt.Println(minx, miny, maxx, maxy)
}
