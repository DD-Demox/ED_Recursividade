def crescente (n :int, parada = 0):
    if n == parada:
        print(n)
    else:
        print(parada)
        crescente(n, parada+1)


def decrescente(n :int):
    if n == 0:
        print(n)
    else:
        print(n)
        decrescente(n - 1)


if __name__ == '__main__':
    decrescente(10)
    crescente(10)