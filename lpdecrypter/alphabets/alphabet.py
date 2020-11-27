
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

    def get_encoding_space(self):
        """
            Returns a list of possible encoding values
        """
        pass

    def get_encoding_space_cardinality(self):
        """
            Returns the encoding space caridnality
        """
        return len(self.get_encoding_space())

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
