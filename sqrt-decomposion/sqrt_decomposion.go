package main

import (
	"fmt"
	"math"
)

func block_processor(arr []int, block *[]int, blockLen int) {

	for i, item := range arr {
		(*block)[int(i/blockLen)] += item
	}
}

func main() {
	arr := []int{1, 4, 6, 2, 5, 7, 21, 4, 68}
	n := len(arr)

	blockLen := int(math.Sqrt(float64(n))) + 1

	block := make([]int, blockLen)

	block_processor(arr, &block, blockLen)

	querries := [][]int{{1, 5}, {2, 7}, {0, 4}}
	sum := 0
	for _, q := range querries {

		left := q[0]
		right := q[1]

		for i := left; i <= right; {
			if i%blockLen == 0 && i+blockLen-1 <= right {
				sum += block[int(i/blockLen)]
				i += blockLen
			} else {
				sum += arr[i]
				i++
			}
		}
		fmt.Println(sum)
	}
	fmt.Println(sum)
}
