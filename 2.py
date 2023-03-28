from functools import cache

@cache
def fibonacci(nTermos):
    if nTermos <= 1:
        print(1)
        return 1
    fib = fibonacci(nTermos-1) + fibonacci(nTermos-2)
    print(fib)
    return fib

if __name__ == '__main__':
    fibonacci(10)
