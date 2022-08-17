def calc_interpolation_index(low, high, arr, k):
    index = low + ((k-arr[low])* (high - low)) / (arr[high] - arr[low])
    return int(index)
    

def interpolation_search(arr, k):
    low = 0
    high = len(arr) - 1
    while arr[low] <=k and arr[high] >= k and arr[low]<=arr[high]:
        index = calc_interpolation_index(low, high, arr, k)
        if arr[index] == k:
            return index
        elif arr[index] < k:
            low = index + 1
        else:
            high = index -1  

if __name__ == "__main__":
    arr = [200, 305, 210, 215, 235, 250, 290]
    k = 250
    result = interpolation_search(arr, k)
    print("the array found at", result)