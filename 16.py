def fatorial_duplo(numero):
    if numero % 2 == 0:
        raise ValueError("Numero não é impar")
    else:
        if numero == 1:
            return 1
        return numero * fatorial_duplo(numero - 2)

if __name__ == '__main__':
    print(fatorial_duplo(11))