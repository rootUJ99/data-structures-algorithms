package main

import "fmt"

func InsertionSort(arr []int) {
	for i, ele := range arr {
		j := i - 1
		for j >= 0 && arr[j] > ele {
			arr[j+1] = arr[j]
			j = j - 1
		}
		arr[j+1] = ele // insertion of small ele to the start happens here
	}
}

func main() {
	arr := []int{5, 4, 3, 2, 1}
	InsertionSort(arr)
	fmt.Print(arr)
}
