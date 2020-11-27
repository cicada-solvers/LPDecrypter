from .cipher import Cipher
from ..number_theory import is_prime, inverse_modulo

class AddedLambdaKeyCipher(Cipher):
    """
        A lamda key cipher is a cipher that encrypts by adding the key calculated from the lambda.
        Calculates the key using the lambda you pass it from the iteration number
    """
    def __init__(self, key_lambda, modulo):
        self.key_lambda = key_lambda
        self.modulo = modulo

    def encrypt(self, data):
        return [(value + self.key_lambda(i)) % self.modulo for i, value in enumerate(data)]

    def decrypt(self, data):
        return [(value - self.key_lambda(i)) % self.modulo for i, value in enumerate(data)]

    def encrypt_words(self, words):
        raise NotImplementedError('Do this')

    def decrypt_words(self, words):
        raise NotImplementedError('Do this')

class MultipliedLambdaKeyCipher(Cipher):
    """
        A lamda key cipher is a cipher that encrypts by multiplying the key calculated from the lambda.
        Calculates the key using the lambda you pass it from the iteration number
    """
    def __init__(self, key_lambda, modulo):
        if not is_prime(modulo):
            raise ValueError('Modulo needs to be prime')
        self.key_lambda = key_lambda
        self.modulo = modulo

    def encrypt(self, data):
        return [(value * self.key_lambda(i)) % self.modulo for i, value in enumerate(data)]

    def decrypt(self, data):
        return [(value * inverse_modulo(self.key_lambda(i), self.modulo)) % self.modulo for i, value in enumerate(data)]

    def encrypt_words(self, words):
        raise NotImplementedError('Do this')

    def decrypt_words(self, words):
        raise NotImplementedError('Do this')
