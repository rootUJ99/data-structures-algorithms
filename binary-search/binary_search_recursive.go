package main

import (
	"fmt"
)

func BinarySerach(arr []int, target int, left int, right int) int {
	if left > right {
		return -1
	}
	mid := (left + right) / 2
	if arr[mid] == target {
		return mid
	} else if arr[mid] > target {
		return BinarySerach(arr, target, left, mid-1)
	} else {
		return BinarySerach(arr, target, mid+1, right)
	}
}

func main() {
	arr := []int{2, 4, 6, 78, 99, 344, 653, 1000, 55555}
	searchedIndex := BinarySerach(arr, 1000, 0, len(arr)-1)
	fmt.Println(searchedIndex)
}
