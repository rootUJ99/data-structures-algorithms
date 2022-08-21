def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_ele:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = current_ele
if __name__ == "__main__":
    arr = [44,22,43,53,21,200,45,300]
    insertion_sort(arr)
    print(arr)
