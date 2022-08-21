def partition(arr, low, high):
    left = low
    right = high - 1
    pivot = arr[high]

    while left <= right:

        while arr[left] < pivot:
            left = left + 1

        while arr[right] > pivot:
            right = right - 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[left], arr[high] = arr[high], arr[left]

    return left

def quick_sort(arr, low, high):
    if (low < high):
        p = partition(arr, low, high)

        quick_sort(arr, p + 1, high)

        quick_sort(arr, low, p - 1)

if __name__ == "__main__":
    arr = [200,900,50,96,220,700,400]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
