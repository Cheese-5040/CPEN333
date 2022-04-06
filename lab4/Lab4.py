#student name: Ow Yong Chee Seng 
#student number: 61164992

from threading import Thread
import heapq
#use a min heap to reduce the runtime for finding min k items
def kthSmallest(arr, k):
    smallest = []
    for value in arr:
        if (len(smallest) < k): #make the smallest new value the root node of the min heap
            heapq.heappush(smallest, -value)
        else: #pop the root and bubble up the heap, put in array
            heapq.heappushpop(smallest, -value)
    #if the kth value is out of range, return nothing 
    if (len(smallest) < k):
        return None
    #return the last index of the smallest as K
    return -smallest[0]

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    global sortedFirstHalf
    global sortedSecondHalf
    
    if firstHalf==True:
        # use min heap to get k min elements
        for i in range(1, int(len(testcase)/2) +1): #sorted first half of the testcase
            #add the smallest k min elements to the sorted array
            sortedFirstHalf.append(kthSmallest(testcase,i))
    else:
        #also use min heap to get k min elements 
        for i in range(int(len(testcase)/2) +1,len(testcase)+1): #sorted second half 
            #similar as above, add the smallest k elements in the array back to second half
            sortedSecondHalf.append(kthSmallest(testcase,i))
    #print(f"sorted first half = {sortedFirstHalf}")
    #print(f"sorted second half = {sortedSecondHalf}")

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    global SortedFullList
    i=0
    j=0
    for k in range(len(testcase)):
        if i<= len(sortedFirstHalf)-1 and sortedFirstHalf[i] <= sortedSecondHalf[j]:
            #print(f"length of sorted first half = {len(sortedFirstHalf)}")
            #print(f"index first half = {i}")
            SortedFullList.append(sortedFirstHalf[i])
            i = i+1
        else :
            SortedFullList.append(sortedSecondHalf[j])
            j = j + 1

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    # testcase = [12,-1,7,-40,7,3,50,6,5040,8]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of their code below, as specified 
    #create the left and right thread to sort the first and second half of the array
    leftThread = Thread(target=sortingWorker, args=(True,))
    rightThread = Thread(target= sortingWorker, args=(False,))
    leftThread.start()
    rightThread.start()
    leftThread.join()
    rightThread.join()
    #wait until left and right to be done to merge all the values together
    mergeThread = Thread(target= mergingWorker)
    mergeThread.start()
    mergeThread.join()
    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)