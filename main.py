# Importing Mendatory Libraries
import AsciiDecryption as Decrypt    # To perform light to code
import decryption4Bit as FunDecrypt  # To perform light to fun code
from time import sleep               # To give some time gap between commands
import sys                           # To exit whole program
import os                            # To execute file because we want this program to run in loop.



# Type your webCam device id (Mine is 0 beacuse my computer have only one webCam Connected)
webCamID = 0

# Type brightness limit "0" is Extreme Dark (Black) and "255" is Extreme Bright (White)
brightnessLimit = 150

# Time Delay in Seconds
ScanTime = 0.25

#DECLARING CONSTANTS 
# define how many seconds of countdown you want in seconds
countDown_time = 5

# countdown background color
countDownColor=(0,0,255)

#DEFINING COLOUR OF FLASHES
white=(255,255,255)
black=(0,0,0)

#Empty string to store encryption
string = ""

# Code Decryption
codeDict= {}
for i in range(128):              # ASCII characters range from 0 to 127
    char = chr(i)
    binary = bin(i)[2:].zfill(8)  # Get binary representation, remove '0b' prefix, and zero-fill to 8 digits
    codeDict[binary] = char




# Instruction to use this program
print("_*"*10+"Instructions"+"*_"*10 + "\n")
print("1. Type 'Code to Light' to perform flashes according to given code.")
print("2. Type 'Light to Code' to turn camera on and start scan brightness to decrypt it into text.")
print("3. Type 'Light to Fun Code' to use custom codes in light to code command.")
print("             Custom Inputs are: 1100 for 'Just looking like a wow.'")
print("                                0111 for 'Bupender Jogi 😎'")
print("                                1101 for 'Ayein🤨'")
print("                                1001 to play bupender jogi video")
print("4. Type 'Presentation' to open our project presentation in your default browser.")
print("5. Type 'Exit' or 'Quit' to turn this program close.\n\n")
print("_*"*10+"Important things to note."+"*_"*10 + "\n")
print("1. Command 'code to light' may crash in first time because pygame run graphic drivers so it may hang.")
print("2. Command 'light to code' or 'light to fun code' may take sometime to start because CV2 need time to connect with camera.")
print()

# Main program in while loop
while True:
    
    # Take Inputs Everytime.

    # Take command to initiate light to code or code to light process
    UIC = ["light to code", "light to fun code", "code to light", "exit", "quit", "presentation"]
    userInput = input("Here: ")
    userInput = userInput.lower()

    # Input scantime to gice gap time for switvhing between black & white also scan time.
    if userInput not in UIC[4:]:
        ScanTime = input("Type your time delay in seconds. It must be integer or float value: ")
    else:
        ScanTime = "0"

    # If condition to check wheather given inputs are correct or they have problem.
    if ScanTime.replace('.', '', 1).isdigit() == False or userInput not in UIC:
        print("Please type correct command.")
    

    else:

        # Converting scantime to float because we need to put it as sleep in functions.
        ScanTime = float(ScanTime)


        # Conditions to check input commands

        # For command light to code
        if userInput == "light to code":
            string = Decrypt.startScanAndGiveCode(webCam = webCamID, timeDelay = ScanTime, MaxLimit = brightnessLimit)
            print(Decrypt.decryption(string, codeDict))
        
        # For command light to fun code
        elif userInput == "light to fun code":
            string = FunDecrypt.startScanAndGiveCode(webCam = webCamID, timeDelay = ScanTime, MaxLimit = brightnessLimit)
            print(FunDecrypt.decryption(string))

        # For command code to light
        elif userInput == "code to light":
            code = input("Type your code: ")

            # Importing Encryption here because importing pygame will start window frame at start.
            import AsciiEncryption as Encrypt

            Encrypt.ConvertToFlash(code, black, white, countDown_time, countDownColor, ScanTime, codeDict)

            # If we want to reset pygame we should exit whole frame. To do so we exit program and restart it.
            os.startfile("main.py")
            sys.exit()

        # To exit this program
        elif userInput == "exit" or userInput == "quit":
            break
        
        # To open presentation in default browser
        elif userInput == "presentation":
            os.system("start \"\" https://www.canva.com/design/DAF1uXCUV2U/NZS9LIFuO5QaT4QqthnBZQ/view?utm_content=DAF1uXCUV2U&utm_campaign=designshare&utm_medium=link&utm_source=editor")
        
        # To make string empty after every run
        string=""