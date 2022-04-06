#student name: Ow Yong Chee Seng    
#student number: 61164992

import multiprocessing as mp

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    #list to track all previously visited numbers
    wholeCol = []
    #start from row 0 to 9
    for i in range(9): 
        #add number to visited list
        wholeCol.append(puzzle[i][column])
        #check if valid number, then check for repeats in previous numbers in whole column
        if puzzle[i][column] < 1 or puzzle[i][column] > 9 or wholeCol.count(puzzle[i][column]) > 1: 
            print(f"Column {column} not valid") 
            return
    #if everything passes it means that the column is valid
    print(f"Column {column} valid")
def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    #list to track all previously visited numbers
    wholeRow = []
    #start from row 0 to 9
    for i in range(9): 
        #add to list of numbers visited
        wholeRow.append(puzzle[row][i])
        #check if valid number, then check for repeats in previous numbers in whole row
        if puzzle[row][i] < 1 or puzzle[row][i] > 9 or wholeRow.count(puzzle[row][i]) > 1: 
            print(f"Row {row} not valid") 
            return
    # if everything passes it means that the row is valid
    print(f"Row {row} valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # list of visited values
    wholeSubgrid = []
    #we need to traverse through each row three times and each column three times
    startCol = 3* int(subgrid % 3) #start column 
    startRow = 3* int(subgrid/3) #start row
    #row traverse
    for i in range(3): 
        #column traverse
        for j in range(3): 
            #add number to list of visited values
            wholeSubgrid.append(puzzle[startRow+i][startCol+j])
            #check if number is out of bound, or repeated in previous values 
            if puzzle[startRow + i][startCol+j] <1 or puzzle[startRow+i][startCol+j] >9 or wholeSubgrid.count(puzzle[startRow+i][startCol+j])!=1:
                print(f"Subgrid {subgrid} not valid")
                return
    #if everything passes it means that the subgrid is valid
    print(f"Subgrid {subgrid} valid")

if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test1   #modify here for other testcases
    SIZE = 9
    allProcess= []
    for col in range(SIZE):  #checking all columns
        singleProcess = mp.Process(target=checkColumn, args=(testcase, col))#create a process to check if a column is valid, parse the testcase and col number as arguments
        allProcess.append(singleProcess)                                    #add the process into the list of all processes
        singleProcess.start()                                               #start the process

    for row in range(SIZE):  #checking all rows
        singleProcess = mp.Process(target=checkRow, args=(testcase, row))#create a process to check if a row is valid, parse the testcase and row number as arguments
        allProcess.append(singleProcess)                                 #add the process to the list of all processes
        singleProcess.start()                                            #start the process

    for subgrid in range(SIZE):   #checking all subgrids
        singleProcess = mp.Process(target=checkSubgrid, args=(testcase, subgrid))#create a process to check if the subgrid is valid, parse the testcase and subgrid number as arguments
        allProcess.append(singleProcess)                                         #add the process to list of all processes
        singleProcess.start()                                                    #start the process

    for i in range(len(allProcess)):
        allProcess[i].join()                                                #combine all the processes to obtain the printed result