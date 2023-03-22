import random


def reverte_vetor(v: list, vetor_reverso=[]):
    if len(v) == 0:
        return vetor_reverso
    vetor_reverso.append(v.pop(-1))
    return reverte_vetor(v, vetor_reverso)


if __name__ == '__main__':
    vetor = []
    for i in range(100):
        vetor.append(random.randint(0, 1000))

    print(vetor)
    print(reverte_vetor(vetor))
