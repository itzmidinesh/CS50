from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")
        

# run following in python shell
# from test0 import test_prime
# test_prime(5, True)
# test_prime(8, False)