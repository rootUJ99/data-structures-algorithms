def binary_search_recursive(arr, target, left, right):
    if (left <= right):
        mid = (left + right) // 2
        print('yo im here', mid)
        if arr[mid] == target:
            return mid

        elif target > arr[mid]:
            return binary_search_recursive(arr, target, mid+1, right)

        else:
            return binary_search_recursive(arr, target, left, mid-1)
    else:
        return -1



arr = [1,3,4,6,7,8,323,359,555,1000]

result = binary_search_recursive(arr, 6, 0, len(arr) - 1)

print(result)