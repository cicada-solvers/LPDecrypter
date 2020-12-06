import sys
sys.path.insert(0, '.')

import os
from lpdecrypter.statistics import FrequencyDistribution

if __name__ == '__main__':
    for filename in os.listdir(sys.argv[1]):
        with open(os.path.join(sys.argv[1], filename), 'r', encoding='utf8') as f:
            words = f.read().split(' ')
        lenghts = [len(word) for word in words]
        distribution = FrequencyDistribution.from_list(lenghts, f'Word lenght distribution for file {filename}', xlabel='Word length', ylabel='Frequency')
        print(f'Word lenght distribution for file {filename}')
        print(distribution.entries)
        distribution.write_to_file(f'out/freq{filename}.json')
