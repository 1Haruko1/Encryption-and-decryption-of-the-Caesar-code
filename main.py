def ceasar_code(text, shift, mode):

    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    russian_alphabet_upper = russian_alphabet.upper()
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    english_alphabet_upper = english_alphabet.upper()
    result = ''

    if mode == 'encode':
        for symbol in text:
            if symbol == symbol.upper():
                if symbol in russian_alphabet_upper:
                    index_symbol = russian_alphabet_upper.index(symbol)
                    result += russian_alphabet_upper[index_symbol + shift]
                elif symbol in english_alphabet_upper:
                    index_symbol = english_alphabet_upper.index(symbol)
                    result += english_alphabet_upper[index_symbol + shift]
                else:
                    result += symbol
            else:
                if symbol in russian_alphabet:
                    index_symbol = russian_alphabet.index(symbol)
                    result += russian_alphabet[index_symbol + shift]
                elif symbol in english_alphabet:
                    index_symbol = english_alphabet.index(symbol)
                    result += english_alphabet[index_symbol + shift]
                else:
                    result += symbol
    elif mode == 'decode':
        for symbol in text:
            if symbol == symbol.upper():
                if symbol in russian_alphabet_upper:
                    index_symbol = russian_alphabet_upper.index(symbol)
                    result += russian_alphabet_upper[index_symbol - shift]
                elif symbol in english_alphabet_upper:
                    index_symbol = english_alphabet_upper.index(symbol)
                    result += english_alphabet_upper[index_symbol - shift]
                else:
                    result += symbol
            else:
                if symbol in russian_alphabet:
                    index_symbol = russian_alphabet.index(symbol)
                    result += russian_alphabet[index_symbol - shift]
                elif symbol in english_alphabet:
                    index_symbol = english_alphabet.index(symbol)
                    result += english_alphabet[index_symbol - shift]
                else:
                    result += symbol
    return result


encode = ceasar_code('Привет, World1234$$%', 2, 'encode') # return --> Сткджф, Yqtnf1234$$% 
decode = ceasar_code(encode, 2, 'decode') # return --> Привет, World1234$$%

print(f'ШИФРОВКА: {encode}')
print(f'ДЕШИФРОВКА: {decode}')
