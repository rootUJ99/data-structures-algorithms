package main

import "fmt"

func Swap(a *int, b *int) {
	temp := *a
	*a = *b
	*b = temp
}

func Heapify(arr []int, n int, i int) {
	largest := i
	left := int((i * 2) + 1)
	right := int((i * 2) + 2)

	if left <= n && arr[left] > arr[largest] {
		largest = left
	}

	if right <= n && arr[right] > arr[largest] {
		largest = right
	}

	if i != largest {
		Swap(&arr[i], &arr[largest])
		Heapify(arr, n, largest)
	}
}

func main() {
	arr := []int{22, 43, 200, 11, 222, 424, 65, 70}
	n := len(arr) - 1
	for i := int(n / 2); i >= 0; i-- {
		// fmt.Println(i)
		Heapify(arr, n, i)
	}
	for i := n; i > 0; i-- {
		// fmt.Println(i)
		Heapify(arr, i, 0)
		Swap(&arr[0], &arr[i])
	}
	fmt.Print("yola", arr)
}
