import pygame as pg
import random as rd
from IndivProject import getDig

def main():
    isOpen = 1
    invalid = 1
    pg.init()

    x = 650
    y = 800

    surface = pg.display.set_mode((x,y)) #size of window display
    pg.display.set_caption("Numdle") #window title

    clock=pg.time.Clock()

    #sets the RGB color codes into readable variable names
    white=(255,255,255) 
    gray = (61,61,61)
    red = (240, 49, 31)
    yellow = (252, 195, 35)
    green = (51, 204, 8)
    pixlFont = 'cvgafix.fon'

    input = NdObj("",pixlFont,16,white,surface)
    descript = NdObj("Welcome to Numdle!",pixlFont,16,white,surface)
    descript2 = NdObj("A random 5-digit number is generated given your input,",pixlFont,16,white,surface)
    descript3 = NdObj("and you have 5 guesses to correctly guess the random number!",pixlFont,16,white,surface)
    prompt=  NdObj("Enter anything to generate your Numdle -> ",pixlFont,16,white,surface)
    guessPrpt = NdObj("",pixlFont,16,white,surface)
    guessInp= NdObj("", pixlFont, 16, white, surface)

    inputSeq = 0
    chg =1

    while isOpen:
        pg.draw.rect(surface,gray,pg.Rect(30,80,70,70))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                isOpen = False
            if inputSeq == 0:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        input.text = input.text[:-1]
                    elif event.key == pg.K_RETURN:
                        seed = input.text
                        rd.seed(seed)
                        numdle = str(f"{rd.randrange(0,100000):05d}")
                        inputSeq+= 1
                    else:
                        input.text += event.unicode
            if inputSeq == 1:
                if invalid:
                    guess=[]
                    if chg ==1:
                        guessPrpt.text = "Enter guess #1: "
                        chg+=1
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_BACKSPACE:
                            guessInp.text = guessInp.text[:-1]
                        elif event.key == pg.K_RETURN and len(guessInp.text)>0:
                
                            if len(guessInp) != 5:
                                system = "Please enter a 5-digit number.(00000-99999)"
                                invalid = 1
                            else:
                                guessDig = getDig(guessInp.text)
                                invalid = 0
                                inputSeq+=1
                        elif event.unicode in '0123456789' and len(guessInp.text) < 5:
                            guessInp.text += event.unicode
                        else:
                            system = "Please enter a 5-digit number without characters."
        surface.fill((0,0,0)) #refreshes elements on screen

        descript.ctr_text(x,16)
        descript2.ctr_text(x,35)
        descript3.ctr_text(x,51)
        prompt.left_text(20,67)

        input.left_text(prompt.Area.right + 1, 67)

        guessPrpt.left_text(20,90)

        guessInp.left_text(guessPrpt.Area.right + 1, guessPrpt.Area.top)

        if chg >= 2:
            pg.draw.rect(surface,gray,pg.Rect(60,120,90,90),border_radius=3)
            pg.draw.rect(surface,(0,0,0),pg.Rect(62.5,122.5,85,85),border_radius=3)

        pg.display.flip()
        clock.tick(15)

'''def update(text, color, font,surface):
    text_disp = font.render(text, True, color)
    gus1Area = text_disp.get_rect()
    gus1Area.left =20
    gus1Area.top = 80
    surface.blit(text_disp, gus1Area)
'''
class NdObj:
    def __init__(self, string,font,size,color,surface):
        self.text = string
        self.font = pg.font.Font(font,size)
        self.color = color
        self.surface= surface

        self.Disp = self.font.render(self.text, True, self.color)
        self.Area = self.Disp.get_rect()


    def ctr_text(self,x,y):
        self.Area.center = (x//2,y)

        self.surface.blit(self.Disp, self.Area)

    def left_text(self, x, y):
        self.Area.left = x
        self.Area.top = y

        self.surface.blit(self.Disp, self.Area)

if __name__ == '__main__':
    main()

    
    


