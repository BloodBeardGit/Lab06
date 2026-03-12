alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + alphabet.upper()


def vigenere_header():
    print('|  ', end=' | ')
    for c in alphabet:
        print(c.upper(), end=' | ')
    print()
    print(f'{"|---" * (len(alphabet) + 1)}|')


def vigenere_sq():
    for i in range(len(alphabet)):
        j = i
        print('| ' + alphabet[j].upper(), end=' | ')
        for _ in range(len(alphabet)):
            j = j % len(alphabet)
            print(alphabet[j], end=' | ')
            j += 1
        print()


vigenere_header()
vigenere_sq()


def letter_to_index(letter: str, alphabet: str):
    if letter not in alphabet:
        raise ValueError ("Letter not in your alphabet, what are you a goof?")

    for i, c in enumerate(alphabet):
        if c == letter:
            return i
    return -1


def index_to_letter(index, alphabet):
    if not 0 <= index < len(alphabet):
        raise ValueError("Index is out of range, pack it up son")
    return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) +
            letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    for i, c in enumerate(plaintext):
        if c == ' ':
            cipher_text += ' '
        elif c.upper() in alphabet:
            cipher_text += index_to_letter(
                vigenere_index(key[i % len(key)].upper(), c.upper(), alphabet),
                alphabet
            )
    return cipher_text


key = 'ThisIsMyEagle'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = "ThisIsMyTaunt"
print(encrypt_vigenere(key, message, alphabet))