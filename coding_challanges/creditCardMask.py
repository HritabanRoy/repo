# Your task is to write a function maskify,
# which changes all but the last four characters into '#'.

def maskify(key_string=""):
    key_arr = list(key_string)
    for i in range(len(key_arr)-4):
        key_arr[i] = '#'
    return ''.join(key_arr)

print(maskify(""))