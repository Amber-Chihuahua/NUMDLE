"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    Replace this line with a description of your program.

Assignment Information
    Assignment:     Individual Project 
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

import random as rd
from UDF_IndivProject import checkVal

def main():
    print("Welcome to Numdle! A random 5-digit number is generated given your input, \nand you have 5 guesses to correctly guess the random number!")
    seed = input("Enter anything to generate your Numdle -> ")

    rd.seed(seed)
    numdle = str(f"{rd.randrange(0,100000):05d}")

    numDig = []
    numRec = []

    correctDig = 0
    invalid = 1
    count = 0

    numDig = getDig(numdle)
    
    while count < 5 and correctDig < 5:
        
        count+=1
        guessDig = []
        correctDig = 0
        numRec = digRecur(numDig)

        while invalid:

            guess = input(f"\nEnter guess #{count}: ")

            if not guess.isdigit():
                print("Please enter a 5-digit number without characters.")
                invalid = 1
            elif len(guess) != 5:
                print("Please enter a 5-digit number.(00000-99999)")
                invalid = 1
            else:
                guessDig = getDig(guess)
                invalid = 0
        correctDig= checkVal(guessDig, numDig, numRec)
        invalid = 1
    if correctDig == 5:
        print("\nCongrats! You have guessed the correct number!")

def getDig(number): #separate the input into recurring digits

    Digits = []

    for digit in number:
        Digits.append(int(digit))

    return Digits

def digRecur(number):#counts the recurrence of digit

    recur = []

    for digit in range(0,10):
        recur.append(number.count(digit))

    return recur

if __name__ == '__main__':
    main()