import re
import sys
# playfence cipher
unprocessed_plaintext = input("Enter the plaintext to encrypt: ").strip().replace(" ","")
plaintext = re.sub(r'[^a-zA-Z]', '', unprocessed_plaintext)
key = int(input("Enter the key(integer): "))

def filling_the_grid(plaintext, grid, cols, encryption = True):
    
    # if encryption is set false then 
    if not encryption:
        col=0
        row=0
        flag = True
        while col < cols:
            while col < cols:
                if(col<len(plaintext)):
                    grid[row][col] = '@'
                else:
                    grid[row][col] = '@'
                if ( row == key-1):
                    flag = False
                elif ( row == 0 ):
                    flag = True
                if(flag):
                    row+=1
                else:
                    row-=1
                col+=1
        
        return grid

    col=0
    row=0
    flag = True

    while col < cols:
        while col < cols:
            if(col<len(plaintext)):
                grid[row][col] = plaintext[col]
            else:
                grid[row][col] = 'X'
            if ( row == key-1):
                flag = False
            elif ( row == 0 ):
                flag = True
            if(flag):
                row+=1
            else:
                row-=1
            col+=1

    return grid

def make_empty_grid(length, key):
    # make the grid of key rows
    # for number of cols of the gridwe will have to find the next multiple of the key

    cols = 0
    i=length
    while True:
        if(i%key == 0):
            cols = i
            break
        else:
            i+=1

    grid = [[0 for _ in range(cols)] for _ in range(key)]

    col=0
    row=0
    flag = True

    while col < cols:
        while col < cols:
            if(col<len(plaintext)):
                grid[row][col] = plaintext[col]
            else:
                grid[row][col] = 'X'
            if ( row == key-1):
                flag = False
            elif ( row == 0 ):
                flag = True
            if(flag):
                row+=1
            else:
                row-=1
            col+=1

    return grid, cols



def encryption(plaintext, key):
    # verify the key
    if(key < 2 or key >= len(plaintext)/2):
        print("Invalid key entered.")
        sys.exit()

    # make the grid of key rows
    empty_grid, cols = make_empty_grid(len(plaintext), key)
    grid = filling_the_grid(plaintext, empty_grid, cols)
    # printing the grid
    for row in grid:
        for col in row: 
            print(col, end=" ")
        print(end="\n")
        
    encrypted = ""
    # now we will read the encrypted text
    for row in grid:
        for col in row:
            if(col != 0):
                encrypted += col

    print("encrypted text: ", encrypted)
    return encrypted


def decryption(encrypted_text, key):
    decrypted = ""
    grid, cols = make_empty_grid(len(encrypted_text),key)
    grid = filling_the_grid(encrypted_text, grid, cols, False)

    traverse = 0
    # now wherever the @ symbol is in the grid we will replace it with the encrupted text character one by one
    for i in range(key):
        for j in range(cols):
            if grid[i][j] == '@':
                if(traverse<len(encrypted_text)):
                    grid[i][j] = encrypted_text[traverse]
                    traverse+=1
                else:
                    grid[i][j] = ""

    for row in grid:
        for col in row:
            print(col, end=" ")
        print("\n")
    
    # now we have to read the grid diagonally
    col=0
    row=0
    flag = True
    while col < cols:
        while col < cols:
            if(col<len(plaintext)):
                decrypted += grid[row][col]
            if ( row == key-1):
                flag = False
            elif ( row == 0 ):
                flag = True
            if(flag):
                row+=1
            else:
                row-=1
            col+=1


    return decrypted


print(encryption(plaintext, key))
encrypted_text = input("Enter the encrypted text: ")
print(decryption(encrypted_text, key))