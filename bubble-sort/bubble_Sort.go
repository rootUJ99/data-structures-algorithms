package main

import "fmt"

func BubbleSort(arr []int) {
	size := len(arr)

	for i := range arr {
		swapped := false
		for j := 0; j < size-i-1; j++ {
			if arr[j] > arr[j+1] {
				temp := arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp

				swapped = true
			}

		}
		if !swapped {
			break
		}
	}
}

func main() {
	arr := []int{500, 200, 700, 2, 90}
	BubbleSort(arr)
	fmt.Println(arr)
}
