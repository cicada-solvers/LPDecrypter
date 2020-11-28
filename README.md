# LPDecrypter

A Python framework to work with the Liber Primus decryption.

## Usage
There are examples in `examples`, but indeed more documentation is needed.

## Contributing
Obviously all contributions are welcome, here are some guidelines:
- if you implement some cipher to test it on LiberPrimus you may as well add it to this repository via a pull request. Name the class like `YourNickname_SomeNameThatDescribesTheCipherCipher` like if i implemented some modified Vigenere cipher that uses the mobius function i would name it `Ekardnam_MobiusVigenereCipher`, put its code in `lpdecrypter/ciphers/yournickname_ciphers.py` and export it in `lpdecrypter/ciphers/__init__.py`.
- as above if you implemented some alphabets follow the same convention. An example would be `Ekardnam_GematriaPrimus`, and put in `lpdecrypter/alphabets/yournickname_alphabets.py` and export it in `lpdecrypter/alphabets/__init__.py`.
- same pattern if you implement custom analyzers
- to avoid having to many files try to put all your alphabets and cipher implementation in one file for each category named as described above, but if you really implement a lot of stuff split it in multiple files with your nick name prepended.
- the above rules aren't valid if you implement some kind of famous cipher, alphabet or analyzer. If i implemented the railfence cipher I would name it `RailfenceCipher` and put it in a file named `railfence_cipher.py` in the corresponding folder. In fact the prepositions of nicknames has the purpose to avoid complex identifiers for very specific ciphers and to give some kind of namespacing to the ciphers, which isn't needed for ciphers (or anything else) that have a globally understood name (and would actually make the class names look bad)

Check the [issues](https://github.com/ekardnam/LPDecrypter/issues) or the [not yet implemented features](https://github.com/ekardnam/LPDecrypter/search?q=%23+NOT+YET+IMPLEMENTED).
