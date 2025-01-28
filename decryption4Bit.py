''' This python module is same as AsciiDecrypiton with different codeDict and
    letterCode to perform custom short codes'''

import cv2
import numpy as np
import os
from time import sleep


# Type quantity of code for one letter
LetterCode = 4

# Code Decryption
codeDict = {"1100": "Just looking like a wow.😁", 
            "0111": "Bupender Jogi 😎",
            "1101": "Ayein🤨"}



def dominentColor(imgAddress:str):
    img = cv2.imread(imgAddress)
    height, width, _ = np.shape(img)
    centerColor = img[height//2,width//2]
    return centerColor


def takePicture(cap):
    frame = cap.read()[1]
    cv2.imwrite('webCamPhoto.jpg', frame)


def frameDominentColor(cam):
    takePicture(cam)
    color = dominentColor('webCamPhoto.jpg')
    os.remove("webCamPhoto.jpg")
    return color


def BrightnessCheck(cam, brightnessLimit):
    colors = frameDominentColor(cam)
    #print(colors)
    fBlue, fGreen, fRed = colors
    if fBlue>=brightnessLimit and fGreen>=brightnessLimit and fRed>=brightnessLimit:
        return "1"
    else:
        return "0"


def startScanAndGiveCode(webCam, timeDelay, MaxLimit):
    encrypted = ""
    pic = cv2.VideoCapture(webCam)
    while encrypted[-1:-1*LetterCode-1:-1]!="0"*LetterCode or len(encrypted)%LetterCode!=0:
        sleep(timeDelay)
        encrypted+=BrightnessCheck(pic, MaxLimit)
        print(encrypted[-1])
    pic.release()
    return encrypted


def decryption(code, decrypted = ""):
    if code == "0"*LetterCode:
        return decrypted
    else:
        if code[:LetterCode] == "1001":
            os.startfile("BupinderJogi.mp4")
        elif code[:LetterCode] in codeDict:
            decrypted+=codeDict[code[:LetterCode]]
        return decryption(code[LetterCode:], decrypted)