import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

# run following in python shell
# from prime import is_prime
# is_prime(5)
# test_prime(8)
# Check manually