def soma_int(vetor:list):
    if len(vetor) == 1:
        return vetor.pop()
    return vetor.pop() + soma_int(vetor)


if __name__ == '__main__':
    vetor = [1, 2, 3, 4, 5, 6]
    print(soma_int(vetor))
