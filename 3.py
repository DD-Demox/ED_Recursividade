def reverter(num, num_rev=0):
    if num == 0:
        return num_rev
    num_rev = num_rev * 10 + num % 10
    return reverter(num // 10, num_rev)


print(reverter(123))