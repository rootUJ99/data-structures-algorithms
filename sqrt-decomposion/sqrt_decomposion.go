package main

import (
	"fmt"
	"math"
)

func block_processor(arr []int, block *[]int) {
	len := len(*block)
	for i, item := range arr {
		(*block)[int(i/len)] += item
	}
	println(*block)
}

func main() {
	arr := []int{1, 4, 6, 2, 5, 7, 21, 4, 68}
	n := len(arr)
	// n := 10
	// arr := make([]int, n)
	// for i := 0; i < n; i++ {
	// 	fmt.Scanf("%d", &arr[i])
	// }
	fmt.Println("yo", arr)
	sqrtLen := int(math.Sqrt(float64(n))) + 1
	// println(sqrt)

	block := make([]int, sqrtLen)

	block_processor(arr, &block)
	// println(block, "here is a block")

	querries := [][]int{{1, 5}, {2, 7}, {0, 4}}
	sum := 0
	for _, q := range querries {
		left := q[0]
		right := q[1]
		// println(left, right)

		for i := left; i <= right; {
			if i%sqrtLen == 0 && i+sqrtLen-1 <= right {
				sum += block[int(i/sqrtLen)]
				i += sqrtLen
			} else {
				sum += arr[i]
				i++
			}
		}
		println(sum)
	}
	println(sum)
}
