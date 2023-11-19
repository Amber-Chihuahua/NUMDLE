"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    User defined function used to compare the user input with program generated value, 
    display corresponding results and return values used for loop control.

Assignment Information
    Assignment:     Individual Project UDF
    Author:         Amber Lu, lu1061@purdue.edu
    Team ID:        LC3 - 02

    Contributor: Name, @purdue.edu

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
from colorama import Fore, Style, init

def checkVal(guess, num, numRec):
    init()
    correctChar =[]
    correctDig = 0
    for i in range(0,5):

            if guess[i] == num[i]:
                correctChar.append(i)
                numRec[guess[i]] -= 1
                correctDig += 1

    for i in range(0,5):
        if i in correctChar:
            print(f"{Fore.GREEN}{guess[i]}{Style.RESET_ALL}",end='')
        elif guess[i] in num and numRec[guess[i]] > 0:
            print(f"{Fore.YELLOW}{guess[i]}{Style.RESET_ALL}",end='')
            numRec[guess[i]] -= 1
        else:
            print(f"{guess[i]}",end='')

    return correctDig


                 


