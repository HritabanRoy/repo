def array_diff(a, b):
    for element in b:
        while element in a:
            a.remove(element)
    return a

print(array_diff([1,2,2,2,3],[2]))