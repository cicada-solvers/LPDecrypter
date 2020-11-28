
from .analyzer import Analyzer

import matplotlib.pyplot as plt
import numpy as np

from ..benchmarking import profile

class BigramAnalyzer(Analyzer):
    """
        Basic bigram frequency analysis
    """
    def __init__(self, alphabet, is_range_from_zero=True, use_decoded_values=True):
        """
            Creates a BigramAnalyzer
                alphabet is the alphabet to use
                is_range_from_zero is True if the encoding space is range(0, n)
        """
        self.alphabet = alphabet
        self.N = alphabet.get_encoding_space_cardinality()
        self.alphabet_str = alphabet.decode(alphabet.get_encoding_space())
        self.is_range_from_zero = is_range_from_zero
        self.use_decoded_values = use_decoded_values
        if not is_range_from_zero:
            # NOT YET IMPLEMENTED
            raise Exception('In future implementation alphabet could also have an encoding space that isnt like range(0, n)')
            # basically this is handled by creating a 1-1 mapping from range(0, alphabet.get_encoding_space_cardinality()) to the encoding space

    @profile
    def analyze(self, data):
        data = self.alphabet.encode_words(data.split(' '))
        if not self.is_range_from_zero:
            # here we should map data into range(0, self.N)
            # NOT YET IMPLEMENTED
            raise Exception('In future implementation alphabet could also have an encoding space that isnt like range(0, n)')
        frequencies = np.zeros((self.N, self.N), dtype=int)
        for word in data:
            for i in range(0, len(word) - 1):
                x = word[i]
                y = word[i+1]
                frequencies[y, x] += 1
        return frequencies

    def display(self, frequencies, display_method='plot'):
        if display_method == 'plot':
            plt.figure()
            plt.imshow(frequencies)
            plt.xlabel('First letter')
            plt.ylabel('Second letter')
            if self.use_decoded_values:
                plt.xticks(range(self.N), self.alphabet_str)
                plt.yticks(range(self.N), self.alphabet_str)
            else:
                plt.xticks(range(self.N), self.alphabet.get_encoding_space())
                plt.yticks(range(self.N), self.alphabet.get_encoding_space())
            for x in range(self.N):
                for y in range(self.N):
                    plt.annotate(str(frequencies[y][x]), xy=(x, y), horizontalalignment='center', verticalalignment='center')
            plt.show()
        elif display_method == 'text':
            print(frequencies)
        else:
            raise ValueError('Unknown display method')
