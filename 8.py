def mdc(x: int, y: int):
    if y == 0:
        return x
    return mdc(y, x % y)

if __name__ == '__main__':

    print(mdc(24,15))
