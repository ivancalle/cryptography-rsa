from typing import List


def get_factors(number: int, start: int = 2) -> List[int]:
    for i in range(start, number//2+1):
        if number % i == 0:
            return [i]+(get_factors(number//i, i))
    return [number]


def is_prime(number: int) -> bool:
    for x in range(2, int(number/2)+1):
        if number % x == 0:
            return False
    return True


def break_key(public_key: int, product: int):
    primes = get_factors(product)
    for i in range(1, 100):
        if (i*(primes[0]-1)*(primes[1]-1)+1) % public_key == 0:
            return (i*(primes[0]-1)*(primes[1]-1)+1) // public_key, product
    raise Exception('Key not in first 100 constants')
