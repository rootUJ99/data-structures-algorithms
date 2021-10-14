def binary_serach(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right ) // 2

        if arr[mid] == target:
            return mid
        
        elif target > arr[mid]:
            left = mid + 1

        else:
            right = mid -1


result = binary_serach([1,3,6,8,9,43,56,466,468,2003,45666], 468)
print(result)
