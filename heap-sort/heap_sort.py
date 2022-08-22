def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[i]:
        largest = right

    if largest != i:
        arr[largest] , arr[i] = arr[i], arr[largest]
    
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)

if __name__ == "__main__":
    print("heapsort")
    arr = [76,22,43,11,55,100,300,50]
    heap_sort(arr)
    print(arr)