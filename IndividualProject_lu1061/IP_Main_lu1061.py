"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    A simple game that challenges the user's logical skills by generating a random number using the seed provided by the user, 
    and providing clues to the user based on their guesses to direct the user towards the correct number. 

Assignment Information
    Assignment:     Individual Project - Numdle - Main Program
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
import pygame as pg
import random as rd
from IP_UDF_lu1061 import getDig, checkVal, digRecur

#sets the RGB color codes into readable global constants
WHITE =(255,255,255) 
GRAY = (61,61,61)
BLACK = (0,0,0)
RED = (240, 49, 31)
YELLOW = (252, 195, 35)
GREEN = (51, 204, 8)

def main():
    isOpen = 1
    isError = 0
    pg.init()

    x = 650
    y = 800

    surface = pg.display.set_mode((x,y)) #size of window display
    pg.display.set_caption("Numdle") #window title

    clock=pg.time.Clock() #counter used to refresh the screen

    pixlFont = 'cvgafix.fon' #store font into variable

    #store text objects into the class NdObj (Numdle Objects)
    input = NdObj("",pixlFont,16,WHITE,surface)
    descript = NdObj("Welcome to Numdle!",pixlFont,16,WHITE,surface)
    descript2 = NdObj("A random 5-digit number is generated given your input,",pixlFont,16,WHITE,surface)
    descript3 = NdObj("and you have 5 guesses to correctly guess the random number!",pixlFont,16,WHITE,surface)
    prompt=  NdObj("Enter anything to generate your Numdle -> ",pixlFont,16,WHITE,surface)
    red = NdObj("",pixlFont,16,RED,surface)
    gray = NdObj("",pixlFont,16,GRAY,surface)
    yellow = NdObj("",pixlFont,16,YELLOW,surface)
    green = NdObj("",pixlFont,16,GREEN,surface)

    #Initializes guess prompts and user guesses into the NdObj class
    guessPrpt = NdObj("",pixlFont,16,WHITE,surface)
    guessInp= NdObj("", None, 40, WHITE, surface)
    guessPrpt2 = NdObj("",pixlFont,16,WHITE,surface)
    guessInp2= NdObj("", None, 40, WHITE, surface)
    guessPrpt3 = NdObj("",pixlFont,16,WHITE,surface)
    guessInp3= NdObj("", None, 40, WHITE, surface)
    guessPrpt4 = NdObj("",pixlFont,16,WHITE,surface)
    guessInp4= NdObj("", None, 40, WHITE, surface)
    guessPrpt5 = NdObj("",pixlFont,16,WHITE,surface)
    guessInp5= NdObj("", None, 40, WHITE, surface)

    #Initialize the on-screen error display and the final text box display into class NdObj
    prtSys = NdObj("",pixlFont,16,RED,surface)
    correct = NdObj("", None, 30, WHITE, surface)
    end = NdObj("", None, 30, WHITE, surface)

    #initializes the input sequence
    inputSeq = 0

    while isOpen:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                isOpen = False
            if inputSeq == 0:
                gameEnd = 0
                correctDig=0
                Line1 = Rect(surface, 90, 140)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        input.txt = input.txt[:-1]
                    elif event.key == pg.K_RETURN:
                        seed = input.txt
                        rd.seed(seed)
                        numdle = str(f"{rd.randrange(0,100000):05d}")
                        numDig = getDig(numdle)
                        numRec = digRecur(numDig)
                        inputSeq+= 1
                    else:
                        input.txt += event.unicode

            elif inputSeq == 1:

                Line2 = Rect(surface, 90, 270, border=BLACK)
                inputSeq, correctDig, isError=getValue(event,inputSeq,numRec,numDig,guessPrpt,guessInp,Line1,prtSys, red, gray, yellow, green, isError)
            elif correctDig >=5:
                 gameEnd=1
                 correct.txt = "Congratulations! You have guessed the correct number!"
                 img = pg.image.load('happi.png').convert_alpha()
                 boxcolor = YELLOW
            elif inputSeq == 2:
                    Line3 = Rect(surface, 90, 400, border=BLACK)
                    Line2.border = [GRAY,GRAY,GRAY,GRAY,GRAY]
                    numRec = digRecur(numDig)
                    inputSeq, correctDig, isError=getValue(event,inputSeq,numRec,numDig,guessPrpt2,guessInp2,Line2,prtSys, red, gray, yellow, green, isError)

            elif inputSeq == 3:
                    Line4 = Rect(surface, 90, 530, border=BLACK)
                    Line3.border = [GRAY,GRAY,GRAY,GRAY,GRAY]
                    numRec = digRecur(numDig)
                    inputSeq, correctDig, isError=getValue(event,inputSeq,numRec,numDig,guessPrpt3,guessInp3,Line3,prtSys, red, gray, yellow, green, isError)
            elif inputSeq == 4:
                Line5 = Rect(surface, 90, 660, border=BLACK)
                Line4.border = [GRAY,GRAY,GRAY,GRAY,GRAY]
                numRec = digRecur(numDig)
                inputSeq, correctDig, isError=getValue(event,inputSeq,numRec,numDig,guessPrpt4,guessInp4,Line4,prtSys, red, gray, yellow, green, isError)
            elif inputSeq == 5:
                
                Line5.border=[GRAY,GRAY,GRAY,GRAY,GRAY]
                numRec = digRecur(numDig)
                inputSeq, correctDig, isError=getValue(event,inputSeq,numRec,numDig,guessPrpt5,guessInp5,Line5,prtSys, red, gray, yellow, green, isError)
            else:
                gameEnd=1
                correct.txt = "You have failed to guess the correct number."
                img = pg.image.load('sadge.png').convert_alpha()
                boxcolor = GRAY
            if gameEnd:
                end.txt= "Press r to play again"
                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                    inputSeq = 0
                    input.txt = ""
                    guessPrpt.txt =""
                    guessInp.txt=""
                    guessPrpt2.txt =""
                    guessInp2.txt=""
                    guessPrpt3.txt =""
                    guessInp3.txt=""
                    guessPrpt4.txt =""
                    guessInp4.txt=""
                    guessPrpt5.txt =""
                    guessInp5.txt=""
            if not isError:
                red.txt = "Error"
                gray.txt = "Fully Incorrect"
                yellow.txt = "Wrong Position"
                green.txt = "Fully Correct"
            else:
                red.txt = " "
                gray.txt=" "
                yellow.txt= " "
                green.txt=" "

        surface.fill(BLACK) #refreshes elements on screen

        descript.ctr_text(x,16)
        descript2.ctr_text(x,35)
        descript3.ctr_text(x,51)
        prompt.left_text(20,67)

        input.update()
        input.left_text(prompt.Area.right + 1, 67)

        prtSys.update()
        prtSys.ctr_text(x,95)
        

        if inputSeq >= 1:
            red.update()
            red.left_text(125,90)
            gray.update()
            gray.left_text(red.Area.right+10, 90)
            yellow.update()
            yellow.left_text(gray.Area.right+10, 90)
            green.update()
            green.left_text(yellow.Area.right+10,90)

            guessPrpt.update()
            guessPrpt.left_text(20,110)
            Line1.drawRect()
            guessInp.update()
            guessInp.indNum(Line1)

        if inputSeq >=2:
            guessPrpt2.update()
            guessPrpt2.left_text(20,240)
            Line2.drawRect()
            guessInp2.update()
            guessInp2.indNum(Line2)

        if inputSeq >=3:
            guessPrpt3.update()
            guessPrpt3.left_text(20,370)
            Line3.drawRect()
            guessInp3.update()
            guessInp3.indNum(Line3)

        if inputSeq >=4 :
            guessPrpt4.update()
            guessPrpt4.left_text(20,500)
            Line4.drawRect()
            guessInp4.update()
            guessInp4.indNum(Line4)

        if inputSeq >=5:
            guessPrpt5.update()
            guessPrpt5.left_text(20,630)
            Line5.drawRect()
            guessInp5.update()
            guessInp5.indNum(Line5)

        if gameEnd:
            correct.update()
            end.update()
            text_box =pg.Rect(20, y,600,200)
            text_box.center = (x//2,y//2)
            pg.draw.rect(surface,boxcolor,text_box,border_radius=3)
            correct.ctr_text(x, text_box.top +30)
            end.ctr_text(x,text_box.top+180)
            surface.blit(img, (225,345))


        pg.display.flip()
        clock.tick(15)

class NdObj:
    def __init__(self, string,font,size,color,surface):
        self.txt = string
        self.font = pg.font.Font(font,size)
        self.color = color
        self.surface= surface

        self.Disp = self.font.render(self.txt, True, self.color)
        self.Area = self.Disp.get_rect()

    def ctr_text(self,x,y):
        self.Area.center = (x//2,y)
    
        self.surface.blit(self.Disp, self.Area)

    def left_text(self, x, y):
        self.Area.left = x
        self.Area.top = y
        
        self.surface.blit(self.Disp, self.Area)

    def update(self):
        self.Disp = self.font.render(self.txt, True, self.color)
        self.Area = self.Disp.get_rect()

    def indNum(self, line):
        j =0
        for i in self.txt:
            Disp = self.font.render(i, True, self.color)
            Area = Disp.get_rect()
            Area.center = line.Inner[j].center
            self.surface.blit(Disp, Area)
            j+=1


class Rect:
    def __init__(self, surface, x, y, wid=90, ht=90, fill=BLACK, border=GRAY):
        self.Border = [0,0,0,0,0]
        self.Inner =[0,0,0,0,0]
        self.fill = [fill,fill,fill,fill,fill]
        self.border = [border,border,border,border,border]
        self.surface = surface
        self.x = x
        self.y = y
        self.wid = wid
        self.ht= ht

        for i in range(0,5):
            self.Border[i], self.Inner[i] = self.makeRect(x+95*i, y)


    def makeRect(self, x, y):
        return pg.Rect(x,y,self.wid,self.ht), pg.Rect(x+2.5, y+2.5, self.wid-5, self.ht-5)

    def drawRect(self):
        for i in range(0,5):
            pg.draw.rect(self.surface, self.border[i], self.Border[i], border_radius =3)
            pg.draw.rect(self.surface, self.fill[i], self.Inner[i], border_radius =3)

def getValue(event,x,numRec, numDig, guessPrpt, guessInp, line, prtSys, red, gray, yellow, green, isError):
    correctDig =0

    guessPrpt.txt = f"Enter guess #{x}: "
    if event.type == pg.KEYDOWN:

                        if event.key == pg.K_BACKSPACE:
                            guessInp.txt = guessInp.txt[:-1]
                        elif event.key == pg.K_RETURN and len(guessInp.txt)>0:
                
                            if len(guessInp.txt) != 5:
                                prtSys.txt = "Please enter a 5-digit number.(00000-99999)"
                                isError=1
                                for i in range (0,5):
                                    line.border[i] = RED
                                    line.fill[i] = RED
                            else:
                                guessDig = getDig(guessInp.txt)
                                isError=0
                                prtSys.txt=""
                                correctDig, color = checkVal(guessDig, numDig, numRec)
                                for i in range (0,5):
                                    if color[i] == 'G':
                                        line.border[i] = GREEN
                                        line.fill[i] = GREEN
                                    elif color[i] == 'Y':
                                        line.border[i] = YELLOW
                                        line.fill[i] = YELLOW
                                    else:
                                        line.border[i] = GRAY
                                        line.fill[i] = GRAY
                                x+=1
                        elif event.unicode in '0123456789' and len(guessInp.txt) < 5:
                            guessInp.txt += event.unicode
                        elif event.key != pg.K_RETURN:
                            prtSys.txt = "Please enter a 5-digit number without characters."
                            isError = 1
    
    return x, correctDig, isError
if __name__ == '__main__':
    main()

    
    


