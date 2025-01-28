#Importing Libraries
import pygame           # Pygame to perform color flashes into fullscreen with text
from time import sleep  # To give some time gaps between commands
from math import ceil   # To convert float into int. Sometime floats are less then 1 so it will make them 1.


# Declaring Constant
letterCode = 8





# Encryption

# Function takes plaintext and converts it to the string of 0s and 1s to be converted to flashes later
def encryption(string, codeDict):
    if string.isnumeric()==True:
        return string
    else:
        for k,v in codeDict.items():
            if v in string:
                string = string.replace(v,k)
        return encryption(string, codeDict)





#INITIALIZING PYGAME
pygame.init()



#setting up pygame and giving it access to output screen and put it into fullscreen
screen=pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)



'''FUNCTION TO FLASH THE SCREEN'''

#Function changes the text in pygame window and been called after change screen colour.
def flashscreen(colour, speed_of_flash, white, black):
    screen.fill(colour)


    # To show text in different color according to background
    myfont = pygame.font.SysFont("Times New Roman", 50)
    if colour == white:
        label = myfont.render("1", 1, black)
    elif colour == black:
        label = myfont.render("0", 1, white)
    text_rect = label.get_rect(center = screen.get_rect().center)
    screen.blit(label, (text_rect[0],0))
    

    pygame.display.flip() # To Update the Frame
    sleep(speed_of_flash) # For the duration of the flash



# Function which will show the countdown screen according to given time.
def countDown(countDown_time, countDownColor, white):
    for i in range(countDown_time):
        screen.fill(countDownColor)
        myfont = pygame.font.SysFont("Times New Roman", 150)
        label = myfont.render(str(countDown_time-i), 1, white)
        text_rect = label.get_rect(center = screen.get_rect().center)
        screen.blit(label, text_rect)
        pygame.display.flip()
        sleep(1)


# This function execute last specified seconds frame. which is important to stop decryption.
def lastFrame(wh, bl, sof):
    for k in range(ceil(sof*4)):
        screen.fill(bl)
        myfont = pygame.font.SysFont("Times New Roman", 50)
        l = myfont.render("It will end in "+str(ceil(sof*4-k))+" seconds", 1, wh)
        text_rect = l.get_rect(center = screen.get_rect().center)
        screen.blit(l, (text_rect[0],0))
        pygame.display.flip()
        sleep(1)


# This function start iteration between white and black screen by given time.
def switchingBlackAndWhite(code, wh, bl, sof):
    for index in range(len(code)):
        current_digit= code[index]
        if current_digit=="0":
            flashscreen(bl, sof, wh, bl)
        elif current_digit=="1":
            flashscreen(wh, sof, wh, bl)


# This is our main function. Which get encrypted code, start countdown then switching including last frame. 
def ConvertToFlash(string, black, white, countDown_time, countDownColor, speed_of_flash, codeDict):
    string=encryption(string, codeDict)
    countDown(countDown_time, countDownColor, white)
    switchingBlackAndWhite(string, white, black, speed_of_flash)
    lastFrame(white, black, speed_of_flash)
    pygame.quit()
