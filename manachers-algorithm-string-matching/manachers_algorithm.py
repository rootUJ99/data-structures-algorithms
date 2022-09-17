def print_substring(str, left, right):
    for i in range(left, right+1):
        print(str[i], end="")



def longest_substring(s):
    str_len = 2 * len(s) + 3
    str_chars = [0] * str_len
    str_chars[0] = '@'
    str_chars[-1] = '$'
    j = 1
    for i in s:
        str_chars[j] = "#"
        j+=1
        str_chars[j] = i
        j+=1
    str_chars[j] = "#"
    max_right = 0
    center = 0
    max_len = 0
    start= 0

    p = [0] * str_len

    for i in range(1, str_len - 1):
        if i < max_right:
            p[i] = min(max_right - i, p[2 * center - i])
        
        while str_chars[i + p[i] + 1] == str_chars[i - p[i] - 1]:
            p[i]+=1
        
        if i + p[i] > max_right:
            center = i
            max_right = i + p[i]

        if p[i] > max_len:
            start= int((i - p[i] -1) / 2)
            max_len = p[i]
    print(p)
    print(str_chars)
    print_substring(s, start, start + max_len - 1)

if __name__ == "__main__":
    string = "abbadazbbac"
    longest_substring(string)