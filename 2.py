def fibonacci(nTermos):
    if nTermos == 1:
        return 1
    elif nTermos <= 0:
        return 0
    return fibonacci(nTermos-1) + fibonacci(nTermos-2)

if __name__ == '__main__':
    print(fibonacci(2))
