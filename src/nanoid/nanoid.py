from os import urandom
from math import ceil, log


class NanoID:
    def __init__(self, alphabet: int = None, size: int = None, prefix: str = None):
        self._prefix = prefix
        self._alphabet = alphabet if alphabet else '_-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self._size = size if size else 21

    def generate(self) -> str:
        alphabet_len = len(self._alphabet)
        
        mask = 1
        if alphabet_len > 1:
            mask = (2 << int(ceil(log(alphabet_len) / log(2)))) - 1
        step = int(ceil(1.6 * mask * self._size / alphabet_len))

        id = ''
        while True:
            for random_byte in bytearray(urandom(step)):
                random_byte = random_byte & mask
                if random_byte < alphabet_len and random_byte >= 0:
                    id += self._alphabet[random_byte]
                    if len(id) == self._size:
                        if self._prefix:
                            return f'{self._prefix}_{id}'
                        else:
                            return id
