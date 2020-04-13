'''
Author: Derek Martin
Assignment: CIS 210 Winter 2019 Project 8.1 Binary Search
Credits: N/A
Description: Design, implement, and test algorithm for determining sequence inclusion using binary search.
'''

def isMember(aseq, target):
    '''
    (sequence of items/values) (item/value) -> boolean

    Determine whether 'target' is in 'aseq' using binary search

    >>> isMember((1, 2, 3, 3, 4), 4)
    True
    >>> isMember('aeiou', 'y')
    False

    note - 'aseq' must be sorted
    '''
    start = 0
    end = len(aseq) - 1
    while (start <= end):
        median = (start + end) // 2 # determine median based on current iteration
        if (aseq[median] == target):
            return True
        elif (target > aseq[median]):
            start = median + 1 # ingore other half of sequence
        else:
            end = median - 1
    return False

def main():
    ''' Calls isMember() function to test different inputs '''
    isMember((1, 2, 3, 3, 4), 4)
    isMember((1, 2, 3, 3, 4), 2)
    isMember('aeiou', 'i')
    isMember('aeiou', 'y')
    isMember((1, 3, 5, 7), 4)
    isMember((23, 24, 25, 26, 27), 5)
    isMember((0, 1, 4, 5, 6, 8), 4)
    isMember((0, 1, 2, 3, 4, 5, 6), 3)
    isMember((1, 3), 1)
    isMember((2, 10), 10)
    isMember((99, 100), 101)
    isMember((42,), 42)
    isMember((43,), 44)
    isMember((), 99)

main()
    
