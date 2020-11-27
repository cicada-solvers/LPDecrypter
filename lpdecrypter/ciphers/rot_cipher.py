
from .cipher import Cipher

class RotCipher(Cipher):
    """
        The ROT(N) cipher
    """
    def __init__(self, rotations, modulo):
        self.rotations = rotations
        self.modulo = modulo

    def encrypt(self, data):
        return [(value + self.rotations) % self.modulo for value in data]

    def decrypt(self, data):
        return [(value - self.rotations) % self.modulo for value in data]
