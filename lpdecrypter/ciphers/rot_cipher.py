from .cipher import Cipher

from ..benchmarking import profile


class RotCipher(Cipher):
    """
        The ROT(N) cipher
    """
    def __init__(self, rotations, modulo):
        self.rotations = rotations
        self.modulo = modulo

    @profile
    def encrypt(self, data):
        return [(value + self.rotations) % self.modulo for value in data]

    @profile
    def decrypt(self, data):
        return [(value - self.rotations) % self.modulo for value in data]
