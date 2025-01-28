#Importing Libraries
import cv2               # To connect with camera
import numpy as np       # To get data from camera vision
import os                # To perform windows explorer commands
from time import sleep   # To give some time gap between commands

# Defining Constant
LetterCode = 8


# This functions returns the bgr tuple of centre pixel of given image by address.
def dominentColor(imgAddress:str):
    img = cv2.imread(imgAddress)
    height, width, _ = np.shape(img)
    centerColor = img[height//2,width//2]
    return centerColor


# This function takes photo and save it as webCamePhoto.jpg
def takePicture(cap):
    frame = cap.read()[1]
    cv2.imwrite('webCamPhoto.jpg', frame)


# This function call takePicture to capture photo then get centre of that photo using dominent color. 
# Then delete existing photo to make space for new one.
def frameDominentColor(cam):
    takePicture(cam)
    color = dominentColor('webCamPhoto.jpg')
    os.remove("webCamPhoto.jpg")
    return color


# Check brightness of given bgr tuple by limit.
def BrightnessCheck(cam, brightnessLimit):
    colors = frameDominentColor(cam)
    fBlue, fGreen, fRed = colors
    if fBlue>=brightnessLimit and fGreen>=brightnessLimit and fRed>=brightnessLimit:
        return "1"
    else:
        return "0"


# This function perform connectivity to camera and after performing 
# different function with camera it will exit from camera
def startScanAndGiveCode(webCam, timeDelay, MaxLimit):
    encrypted = ""
    pic = cv2.VideoCapture(webCam)
    while encrypted[-1:-1*LetterCode-1:-1]!="0"*LetterCode or len(encrypted)%LetterCode!=0:
        sleep(timeDelay)
        encrypted+=BrightnessCheck(pic, MaxLimit)
        print(encrypted[-1])
    pic.release()
    return encrypted


# This function convert binary into text
def decryption(code, codeDict, decrypted = ""):
    if code == "0"*LetterCode:
        return decrypted
    else:
        if code[:LetterCode] in codeDict:
            decrypted+=codeDict[code[:LetterCode]]
        return decryption(code[LetterCode:], codeDict, decrypted)
