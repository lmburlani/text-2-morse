# Dicionario do código morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# função para encriptar a mensagem
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Verifica o dicionario e adiciona o correspondente
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 espaço indicada letras diferentes
            # e 2 indica palavras diferentes
            cipher += ' '
 
    return cipher
 
# Função para descriptografar 
def decrypt(message):
 
    # espaço extra
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        #  verifica por espaço
        if (letter != ' '):
 
            # contador para seguir os espaços
            i = 0
 
            # armazenamento do código morse
            citext += letter
 
        # em caso de espaço
        else:
            # if i = 1 indica nova letra
            i += 1
 
            # if i = 2 indica nova palavra
            if i == 2 :
 
                 # adiciona espaço em palavras separadas
                decipher += ' '
            else:
 
                # acessa as chaves usando seus valores 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher
 
# Função para rodar o programa
def main():
    message = input()
    result = encrypt(message.upper())
    print (result)
 
    
    result = decrypt(message)
    print (result)
 
# Executa o main
if __name__ == '__main__':
    main()
