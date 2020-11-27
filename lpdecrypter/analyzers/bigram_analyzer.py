
from .analyzer import Analyzer

import matplotlib.pyplot as plt
import numpy as np

class BigramAnalyzer(Analyzer):
    """
        Basic bigram frequency analysis
    """
    def __init__(self, alphabet, is_range_from_zero=True):
        """
            Creates a BigramAnalyzer
            alphabet is the alphabet to use
            is_range_from_zero is True if the encoding space is range(0, n)
        """
        self.alphabet = alphabet
        self.N = alphabet.get_encoding_space_cardinality()
        self.alphabet_str = alphabet.decode(alphabet.get_encoding_space())
        self.is_range_from_zero = is_range_from_zero
        if not is_range_from_zero:
            raise NotImplementedError('In future implementation alphabet could also have an encoding space that isnt like range(0, n)')
            # basically this is handled by creating a 1-1 mapping from range(0, alphabet.get_encoding_space_cardinality()) to the encoding space

    def analyze(self, data):
        data = self.alphabet.encode_words(data.split(' '))
        if not self.is_range_from_zero:
            # here we should map data into range(0, self.N)
            raise NotImplementedError('In future implementation alphabet could also have an encoding space that isnt like range(0, n)')
        frequencies = np.zeros((self.N, self.N), dtype=int)
        for word in data:
            for i in range(0, len(word) - 1):
                x = word[i]
                y = word[i+1]
                frequencies[x, y] += 1
        return frequencies

    def display(self, frequencies, display_method='plot'):
        if display_method == 'plot':
            plt.figure()
            plt.imshow(frequencies)
            plt.xticks(range(self.N), self.alphabet_str)
            plt.yticks(range(self.N), self.alphabet_str)
            for x in range(self.N):
                for y in range(self.N):
                    plt.annotate(str(frequencies[x][y]), xy=(x, y), horizontalalignment='center', verticalalignment='center')
            plt.show()
        elif display_method == 'text':
            print(frequencies)
        else:
            raise ValueError('Unknown display method')
