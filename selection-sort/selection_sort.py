def selection_sort(arr):
    size = len(arr)
    for i in range(size -1):
        min_index = i
        for j in range(i+1, size):
            print('im here')
            if arr[j] < arr[min_index]:
                min_index = j
            
                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index] = temp


if __name__ == "__main__":
    print("this is sleecttion sort")
    arr = [534, 6454, 11, 422355, 6562]
    selection_sort(arr)
    print(arr)