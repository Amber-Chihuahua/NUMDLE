"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    User defined functions for the Numdle Project. Separate input into standalone digits, find the recurrence of digits, 
    and compare the value of the guesses with the actual generated number, and return the necessary information to main.

Assignment Information
    Assignment:     Individual Project - Numdle -User Defined Functions
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
#this UDF separate the input into recurring digits
def getDig(number): 

    Digits = [] #array containing individual digits

    for digit in number:
        Digits.append(int(digit))

    return Digits

#this UDF counts the recurrence of digit
def digRecur(number):
    recur = [] #array containing the frequency of numbers from 0-9 in the number passed in

    for digit in range(0,10):
        recur.append(number.count(digit))

    return recur

#this UDF compares the user's guess with the actual generated value and returns the necessary details to main
def checkVal(guess, num, numRec):
    correctChar =[] #contains the 
    color = [0,0,0,0,0]
    correctDig = 0

    for i in range(0,5):

            if guess[i] == num[i]:
                correctChar.append(i)
                numRec[guess[i]] -= 1
                correctDig += 1

    for i in range(0,5):
        if i in correctChar:
            color[i] = 'G'
        elif guess[i] in num and numRec[guess[i]] > 0:
            color[i] = 'Y'
            numRec[guess[i]] -= 1
        else:
            color[i] = 'N'

    return correctDig, color
