board = [
    [2, 2, 0,  3, 0, 0,  0, 0, 0],
    [8, 0, 4,  0, 6, 2,  0, 0, 3],
    [0, 1, 3,  8, 0, 0,  2, 0, 0],

    [0, 0, 0,  0, 2, 0,  3, 9, 0],
    [5, 0, 7,  0, 0, 0,  6, 2, 1],
    [0, 3, 2,  0, 0, 6,  0, 0, 0],

    [0, 2, 0,  0, 0, 9,  1, 4, 0],
    [6, 0, 1,  2, 5, 0,  8, 0, 9],
    [0, 0, 0,  0, 0, 1,  0, 0, 2]
]   


def main() -> bool:
    """The base program"""
    
    # check once for any obviously wrong inputs (2 same numbers in row, col, square)
    if not valid_input():
        print("Puzzle unsolvable")
        print("!!!")
        exit()
    
    row, col = find_next_empty()   # pick a location to experiment with
    
    if row is None:   
        return True
    
    # generate a guess in the location determined in find_next_empty(board)
    for guess in range(1,10):
        if is_valid(guess, row, col):
            board[row][col] = guess
            
            if main():   # recursive call
                return True
        
        # if not valid, reset    
        board[row][col] = 0
    
    return False

def valid_input() -> bool:
    """Loops through the initial board to make sure input is valid"""
    
    # check row for duplicates
    for r in range(9):
        inrow: List = []
        for c in range(9):
            elem = board[r][c]
            if elem in inrow and elem != 0:
                print("!!!")
                print(f"{elem} appears more than once in row {r+1}")
                return False
            inrow.append(elem)
            # print(inrow)
            
    # check col for duplicates
    for c in range(9):
        incol: List = []
        for r in range(9):
            elem = board[r][c]
            if elem in incol and elem != 0:
                print("!!!")
                print(f"{elem} appears more than once in col {c+1}")
                return False
            incol.append(elem)
            
    # check square for duplicates
    row_start = 0
    col_start = 0
    for s in range(9):
        insquare: List = []
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                elem = board[r][c]
                if elem in insquare and elem != 0:
                    print("!!!")
                    print(f"{elem} appears more than once in square {s+1}")
                    return False
                insquare.append(elem)
                # print(insquare)
        if col_start == 6:
            col_start = 0
            row_start += 3
        else: 
            col_start += 3
               
    return True
    
def find_next_empty() -> tuple:
    """Find the next empty location"""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r,c
    return None, None   # return null if there are no more empty spaces (done!)


def is_valid(guess, row, col) -> bool:
    """Check to for duplicates for a guess in a row, col, and square"""
    # check row for duplicates
    row_vals = board[row]
    if guess in row_vals:
        return False
    
    # check col for duplicates
    col_vals = []
    col_vals = [board[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # check square for duplicates
    row_start = (row // 3) * 3  # find starting row of the square the location is in
    col_start = (col // 3) * 3  # find starting col of the square the location is in
    for r in range(row_start, row_start + 3):  # loop through everything in the square given top-right corner
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False
    
    return True


def print_board() -> None:
    """Print the board array with lines to separate squares"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
            
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  # print without the newline at the end
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")  # print without the newline at the end
             
main()
print_board()