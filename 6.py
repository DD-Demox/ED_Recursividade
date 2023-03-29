def elevar(k: int, n: int):
    if n == 1:
        return k
    return k * elevar(k, n-1)


if __name__ == '__main__':
    print(elevar(7, 2))
