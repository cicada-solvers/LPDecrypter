from .prime_table import prime_table, prime_set, prime_table_len, prime_table_max

from ..benchmarking import profile

@profile
def is_prime(n):
    if n < prime_table_max:
        # in this case do a binary search in the table to see
        # if there is n
        return n in prime_set
    # NOT YET IMPLEMENTED
    raise Exception('Really need to find a good library for primes')

@profile
def prime(n):
    if n < prime_table_len:
        return prime_table[n]
    # NOT YET IMPLEMENTED
    raise Exception('Really need to find a good library for primes')

@profile
def inverse_modulo(n, mod):
    return pow(n, -1, mod)

@profile
def inverse_modulo_or_zero(n, mod):
    if n == 0:
        return 0
    return inverse_modulo(n, mod)
