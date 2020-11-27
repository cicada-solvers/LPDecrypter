
class Cipher(object):
    """
        A Cipher is a class that describes how to encrypt and decrypt some input based on
        a key
    """

    def encrypt(self, data):
        """
            Encrypts data
        """
        pass

    def decrypt(self, data):
        """
            Decrypts data
        """
        pass

    def encrypt_words(self, words):
        return [self.encrypt(word) for word in words]

    def decrypt_words(self, words):
        return [self.decrypt(word) for word in words]
