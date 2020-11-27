import sys
sys.path.insert(0, '.')

from lpdecrypter.analyzers import BigramAnalyzer
from lpdecrypter.alphabets import GematriaPrimus
from lpdecrypter.liberprimus import get_section_words

if __name__ == '__main__':
    all_section_words = get_section_words(0)
    for i in range(1, 13):
        all_section_words += get_section_words(i)
    sec = ' '.join(all_section_words)
    gp = GematriaPrimus()
    bigrams = BigramAnalyzer(gp)
    result = bigrams.analyze(sec)
    bigrams.display(result)
