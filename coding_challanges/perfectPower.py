from random import random, randrange
from math import log, floor
def isPP(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            print(i)
            for j in range(2, int(n**(1/i))+i):
                print(["try:", i,j])
                if i ** j == n:
                    return [i, j]
                elif i ** j > n:
                    break
    return
pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]

print(isPP(15645464545))