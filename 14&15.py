def par_crescente (n :int, parada = 0):
    if n % 2 != 0:
        raise ValueError("Numero não é par")
    if n == parada:
        print(n)
    else:
        print(parada)
        par_crescente(n, parada+2)


def par_decrescente(n :int):
    if n % 2 != 0:
        raise ValueError("Numero não é par")
    if n == 0:
        print(n)
    else:
        print(n)
        par_decrescente(n - 2)

if __name__ == '__main__':
    par_decrescente(10)
    par_crescente(20)