from .prime_table import prime_table, prime_set, prime_table_len, prime_table_max

def is_prime(n):
    if n < prime_table_max:
        # in this case do a binary search in the table to see
        # if there is n
        return n in prime_set
    raise NotImplementedError('Really need to find a good library for primes')

def prime(n):
    if n < prime_table_len:
        return prime_table[n]
    raise NotImplementedError('Really need to find a good library for primes')

def inverse_modulo(n, mod):
    return pow(n, -1, mod)

def inverse_modulo_or_zero(n, mod):
    if n == 0:
        return 0
    return inverse_modulo(n, mod)
