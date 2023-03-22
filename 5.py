def somatorio(n_final:int):
    if n_final == 1:
        return 1
    return n_final + somatorio(n_final-1)

if __name__ == '__main__':
    print(somatorio(2))