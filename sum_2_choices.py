def sum_of_digits(n):
    if len(n)==1:
        return int(n)
    return int(n[0])+sum_of_digits(n[1:])
print(sum_of_digits("125"))
