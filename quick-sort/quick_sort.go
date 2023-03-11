package main

import "fmt"

func swap(left *int, right *int) {
	temp := *left
	*left = *right
	*right = temp
}

func partition(arr []int, low int, high int) int {
	left := low
	right := high - 1
	pviot := arr[high]

	for left <= right {
		if arr[left] < pviot {
			left += 1
		}

		if arr[right] > pviot {
			right -= 1
		}

		if left < right {
			swap(&arr[left], &arr[right])

		}

	}

	swap(&arr[left], &arr[high])

	return left
}

func quick_sort(arr []int, low int, high int) {
	if low < high {
		p := partition(arr, low, high)

		quick_sort(arr, p+1, high)

		quick_sort(arr, low, p-1)

	}
}

func main() {
	arr := []int{200, 20, 50, 500, 900, 600}
	low := 0
	high := len(arr) - 1
	quick_sort(arr, low, high)
	fmt.Println(arr)
}
