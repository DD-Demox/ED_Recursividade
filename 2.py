from functools import cache

# tentativa de colocar o print dentro da propria função antes de conhecer memoization para dimunuir numeros de
# repetiçao de chamada da propria funçao. Sem sucesso.
@cache
def fibonacci_seq(n_termos):
    if n_termos < 1:
        print(0)
        return 0
    elif n_termos <= 2:
        print(1)
        return 1
    fib = fibonacci_seq(n_termos - 1) + fibonacci_seq(n_termos - 2)
    print(fib)
    return fib


@cache
def fibonacci(n_termo):
    if n_termo <= 1:
        return 0
    if n_termo <= 2:
        return 1
    return fibonacci(n_termo - 1) + fibonacci(n_termo - 2)


if __name__ == '__main__':
    for i in range(10):
        print(fibonacci(i+1))
    # print(fibonacci(1))
