
class Alphabet(object):
    """
        An Alphabet describes how characters or tokens should be encoded and decoded
        to integers before they're passed to a cipher for processing
    """

    def encode(self, text):
        """
            Encodes a string of characters into a list of integer values
            or possibly a single integer value
        """
        pass

    def decode(self, encoded):
        """
            Decodes what has been encoded with encode back into text
        """
        pass

    def encode_words(self, words):
        """
            Encodes a list of words
        """
        return [self.encode(word) for word in words]

    def decode_words(self, words):
        """
            Decodes a list of encoded values back into a list of words
        """
        return [self.decode(word) for word in words]
