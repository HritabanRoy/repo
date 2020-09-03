# Create a function that checks if a number n is divisible by two numbers x AND y.
# All inputs are positive, non-zero digits.

def divisible(n, x, y):
    if n!=0 and x!=0 and y!=0 and n%x == 0 and n%y == 0 :
        return True;
    else:
        return False;
print(divisible(90, 9, 5))
