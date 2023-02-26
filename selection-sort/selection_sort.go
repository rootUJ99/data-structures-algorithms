package main

import "fmt"

func SelectionSort(arr []int) {
	size := len(arr)

	for i := 0; i < size-1; i++ {
		min_ele_index := i
		for j := i + 1; j < size; j++ {
			if arr[min_ele_index] > arr[j] {
				min_ele_index = j
			}
		}

		temp := arr[i]
		arr[i] = arr[min_ele_index]
		arr[min_ele_index] = temp

	}

}
func main() {
	arr := []int{40, 310, 30, 2000, 33}
	SelectionSort(arr)
	fmt.Println(arr)

}
