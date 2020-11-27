from .alphabet import Alphabet

_english_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y', 'Z']
_letter_to_value = {letter: i for i, letter in enumerate(_english_letters)}

def _sanitize_english(text):
    return [letter for letter in text.upper() if letter in _english_letters]

class EnglishAlphabet(Alphabet):
    """
        The regular english alphabet
    """

    def encode(self, text):
        return [_letter_to_value[letter] for letter in _sanitize_english(text)]

    def decode(self, encoded):
        return ''.join([_english_letters[value] for value in encoded])

    def get_encoding_space(self):
        return list(range(0, 26))

    def get_encoding_space_cardinality(self):
        return 26
