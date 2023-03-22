def num_digito(n: int, k: int):
    if n//10 == 0:
        if n % 10 == k:
            return 1
        else:
            return 0
    if n % 10 == k:
        return 1 + num_digito(n//10, k)
    else:
        return 0 + num_digito(n//10, k)

if __name__ == '__main__':
    print(num_digito(12342353234542, 3))
