from .cipher import Cipher
from ..number_theory import is_prime, inverse_modulo_or_zero

from ..benchmarking import profile

class AddedLambdaKeyCipher(Cipher):
    """
        A lamda key cipher is a cipher that encrypts by adding the key calculated from the lambda.
        Calculates the key using the lambda you pass it from the iteration number
    """
    def __init__(self, key_lambda, modulo):
        self.key_lambda = key_lambda
        self.modulo = modulo

    @profile
    def encrypt(self, data):
        return [(value + self.key_lambda(i)) % self.modulo for i, value in enumerate(data)]

    @profile
    def decrypt(self, data):
        return [(value - self.key_lambda(i)) % self.modulo for i, value in enumerate(data)]

    @profile
    def encrypt_words(self, words):
        # NOT YET IMPLEMENTED
        raise Exception('Do this')

    @profile
    def decrypt_words(self, words):
        # NOT YET IMPLEMENTED
        raise Exception('Do this')
