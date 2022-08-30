def counting_sort(arr, n, div):
    count = [0] * 10


    for i in range(0, n):
        count[(arr[i]//div)%10]+=1
    # print(count, 'before')

    for i in range(1, 10):
        count[i]+=count[i-1]
    # print(count, 'after')

    temp = [0] * 10

    for i in range(n-1, -1, -1):
        temp[count[(arr[i]//div)%10]-1] = arr[i]
        count[(arr[i]//div)%10]-=1
    # print(temp, 'temp')
    # print(count, 'count --')

    for i in range(0, len(arr)):
        arr[i] = temp[i]
    

def radix_sort(arr, n):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max: max = arr[i]

    div = 1
    while max/div > 1:
        counting_sort(arr, n, div)
        div*=10


if __name__ == "__main__":
    arr = [32,443,32,88,771,39]
    radix_sort(arr, len(arr))
    # print(arr)