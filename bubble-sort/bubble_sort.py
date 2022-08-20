def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(0, size-i-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


if __name__ == "__main__":
    print("this is bubble sort")
    arr = [44,21,500,200,700,100]
    bubble_sort(arr)
    print(arr)