from .cipher import Cipher

class SubstitutionCipher(Cipher):
    """
        The monoalphabetic substitution cipher
    """
    def __init__(self, permutation):
        self.permutation = permutation
        if isinstance(permutation, dict):
            self.inverse_permutation = {v: k for k, v in permutation.items()}
        elif isinstance(permutation, list):
            self.inverse_permutation = {v: i for i, v in enumerate(permutation)}
        else:
            raise TypeError('Permutation should be list or dict')

    def encrypt(self, data):
        return [self.permutation[value] for value in data]

    def decrypt(self, data):
        return [self.inverse_permutation[value] for value in data]
