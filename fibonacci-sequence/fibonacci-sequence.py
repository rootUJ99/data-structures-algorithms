def fibonacci_sequence(n):
    arr = []
    def fibonacci_sequence_util(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci_sequence_util(n-1) + fibonacci_sequence_util(n-2)
    for i in range(n):
        arr.append(fibonacci_sequence_util(i))
    return arr


def fibonacci_squence_top_down(n):
    memo = {}
    arr = []
    def fibonacci_squence_memo_util(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = fibonacci_squence_memo_util(n-1) + fibonacci_squence_memo_util(n-2)

        return memo[n] 
    for i in range(n):
        arr.append(fibonacci_squence_memo_util(i))
    return arr

def fibonacci_sequence_bottom_up(n):
    dp = [0 for _ in range(n)]
    dp[1] = 1
    def fibonacci_sequence_util(n):
        for i in range(2, n):
            if i in dp and dp[i] != 0:
                continue
            dp[i] = dp[i-1] + dp[i-2]
    fibonacci_sequence_util(n)
    return dp
        

if __name__ == "__main__":
    print(fibonacci_sequence(10))
    print(fibonacci_squence_top_down(10))
    print(fibonacci_sequence_bottom_up(10))
