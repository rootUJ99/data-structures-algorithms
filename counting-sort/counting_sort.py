def max_ele(arr):
    max=arr[0]
    for i in arr:
        if i > max:
            max = i
    return max
    
def couning_sort(arr):
    max = max_ele(arr)
    count = [0] * (max+1)

    for i in arr:
        count[i]+=1

    lastindex = 0

    for i in range(max + 1):
        while count[i] > 0:
            arr[lastindex] = i
            lastindex +=1
            count[i] -=1

if __name__ == "__main__":
    arr = [33,42,14,11,34,63,73,51,91]
    couning_sort(arr)
    print(arr)