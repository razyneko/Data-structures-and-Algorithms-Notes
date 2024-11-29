# Fibonacci sequence is a sequence in which each number is the sum of two preceding numbers and sequence starts from 0 and 1

def fibo(n):
    assert n >= 0 and int(n) == n, 'The number must be non negative'
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
    
print(fibo(6))