def rgb(r, g, b):
    r_hex = convert(r)
    g_hex = convert(g)
    b_hex = convert(b)
    return r_hex+g_hex+b_hex

def convert(decimal):
    res = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
    if decimal > 255:
        decimal = 255
    elif decimal < 0:
        decimal = 0
    for i in range(2):
        r = decimal % 16
        if r > 9:
            r = alphabet[r-10]
        res.append(str(r))
        decimal = int(decimal / 16)
    res.reverse()
    return ''.join(res)

print(rgb(148, 0, 211))