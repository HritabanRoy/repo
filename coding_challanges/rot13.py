def rot13(message):
    message = list(message)
    for i in range(len(message)):
        encrypt = chr(ord(message[i]) + 13)
        if ord(message[i]) >= ord('a') and ord(message[i]) <=ord('z'):
            message[i] = encrypt if ord(encrypt) <= ord('z') else chr(ord('a')+(ord(encrypt)-ord('z')-1))
        if ord(message[i]) >= ord('A') and ord(message[i]) <= ord('Z'):
            message[i] = encrypt if ord(encrypt) <= ord('Z') else chr(ord('A') + (ord(encrypt) - ord('Z')-1))
    message = "".join(message)
    return message
print(rot13("test"))