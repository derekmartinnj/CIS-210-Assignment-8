'''
Author: Derek Martin
Assignment: CIS 210 Winter 2019 Project 8.2 Test Binary Search
Credits: N/A
Description: write a test function, test_isMember(), to automate testing of isMember() from project 8-1.
'''

import p81_binsearch as p81

testcases = (((1, 2, 3, 3, 4), 4, True),((1, 2, 3, 3, 4), 2, True),('aeiou', 'i', True),
             ('aeiou', 'y', False),((1, 3, 5, 7), 4, False),((23, 24, 25, 26, 27), 5, False),
             ((0, 1, 4, 5, 6, 8), 4, True),((0, 1, 2, 3, 4, 5, 6), 3, True),((1, 3), 1, True),
             ((2, 10), 10, True),((99, 100), 101, False),((42,), 42, True),((43,), 44, False),
             ((), 99, False))

def test_isMember():
    '''
    () -> None

    Run through test case data, check results of isMember() function, and display test results

    >>> test_isMember((1, 2, 3, 3, 4), 4)
    Checking (1, 2, 3, 3, 4) for target 4 ...Its value True is correct!
    >>> isMember('aeiou', 'y')
    Checking aeiou for target y ...Its value False is correct!
    '''
    for case in testcases:
        if p81.isMember(case[0],case[1]) == case[2]:
            print("Checking", case[0], "for target", case[1], "...Its value", case[2], "is correct!")
        else:
            print("Checking", case[0], "for target", case[1], "...Its value", case[2], "is not correct.")
    return None

def main():
    ''' Calls test_isMember() '''
    test_isMember()

main()
