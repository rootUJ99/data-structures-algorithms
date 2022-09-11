package main

import (
	"fmt"
	"math"
	"sort"
)

type Query struct {
	left  int
	right int
}

func compareBlocks(query []Query, i int, j int, bLen int) bool {
	q1 := query[i]
	q2 := query[j]
	if int(q1.left/bLen) != int(q2.left/bLen) {
		return int(q1.left/bLen) < int(q2.left/bLen)
	}
	return q1.right < q2.right
}

func main() {
	query := []Query{
		{0, 4},
		{2, 7},
		{1, 5},
	}
	arr := []int{1, 4, 6, 2, 5, 7, 21, 4, 68}
	n := len(arr)
	fmt.Println("query before", query)
	bLen := int(math.Sqrt(float64(n))) + 1

	sort.SliceStable(query, func(i int, j int) bool { return compareBlocks(query, i, j, bLen) })
	fmt.Println("query after", query)

	summations := [3]int{}
	currL := 0
	currR := -1
	currSum := 0
	for i, ele := range query {
		left := ele.left
		right := ele.right

		for currL > left {
			currL -= 1
			currSum += arr[currL]
		}
		for currR < right {
			currR += 1
			currSum += arr[currR]
		}

		for currL < left {
			currSum -= arr[currL]
			currL += 1
		}
		for currR > right {
			currSum -= arr[currR]
			currR -= 1
		}

		fmt.Println("left", left, "right", right, currSum, "sum")
		summations[i] = currSum
	}

	fmt.Println(summations)
}
