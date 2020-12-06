import sys
sys.path.insert(0, '.')

from lpdecrypter.liberprimus import get_section
from lpdecrypter.statistics import FrequencyDistribution


if __name__ == '__main__':
    for i in range(0, 13):
        section = get_section(i)
        words = section['all_words']
        lenghts = [len(word) for word in words]
        distribution = FrequencyDistribution.from_list(lenghts, f'Word lenght distribution for section {section["page_number_start"]}-{section["page_number_end"]}', xlabel='Word length', ylabel='Frequency')
        print(f'Word lenght distribution for section {section["page_number_start"]}-{section["page_number_end"]}')
        print(distribution.entries)
        distribution.plot()
        distribution.write_to_file(f'out/section{i+1}.json')
