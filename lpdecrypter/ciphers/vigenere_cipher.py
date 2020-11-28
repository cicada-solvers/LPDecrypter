from .cipher import Cipher
from ..number_theory import is_prime, inverse_modulo_or_zero

from ..benchmarking import profile

class VigenereCipher(Cipher):
    """
        The Viginere cipher
    """
    def __init__(self, key, modulo):
        self.key = key
        self.key_len = len(key)
        self.modulo = modulo

    def __encrypt_value(self, value, key):
        return (value + key) % self.modulo

    @profile
    def encrypt(self, data):
        return [self.__encrypt_value(value, self.key[i % self.key_len]) for i, value in enumerate(data)]

    @profile
    def decrypt(self, data):
        return [self.__encrypt_value(value, -self.key[i % self.key_len]) for i, value in enumerate(data)]

    @profile
    def encrypt_words(self, words):
        i = 0
        result = []
        for word in words:
            encrypted = []
            for value in word:
                encrypted.append(self.__encrypt_value(value, self.key[i % self.key_len]))
                i += 1
            result.append(encrypted)
        return result

    @profile
    def decrypt_words(self, words):
        i = 0
        result = []
        for word in words:
            decrypted = []
            for value in word:
                decrypted.append(self.__encrypt_value(value, -self.key[i % self.key_len]))
                i += 1
            result.append(decrypted)
        return result

class VigenereWithInterruptersCipher(Cipher):
    """
        The Viginere cipher, with interrupters
    """
    def __init__(self, key, interrupters, modulo):
        self.key = key
        self.key_len = len(key)
        self.interrupters = interrupters
        self.modulo = modulo

    def __encrypt_value(self, value, key):
        return (value + key) % self.modulo

    @profile
    def encrypt(self, data):
        result = []
        key_index = 0
        for i, value in enumerate(data):
            if i in self.interrupters:
                result.append(value)
                continue
            result.append(self.__encrypt_value(value, self.key[key_index % self.key_len]))
            key_index += 1
        return result

    @profile
    def decrypt(self, data):
        result = []
        key_index = 0
        for i, value in enumerate(data):
            if i in self.interrupters:
                result.append(value)
                continue
            result.append(self.__encrypt_value(value, -self.key[key_index % self.key_len]))
            key_index += 1
        return result

    @profile
    def encrypt_words(self, words):
        i = 0
        key_index = 0
        result = []
        for word in words:
            encrypted = []
            for value in word:
                if i in self.interrupters:
                    encrypted.append(value)
                else:
                    encrypted.append(self.__encrypt_value(value, self.key[key_index % self.key_len]))
                    key_index += 1
                i += 1
            result.append(encrypted)
        return result

    @profile
    def decrypt_words(self, words):
        i = 0
        key_index = 0
        result = []
        for word in words:
            decrypted = []
            for value in word:
                if i in self.interrupters:
                    decrypted.append(value)
                else:
                    decrypted.append(self.__encrypt_value(value, -self.key[key_index % self.key_len]))
                    key_index += 1
                i += 1
            result.append(decrypted)
        return result
