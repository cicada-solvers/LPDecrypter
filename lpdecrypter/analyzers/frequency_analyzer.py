
from .analyzer import Analyzer

import matplotlib.pyplot as plt

class FrequencyAnalyzer(Analyzer):
    """
        Basic frequency analysis
    """
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def analyze(self, data):
        data = self.alphabet.encode(data)
        frequencies = {value: 0 for value in self.alphabet.get_encoding_space()}
        for value in data:
            if value in frequencies:
                frequencies[value] += 1
        return {self.alphabet.decode([value]): frequency for value, frequency in frequencies.items()}

    def display(self, frequencies, display_method='plot'):
        if display_method == 'plot':
            plt.figure()
            plt.bar(frequencies.keys(), frequencies.values())
            plt.show()
        elif display_method == 'text':
            print(frequencies)
        else:
            raise ValueError('Unknown display method')
