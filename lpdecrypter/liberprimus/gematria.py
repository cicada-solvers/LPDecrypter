from ..benchmarking import profile

value_to_rune = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛂ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ',
         'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
value_to_latin = ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X',
                   'S', 'T', 'B', 'E', 'M', 'L', 'ING', 'OE', 'D', 'A', 'AE', 'Y', 'IA',
                   'EA']
value_to_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                     73, 79, 83, 89, 97, 101, 103, 107,
                     109]  # arbitrarily chosen common choices
rune_to_value = {rune: i for i, rune in enumerate(value_to_rune)}
rune_to_value['ᛄ'] = rune_to_value['ᛂ']
rune_to_latin = {rune: latin for rune, latin in zip(value_to_rune, value_to_latin)}
rune_to_latin['ᛄ'] = rune_to_latin['ᛂ']
rune_to_prime = {rune: prime for rune, prime in zip(value_to_rune, value_to_prime)}
rune_to_prime['ᛄ'] = rune_to_prime['ᛂ']

latin_to_value = {latin: i for i, latin in enumerate(value_to_latin)}
latin_to_rune = {latin: rune for latin, rune in zip(value_to_latin, value_to_rune)}
latin_to_rune['Z'] = latin_to_rune['S']
latin_to_rune['K'] = latin_to_rune['C']
latin_to_rune['V'] = latin_to_rune['U']
latin_to_rune['NG'] = latin_to_rune['ING']
latin_to_rune['IO'] = latin_to_rune['IA']
latin_to_prime = {latin: prime for latin, prime in zip(value_to_latin, value_to_prime)}

prime_to_value = {prime: i for i, prime in enumerate(value_to_prime)}
prime_to_rune = {prime: rune for prime, rune in zip(value_to_prime, value_to_rune)}
prime_to_latin = {prime: latin for prime, latin in zip(value_to_prime, value_to_latin)}

@profile
def runes_to_latin(runes):
    """
        Decodes runes back to latin
    """
    return ''.join([
        rune_to_latin[rune] if rune in rune_to_latin else rune for rune in runes
    ]) # the else handles spaces and commas and so on

def _iter_runes_from_latin(latins):
    i = 0
    while i < len(latins):
        if latins[i:i+3] in latin_to_rune:
            yield latin_to_rune[latins[i:i+3]]
            i += 3
        elif latins[i:i+2] in latin_to_rune:
            yield latin_to_rune[latins[i:i+2]]
            i += 2
        elif latins[i] in latin_to_rune:
            yield latin_to_rune[latins[i]]
            i += 1
        else:
            yield latins[i] # handle commas spaces and so on
            i += 1

@profile
def latin_to_runes(latin_fragments):
    """
        Decodes latin fragments back to runes
    """
    latins = latin_fragments.upper()
    latins = latins.replace('QU', 'KW')
    latins = latins.replace('Q', 'K')
    return ''.join(list(_iter_runes_from_latin(latins)))
