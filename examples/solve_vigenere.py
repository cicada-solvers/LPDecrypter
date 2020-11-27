import sys
sys.path.insert(0, '.')

runes = """ᚢᛠᛝᛋᛇᚠᚳ.ᚱᛇᚢᚷᛈᛠᛠ-ᚠᚹᛉ
ᛏᚳᛚᛠ-ᚣᛗ-ᛠᛇ-ᛏᚳᚾᚫ-ᛝᛗᛡ
ᛡᛗᛗᚹ-ᚫᛈᛞᛝᛡᚱ-ᚩᛠ-ᛡᛗᛁ-ᚠᚠ-
ᛖᚢᛝ-ᛇᚢᚫ.ᚣᛈ-ᚱᚫ-ᛁᛈᚫ-ᚳᚫ-ᚫᚾᚹ-ᛒᛉᛗᛞ
-ᚱᛡᛁ-ᚠᛈᚳ-ᛇᛇᚫᚳ-ᚱᚦᛈ-ᚠᛄᛗᚩ-ᛇᚳᚹᛡ-ᛒᚫᚹ-
ᛒᛠᛚᛋ-ᚱᚣ-ᛄᚫ-ᚱ-ᛗᚳᚦᛇᚫᛏᚳᛈᚹ-ᛗᚷᛇ.ᚳ
ᛝᛈᚢ-ᛇᚳ-ᚱᛖᚹ-ᛡᛈᛁ-ᛒᚣᛒᛉ-ᚠᛚᛁᚱ-ᚱᛗ-ᚳᚷ
ᛒ-ᚣᚱ-ᚳᚠᚢ-ᚦᛈᛡᛄᚹᛏᚠᛠ-ᛄᚷᛒ-ᚫᚦᚠᚠᛠ
ᛈᚦ-ᛈᚠᚪᛉ-ᛄᛗᛖᛈᛝᛋᚩᛋᛗ-ᚹᛇᛄᛚ-ᚹᛉᚢᚦ
ᚫᚹᛗᚦ-ᛞᚣᛄᚳ-ᛋᛡᛉᚩᛝᚱᛗᛒᚹ-ᚱᛗᛁ-ᛞᚣᛄ
ᚳ-ᛉᚻᚢᚣᛈᛚ.ᛄᛝᚣᛗᚠᛄᛈᛇᚢᛡ-ᚹᛇᛄ-ᛞ
ᚹᛉᚢ-ᚪᛚᚪᛋᛗᛡᛇᛉ-ᚫᛗ-ᛡᛗᛁ-ᛈᚣ-ᚫᛗᚢᚠ
.ᛗᚣ-ᚣᛇ-ᚫᛉᚱᛄᛋᛖ-ᛖᚹᚾ-ᛞᛄᚢᛋᛉᚣᛏ
ᛖᛏᛗ-ᛇᚱᚣ-ᛞᛋ-ᚾᛖᚫᛞᛡ-ᛈᛒᚢᚾᛠᛝᛄᛡ
ᚫ-ᛄᚷᛒ-ᛈᚦᛉ-ᛈᚾᚹᚹᛁᛚᛗᚫ.ᛚᛈᛒᚢᚩᛠᛡ-ᚱ
ᛡᛠᚠ-ᚱᚱᛇᛄᛗ-ᚱᛗᛁ-ᛞᚣᛄ-ᚻᛚᚠᚢ-ᛄᚢᛡᛚᚦ
ᛠ-ᛇᛄᚩᛇᚱᚱᛗ.ᚢᛗᛋᚳ-ᛠᛇ-ᛚᛁᚫᚫᚳᛚ-ᚹᛁ-ᛚ
ᛏ-ᛈᛖᚢᛈ-ᛠᛡᛈᚦᛏᛒ-ᛏᛗᛖ-ᚢᛚᚩᛚᛖ-ᛇᛄ
ᛈ-ᚢᛠ-ᛚᚳᚷ-ᛠᚷᛋᛡᛏᛗ.
ᛒᛗᚱᚦᚠᛈ.ᚹᚱᛄ-ᚱᛉᚳ-ᛝ-ᛄᛠᛟ-ᛄᛖ
ᚣᛗ-ᛞᚣᛄᚳᚫᛡᚢᚠ.ᛈᚠᚪ-ᚳᚳᛠ-ᚱ-
ᚢᛄᚱ-ᚪᛗᛒᛈ-ᚷᛈᛒᚢᚾᛠᛝᚠ.ᚾᛉᛖ-
ᚣᚷᛁᛠᛝᚢᛗᛏᚳᚷᛠᛠ-ᛄᚫ-ᛒᛈᚹᛞ.ᚠᚣ
ᛉ-ᚫᚢᚠ-ᛇᛄᛈ-ᛉᛚᚦᛠᚪ-ᛚᚦ-ᚳᚣᚢᛡ.
ᚳᛖ-ᛚᚫᛇᛁᛉᚦᛋᚫᚻᚫ-ᚦᚣᚠᛚᚳᛖᚱ-ᛈᚠᚪᛉ-ᚱᛒᛖ-ᚫᚳᛒᚠ.""".replace('.', '-').split('-')

from lpdecrypter.alphabets import GematriaPrimus
from lpdecrypter.ciphers import VigenereWithInterruptersCipher
from lpdecrypter.liberprimus import runes_to_latin, latin_to_runes

if __name__ == '__main__':
    gp = GematriaPrimus()
    encoded = gp.encode_words(runes)
    key = gp.encode(latin_to_runes('DIVINITY'))
    vigenere = VigenereWithInterruptersCipher(key, [48, 74, 84], 29) # add all the interrupters
    decrypted = vigenere.decrypt_words(encoded)
    decrypted = gp.decode_words(decrypted)
    print(runes_to_latin(' '.join(decrypted)))
