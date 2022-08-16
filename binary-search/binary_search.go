package main

import (
	"fmt"
)

func BinarySerach(arr []int, target int) int {
	left := 0
	right := len(arr) - 1
	for left <= right {
		mid := (left + right) / 2
		if arr[mid] == target {
			fmt.Println("Item found at", mid)
			return mid
		} else if arr[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}

func main() {
	arr := []int{1, 3, 4, 5, 6, 66, 77, 888, 8822, 9522}
	target := 77
	searchedVal := BinarySerach(arr, target)
	fmt.Println("searched item index", searchedVal)
}
