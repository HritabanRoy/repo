def elder_age(m,n,l,t):
    #1 kyu problem, not completed yet
    res = 0
    for x in range(n):
        for y in range(m):
            res = res + (y ^ x) - l if (y ^ x) > 0 else res

    return res%t

print(elder_age(28827050410, 35165045587, 7109602, 13719506))