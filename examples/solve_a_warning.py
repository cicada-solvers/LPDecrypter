import sys
sys.path.insert(0, '.')

runes = """ᚱ-ᛝᚱᚪᛗᚹ.ᛄᛁᚻᛖᛁᛡᛁ-ᛗᚫᚣᚹ-ᛠᚪᚫᚾ-
ᚣᛖᛈ-ᛄᚫᚫᛞ.ᛁᛉᛞᛁᛋᛇ-ᛝᛚᚱᛇ-ᚦᚫᛡ
-ᛞᛗᚫᛝ-ᛇᚫ-ᛄᛁ-ᛇᚪᛡᛁ.ᛇᛁᛈᛇ-ᚣᛁ-ᛞ
ᛗᚫᛝᚻᛁᚳᛟᛁ.ᛠᛖᛗᚳ-ᚦᚫᛡᚪ-ᛇᚪᛡᚣ.ᛁᛉ
ᛋᛁᚪᛖᛁᛗᛞᛁ-ᚦᚫᛡᚪ-ᚳᚠᚣ.ᚳᚫ-ᛗᚫᛇ-ᛁᚳᛖᛇ-ᚫ
ᚪ-ᛞᛚᚱᚹᛁ-ᚣᛖᛈ-ᛄᚫᚫᛞ.ᚫᚪ-ᚣᛁ-ᚾᛁᛈᛈᚱᛟᛁ-
ᛞᚫᛗᛇᚱᛖᛗᛁᚳ-ᛝᛖᚣᛖᛗ.ᛁᛖᚣᛁᚪ-ᚣᛁ-ᛝᚫ
ᚪᚳᛈ-ᚫᚪ-ᚣᛁᛖᚪ-ᛗᛡᚾᛄᛁᚪᛈ.ᛠᚫᚪ-ᚱᚻᚻ-ᛖ
ᛈ-ᛈᚱᛞᚪᛁᚳ.""".replace('.', '-').split('-')

from lpdecrypter.alphabets import GematriaPrimus, ReverseGematriaPrimus
from lpdecrypter.liberprimus import runes_to_latin

if __name__ == '__main__':
    gp = GematriaPrimus()
    rev = ReverseGematriaPrimus()
    reverse_encoded = rev.encode_words(runes)
    print(reverse_encoded)
    decoded = gp.decode_list(reverse_encoded)
    print(decoded)
    print(runes_to_latin(' '.join(decoded)))
