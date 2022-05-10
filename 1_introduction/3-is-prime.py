'''
is prime
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.

test_00:
is_prime(2) # -> True
test_01:
is_prime(3) # -> True
test_02:
is_prime(4) # -> False
test_03:
is_prime(5) # -> True
test_04:
is_prime(6) # -> False
test_05:
is_prime(7) # -> True
test_06:
is_prime(8) # -> False
test_07:
is_prime(25) # -> False
test_08:
is_prime(31) # -> True
test_09:
is_prime(2017) # -> True
test_10:
is_prime(2048) # -> False
test_11:
is_prime(1) # -> False
test_12:
is_prime(713) # -> False
'''


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    upper_limit = int(n ** 0.5) + 1
    for i in range(2, upper_limit + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(5))
