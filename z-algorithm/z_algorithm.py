def create_zarray(string, zarr):
    n = len(string)
    left, right, k= 0, 0, 0
    for i in range(1,n):
        if i > right:
            left, right = i, i
            while right < n and string[right-left] == string[right]:
                right+=1
            zarr[i] = right - left
            right-=1
        else:
            k = i - left
            if zarr[k] < right - i + 1:
                zarr[i] = zarr[k]

            else:
                left = i
                while right < n and string[right-left] == string[right]:
                    right+=1
                zarr[i] = right - left
                right-=1

def find(string, pattern):
    concat_string = pattern + '#' + string
    n = len(concat_string)
    zarr = [0] * n
    create_zarray(concat_string, zarr)
    string_len = len(string)
    pattern_len = len(pattern)
    for i in range(string_len):
        if pattern_len == zarr[i]:
            return i - pattern_len - 1

    return -1
    

if __name__ == "__main__":
    string = "fsabbachaabaabba"
    pattern = "chaa"
    result = find(string, pattern)
    print("result found at", result)