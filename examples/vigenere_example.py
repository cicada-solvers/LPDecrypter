import sys
sys.path.insert(0, '.')

# using vigenere with english

from lpdecrypter.ciphers import VigenereCipher
from lpdecrypter.alphabets import EnglishAlphabet

if __name__ == '__main__':
    eng = EnglishAlphabet()
    key = eng.encode('lemon')
    cleartext = eng.encode_words('attack at dawn'.split(' '))
    vigenere = VigenereCipher(key, 26)
    ciphertext = vigenere.encrypt_words(cleartext)
    print(eng.decode_words(ciphertext))
    print(eng.decode_words(vigenere.decrypt_words(ciphertext)))
