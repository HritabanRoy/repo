def binary_array_to_number(arr):
    arr.reverse()
    res = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            res = res + (2 ** i)
    return res
print(binary_array_to_number([1, 0, 0, 1]))