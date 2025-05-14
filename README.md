**LightFlash Converter**

LightFlash Converter is a Python application that converts text to light flashes and decodes light flashes into text. Using Pygame, it displays text as a sequence of black (0) and white (1) flashes based on ASCII binary representation. With OpenCV, it captures light flashes via a webcam and decodes them into text. The project also includes a fun mode with custom codes for humorous phrases and media playback.
✨ Features

Text to Flashes: Converts input text to binary (ASCII) and displays it as black and white flashes using Pygame.
Flashes to Text: Captures light flashes via webcam (OpenCV) and decodes them into text using ASCII or custom codes.
Custom Fun Mode: Decodes specific 4-bit codes into phrases like "Just looking like a wow. 😁" or triggers a video playback.
Interactive CLI: Command-line interface for selecting modes (e.g., Code to Light, Light to Code, Presentation).
Configurable Parameters: Adjustable time delay, brightness threshold, and countdown duration.

📑 **Table of Contents**

Installation
Usage
Configuration
Project Structure
Contributing
License
Contact

🛠️ **Installation**
Follow these steps to set up the project locally.
Prerequisites

Python 3.8+
Webcam (for flash-to-text functionality)
Windows OS (for certain OS-specific commands like os.startfile)

Steps

Clone the repository:
git clone https://github.com/your-username/lightflash-converter.git
cd lightflash-converter


Install dependencies:
pip install opencv-python pygame numpy


Ensure your webcam is connected and accessible (default device ID: 0).


🚀 **Usage**
Run the main script to start the command-line interface:
python main.py

Follow the on-screen instructions to select a mode:

Code to Light: Enter text to convert into flashes.
Light to Code: Use the webcam to decode flashes into ASCII text.
Light to Fun Code: Decode flashes into custom phrases or trigger a video.
Presentation: Open the project presentation in your default browser.
Exit/Quit: Close the program.

_Example Commands_

Text to Flashes:
Here: code to light
Type your time delay in seconds: 0.25
Type your code: hello

The screen will flash black and white based on the binary representation of hello.

Flash to Text:
Here: light to code
Type your time delay in seconds: 0.25

Point your webcam at a flashing screen to decode the text.

Fun Mode:
Here: light to fun code
Type your time delay in seconds: 0.25

Flash specific patterns (e.g., 1100) to display phrases like "Just looking like a wow. 😁".


Demo

⚙️ **Configuration**
Modify parameters in main.py to customize the application:

webCamID: Set to your webcam device ID (default: 0).
brightnessLimit: Adjust the brightness threshold for flash detection (0–255, default: 150).
ScanTime: Set the time delay between flash captures or displays (default: 0.25 seconds).
countDown_time: Duration of the countdown before flashing (default: 5 seconds).
countDownColor: RGB color for the countdown background (default: red, (0,0,255)).

📂 **Project Structure**

main.py: Entry point with the command-line interface and core logic.
AsciiEncryption.py: Handles text-to-flash conversion using Pygame.
AsciiDecryption.py: Manages flash-to-text decoding using OpenCV and ASCII.
decryption4Bit.py: Implements the "fun" mode with 4-bit custom codes.

🤝 **Contributing**
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

Please read our Contributing Guidelines for more details.
📜 **License**
This project is licensed under the MIT License.
📬 **Contact**

Email: nabeeharehmanali@gmail.com
GitHub: nabeeharehman
Project Link: lightflash-converter

