def fibonacci_memo(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
    return memo[n]
n=7
print(fibonacci_memo(n,{}))