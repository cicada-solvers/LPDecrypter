from .analyzer import Analyzer

import csv
import collections

import matplotlib.pyplot as plt
import numpy as np

from math import inf

TextScoreResult = collections.namedtuple(
    'TextScoreResult',
    [
        'total_score',
        'score_per_four_gram',
        'min_score_count',
        'four_gram_count',
        'rejected'
    ]
)

class MortlachScoringAnalyzer(Analyzer):
    """
        MortlachScoringAnalyzer analyzes plaintext (or what you think might be plaintext)
        and assigns a score to them.
        The original implementation for this is here: https://github.com/mortlach/lp-decrypter/blob/master/text_ranking/FourGramTextScore.py

        Basically it loads 4-gram probabilities from a CSV file formatted like this:
            4-gram, number of occurencies, log probability

        In the GitHub repository for this code under the folder data there is a file named
        4GramProbabilityData.csv which contains this values from project Guttenburg as
        computed by mortlach
    """
    def __init__(self, csv_file, min_score_per_four_gram, min_score_per_four_gram_offset, min_score=-inf, min_count=-inf):
        self.four_gram_probabilities = {}
        self.min_score = min_score
        self.min_count = min_count
        self.min_score_per_four_gram = min_score_per_four_gram
        self.min_score_per_four_gram_offset = min_score_per_four_gram_offset
        with open(csv_file, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            for four_gram, n, logp in reader:
                self.four_gram_probabilities[four_gram] = tuple([int(n), float(logp)])

    def __score_four_gram(self, four_gram):
        count, score = self.four_gram_probabilities.get(four_gram, (0, self.min_score))
        if count < self.min_count:
            return self.min_score
        return score

    def analyze(self, data):
        score = 0
        min_score_count = 0
        four_gram_count = len(data) - 3
        for i in range(0, four_gram_count):
            four_gram = data[i:i+4]
            four_gram_score = self.__score_four_gram(four_gram)
            if abs(four_gram_score - self.min_score) < 1e-4:
                min_score_count += 1
            score += four_gram_score
        rejected = score < self.min_score_per_four_gram * four_gram_count + self.min_score_per_four_gram_offset
        return TextScoreResult(round(score, 4), round(score / four_gram_count, 4), min_score_count, four_gram_count, rejected)

    def display(self, text_score_result, display_method='text'):
        if display_method == 'text':
            print(text_score_result)
        elif display_method == 'plot':
            plt.figure()
            plt.scatter([text_score_result.four_gram_count], [text_score_result.total_score], label='Scoring result')
            X = np.linspace(-10, 10) + text_score_result.four_gram_count
            Y = self.min_score_per_four_gram * X + self.min_score_per_four_gram_offset
            plt.plot(X, Y, color='red', label='Linear separation between classes')
            plt.legend()
            plt.xlabel('4-gram count')
            plt.ylabel('Score')
            plt.show()
        else:
            raise ValueError('Unknown display method')
