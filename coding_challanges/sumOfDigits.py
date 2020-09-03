def digital_root(n):
    while n > 9:
        n_arr = list(str(n))
        n = 0
        for i in n_arr:
            n = n + int(i)
    return n
print(digital_root(493193))


