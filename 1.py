def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    return numero * fatorial(numero-1)

if __name__ == "__main__":
    print(fatorial(5))
