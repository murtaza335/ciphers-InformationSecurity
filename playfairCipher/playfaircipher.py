# u have a string
# break it into pairs (follow the rules)
# rules:
# if the number of characters are odd then add bogus letter to the end lets say 'X'
# u cannot make a pair f the same letters, add bogus letter to each of them


# now we have the splitted string
# encrytion: rules
# if in the same column then both immediate letters after that
# if in the same row then both immediate letters below that
# if neither of the above condition then we will make the cross from both letters to find two letters.
import string
key = 'explanation'.replace('J', 'I').upper()
# removing duplicates from the key
key_unique = list(dict.fromkeys(key))

plain_text = 'Information security is a "MUST" to learn.'
plain_text = plain_text.translate(str.maketrans('', '', string.punctuation))
print(plain_text)

ciphertext = ''
alphabets = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def checkIfInMatrix(letter):
    if letter == 'J':
        letter = 'I'
    for row in matrix:
        if letter in row:
            return True
    return False

bogus_letter = 'X'
matrix = [['']*5 for i in range(5)]



def fillTheMatrix():
    key_index = 0
    alphabet_index = 0
    for i in range(5):
        for j in range(5):
            # ensures that the key is not completed
            if(key_index < len(key_unique)):
                matrix[i][j] = key_unique[key_index]
                key_index += 1

            # if the key is completed in the matrix then we have to fill other alphabets
            else:
                # only fill those letters that are not in the key_unique
                if checkIfInMatrix(alphabets[alphabet_index]):
                    alphabet_index += 1
                    
                    while True:
                        if checkIfInMatrix(alphabets[alphabet_index]):
                            alphabet_index +=1
                        else:
                            matrix[i][j] = alphabets[alphabet_index]
                            alphabet_index+=1
                            break
                else:
                    matrix[i][j] = alphabets[alphabet_index]
                    alphabet_index += 1
    
    for row in matrix:
        print(row)


def find_position(letter):
    if letter == 'J':
        letter = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j


def encryptMatrix():
    plain_text_no_spaces = plain_text.strip().replace(" ", "").replace("J", "I").upper()
    fillTheMatrix()

    # count the length of the string
    if len(plain_text_no_spaces) % 2 != 0:
        plain_text_no_spaces = plain_text_no_spaces+bogus_letter

    # now make pairs of two
    # pairs = [plain_text_no_spaces[i:i+2] for i in range(0, len(plain_text_no_spaces), 2)]
    pairs = list()
    encrypted = list()
    i=0
    while i<len(plain_text_no_spaces):
        if(i!=len(plain_text_no_spaces)-1):
            if plain_text_no_spaces[i] != plain_text_no_spaces[i+1]:
                pairs.append(plain_text_no_spaces[i:i+2])
                i+=2
            else:
                pairs.append(plain_text_no_spaces[i] + bogus_letter)
                i += 1
        else:
            pairs.append(plain_text_no_spaces[i]+bogus_letter)
            i+=1
    
    # now we have to encrypt these pairs using the matrix
    print("pairs: ", pairs)

    for element in pairs:
        row_char_1, col_char_1 = find_position(element[0])
        row_char_2, col_char_2 = find_position(element[1])
        
        if row_char_1 == row_char_2:
            encrypted.append(matrix[row_char_1][(col_char_1+1)%5] + matrix[row_char_2][(col_char_2+1)%5])
        elif col_char_1 == col_char_2:
            encrypted.append(matrix[(row_char_1+1)%5][col_char_1] + matrix[(row_char_2+1)%5][col_char_2])
        else:
            # first move through the row and then move through the column
            encrypted.append(matrix[row_char_1][col_char_2] + matrix[row_char_2][col_char_1])
    
    
    for pair in encrypted:
        print(pair,end="")

def decryptMatrix(cipher_text):
    cipher_text = cipher_text.strip().replace(" ", "").replace("J", "I").upper()
    fillTheMatrix()
    
    # making pairs
    pairs = [cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)]

    decrypted = []

    for element in pairs:
        row1, col1 = find_position(element[0])
        row2, col2 = find_position(element[1])

        if row1 == row2:
            decrypted.append(matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted.append(matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2])
        else:
            decrypted.append(matrix[row1][col2] + matrix[row2][col1])
    
    for pair in decrypted:
        print(pair, end="")

    

encryptMatrix()







        