from random import SystemRandom
from typing import Set, Tuple
from functools import reduce
import operator

from .encrypter import Encrypter
from .decrypter import Decrypter
from .utils import get_factors, is_prime


class KeyGenerator:
    def __init__(
        self,
        seed: int | None = None,
        prime_min: int = 10000,
        prime_max=100000,
        constant_min: int = 10,
        constant_max=100
    ) -> None:
        self._random = SystemRandom(seed)
        self._prime_min = prime_min
        self._prime_max = prime_max
        self._constant_min = constant_min
        self._constant_max = constant_max

    def _get_prime(self, min: int, max: int) -> int:
        diff = max-min
        start = self._random.randint(0, diff)
        for i in range(diff+1):
            number = min+(start+i) % (diff+1)
            if is_prime(number):
                return number

        raise Exception('Prime not found')

    def _get_primes(self) -> Tuple[int, int]:
        primes: Set[int] = set()
        while len(primes) < 2:
            primes.add(self._get_prime(self._prime_min, self._prime_max))

        return tuple(primes)

    def _get_encription_keys(self) -> Tuple[int, int, int]:
        primes = self._get_primes()

        product = primes[0]*primes[1]
        constant = self._random.randint(self._constant_min, self._constant_max)
        encrypt_product = constant*((primes[0]-1)*(primes[1]-1))+1
        factors = get_factors(encrypt_product)
        self._random.shuffle(factors)
        encrypt_key_1 = reduce(operator.mul, factors[:len(factors)//2], 1)
        encrypt_key_2 = encrypt_product//encrypt_key_1

        return encrypt_key_1, encrypt_key_2, product

    def get_encrypters(self) -> Tuple[Encrypter, Decrypter]:
        public_key, private_key, product = self._get_encription_keys()
        return Encrypter(public_key, product), Decrypter(private_key, product)
