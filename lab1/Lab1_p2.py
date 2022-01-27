'''
Done by : Ow Yong Chee Seng
SID: 61164992
'''
def displayPyramid(size: int) -> None:
    """
        This method prints a pyramid of size size.
        Implement the method using nested for loops.
        size is an integer between 1 and 9 (inclusive).
        Example: if size is 7, it should print:
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
    """      
    layer = 1 
    while layer <=size: 
        string = ""
        #appending the first sequence of double spaces before the digit
        for i in range(size - layer):
            string += "  "
        #appending the number in decending order based on layer height
        for j in range(layer):
            string += " " + str(layer-j)
        #appending the ascending number after 1, starting from 2 until layer height
        for k in range(2,layer+1):
            string += " " + str(k)
        print(string) #one row produced, go to newline and increment layer height
        layer +=1    
        
if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Make sure that you fully test your code.
        This prints the output for all rquired 
        sizes, from 1 to 9.
    """
    for size in range (1, 10):
        displayPyramid(size)