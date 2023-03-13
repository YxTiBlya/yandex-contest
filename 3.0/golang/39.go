package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var N int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscanln(in, &N)

	var blocks [][]string
	field := make([][][]int, N)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			var lastl []int
			for k := 0; k < N; k++ {
				lastl = append(lastl, -1)
			}
			field[i] = append(field[i], lastl)
		}
	}
	dm := []int{-1, 1}
	x, y, z := 0, 0, 0

	for k := 0; k < N; k++ {
		fmt.Fscanln(in)

		var tmp []string
		var layer string
		for i := 0; i < N; i++ {
			fmt.Fscanln(in, &layer)
			tmp = append(tmp, layer)

			for j := 0; j < N; j++ {
				if layer[j] == 'S' {
					x, y, z = j, i, k
				}
			}
		}
		blocks = append(blocks, tmp)
	}

	field[z][y][x] = 0
	res := make(map[int][][]int)
	res[0] = [][]int{{z, y, x}}
	ans := 0
	for i := 1; i < int(math.Pow(float64(N), float64(3))); i++ {
		res[i] = [][]int{}
		for _, coords := range res[i-1] {
			for delta := 0; delta < 2; delta++ {
				z = coords[0]
				y = coords[1]
				x = coords[2]

				if 0 <= z+dm[delta] && z+dm[delta] < N && blocks[z+dm[delta]][y][x] == '.' {
					if field[z+dm[delta]][y][x] == -1 {
						field[z+dm[delta]][y][x] = i
						res[i] = append(res[i], []int{z + dm[delta], y, x})
						if z+dm[delta] == 0 && ans == 0 {
							ans = i
							break
						}
					}
				}
				if 0 <= y+dm[delta] && y+dm[delta] < N && blocks[z][y+dm[delta]][x] == '.' {
					if field[z][y+dm[delta]][x] == -1 {
						field[z][y+dm[delta]][x] = i
						res[i] = append(res[i], []int{z, y + dm[delta], x})
					}
				}
				if 0 <= x+dm[delta] && x+dm[delta] < N && blocks[z][y][x+dm[delta]] == '.' {
					if field[z][y][x+dm[delta]] == -1 {
						field[z][y][x+dm[delta]] = i
						res[i] = append(res[i], []int{z, y, x + dm[delta]})
					}
				}
			}
		}
		if len(res[i]) == 0 {
			break
		}
	}

	fmt.Println(ans)
}
