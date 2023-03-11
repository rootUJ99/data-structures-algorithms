package main

import "fmt"

func MergeSort(arr []int) {
	// since go on creation of the slice based on original array still preserves the reference needed to do following two steps
	new_arr := make([]int, len(arr))
	copy(new_arr, arr)

	size := len(new_arr)
	if size > 1 {
		mid := size / 2
		left := new_arr[0:mid]
		right := new_arr[mid:size]

		MergeSort(left)
		MergeSort(right)

		i := 0
		j := 0
		k := 0
		for i < len(left) && j < len(right) {
			if left[i] > right[j] {
				arr[k] = right[j]
				j += 1
			} else {
				arr[k] = left[i]
				i += 1
			}
			k += 1

		}
		fmt.Println("print stage original", arr)
		for i < len(left) {
			arr[k] = left[i]
			i += 1
			k += 1
		}
		fmt.Println("print stage i", arr)

		for j < len(right) {
			arr[k] = right[j]
			j += 1
			k += 1
		}
		fmt.Println("print stage j", arr)

	}

}

func main() {
	arr := []int{100, 400, 20, 50, 6, 90, 9}
	MergeSort(arr)
	fmt.Println(arr)

}
