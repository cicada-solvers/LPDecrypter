
from .alphabet import Alphabet

from ..liberprimus.gematria import *

def _sanitize_runes(runes):
    """
        Removes non runic characters from a rune string
    """
    return ''.join([rune for rune in runes if rune in value_to_rune + ['ᛄ']])

class GematriaPrimus(Alphabet):
    """
        The Gematria Primus runic alphabet
    """

    def encode(self, text):
        """
            Encodes text, which should be a string of runic characters, into they're
            decimal representation in gematria
        """
        return [rune_to_value[rune] for rune in _sanitize_runes(text)]

    def decode(self, encoded):
        """
            Decodes a list of integer representation of runic characters back into runes
        """
        return ''.join(value_to_rune[value] for value in encoded)

    def get_encoding_space(self):
        return list(range(0, 29))

    def get_encoding_space_cardinality(self):
        return 29

class ReverseGematriaPrimus(Alphabet):
    """
        The reverse Gematria primus runic alphabet
    """

    def encode(self, text):
        """
            Encodes text, which should be a string of runic characters, into they're
            decimal representation in the reverse gematria
        """
        return [(28 - rune_to_value[rune]) for rune in _sanitize_runes(text)]

    def decode(self, encoded):
        """
            Decodes a list of integer representation of runic characters back into runes
        """
        return ''.join([value_to_rune[28 - value] for value in encoded])

    def get_encoding_space(self):
        return list(range(0, 29))

    def get_encoding_space_cardinality(self):
        return 29

class RotatedGematriaPrimus(Alphabet):
    """
        The reverse Gematria primus runic alphabet
    """
    def __init__(self, rotations):
        """
            Rotates the gematria primus runic alphabet by rotations
        """
        self.rotations = rotations

    def encode(self, text):
        """
            Encodes text, which should be a string of runic characters, into they're
            decimal representation in the reverse gematria
        """
        return [(rune_to_value[rune] + self.rotations) % 29 for rune in _sanitize_runes(text)]

    def decode(self, encoded):
        """
            Decodes a list of integer representation of runic characters back into runes
        """
        return ''.join([value_to_rune[(value - self.rotations) % 29] for value in encoded])

    def get_encoding_space(self):
        return list(range(0, 29))

    def get_encoding_space_cardinality(self):
        return 29
