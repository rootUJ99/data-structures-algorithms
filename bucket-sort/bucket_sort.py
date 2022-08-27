def bucket_sort(arr, bucket):
    temp = []
    
    for _ in range(bucket):
        temp.append([])
        
    for i in arr:
        temp[int(i * bucket)].append(i)

    for j in range(bucket):
        temp[j].sort()

    sorted_arr = []
    for k in temp:
        sorted_arr = [*sorted_arr, *k]

    return sorted_arr
        
    
if __name__ == "__main__":
    bucket = 10
    arr = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434] 
    sorted_arr = bucket_sort(arr, bucket)

    print(sorted_arr)