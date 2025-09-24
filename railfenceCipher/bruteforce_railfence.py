
def filling_the_grid(plaintext, grid, cols, key):
    
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
    return grid, cols


def decryption(encrypted_text, key):
    decrypted = ""
    grid, cols = make_empty_grid(len(encrypted_text),key)
    grid = filling_the_grid(encrypted_text, grid, cols, key)
    
    


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

    
    # now we have to read the grid diagonally
    col=0
    row=0
    flag = True
    while col < cols:
        while col < cols:
            if(col<len(encrypted_text)):
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



encrypted_text = input("Enter the encrypted text: ")


for i in range(2,len(encrypted_text)):
    decrypted = decryption(encrypted_text, i)
    print("encrypted with key: ", i , " " ,decrypted)
    ask = int(input("Is the decryption menaningful ? (1/0)"))
    if(ask == 0):
        continue
    else:
        break


