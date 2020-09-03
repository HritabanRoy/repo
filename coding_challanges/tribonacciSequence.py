def tribonacci(signature, n):
    res = signature
    for i in range(n):
        l = len(res)
        res.append(res[l-3]+res[l-2]+res[l-1])
    return res[:5]

print(tribonacci([1,1,1],2))