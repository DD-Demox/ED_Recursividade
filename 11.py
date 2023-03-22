def multip_rec(n1: int, n2:  int):
    if n2 == 1:
        return n1
    return n1 + multip_rec(n1,n2-1)


if __name__ == '__main__':
    print(multip_rec(2, 10))