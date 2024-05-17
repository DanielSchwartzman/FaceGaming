<p align="center">
  <img src="./res/Icons/FaceGamingDisplayLogo.png" width="437.5" height="125">
</p>

# About FaceGaming
FaceGaming is Python project aiming to allow physically impaired people to comfortably and easily play videogames by using their face and facial expressions as input for in game events.
Made as capstone project for my B.Sc in Computer Science studies at Afeka College of Engineering in Tel-Aviv.

## Usage and Demonstration

### Main window
![MainWindowDemo](https://github.com/DanielSchwartzman/FaceGaming/assets/127026045/ffea6e06-7512-4e08-86b8-aa7c5b8bbae6)

Overall system toggle, while toggled off, Facial expressions or Head movement wont be translated to computer input


### Keyboard Configuration window
![KeyboardWindowDemo](https://github.com/DanielSchwartzman/FaceGaming/assets/127026045/5c89189a-2dd4-4235-96d7-6ae88243e568)

Choose your prefered binding for the selected key, currently supporting:
* Movement - Controls for the default in game(3D) movement keys(WASD).
* Spacebar - Controls the spacebar key, usually mapped to "Jump".
* Control - Controls the Left Control key, usually mapped to "Crouch" or "Duck".
* Interact - Controls the Left Interact("E") key, usually used to interact with in-game environment

### Mouse configuration window
![MouseWindowDemo](https://github.com/DanielSchwartzman/FaceGaming/assets/127026045/05ac388b-fb55-47f0-ac76-494d1045081b)

Choose your prefered binding for the selected key, currently supporting:
* LeftClick - Controls the Left click mouse button
* RightClick - Controls the Right click mouse button
* Mouse - Controls for movement of the mouse, simple and comfortable to use both in-game and general computer usage.
Wide angle movements, such as orienting your face left, right, up or down, control the relative movement of the cursor, used to position the
cursor on the general area of the desired object.
Finer movements, control the absolute position of the cursor, used to allow the user to place the cursor on smaller 
objects such as Windows/Menu buttons and/or small in-game objects.

NOTE - Since in-game mouse movement and general movement(Menu/Windows) use different type of overall mouse movement,
you need to switch between the two modes depending on your current use.

To switch between modes, Orient your Eyebrows down and open your mouth simultaniously, as noted in the small pink banner at the bottom
of the "Mouse Configuration" tab.

### Options Window
![OptionWindowDemo](https://github.com/DanielSchwartzman/FaceGaming/assets/127026045/a5527069-638d-4a05-a6e2-fe31481559e8)

General options and additional features to increase ease of use, currently supporting:
* Save settings - Save your currently selected input mapping for future use, Input mapping will be automatically loaded
when starting the application
* Input Device - Switch between all currently available PC cameras, All available cameras are scanned on application start
so connecting new camera will require you to restart the application
* Camera output - Small window that displays what the application currently sees, used to ensure that the camera is working correctly and that
the desired camera is currently selected.

NOTE - The stream is capped at 30FPS, while the overall system support higher framerate cameras

### Demonstration
TODO

## Installation
You can either download the Executable version or the Python script

### Executable version:
Download the [release](https://github.com/DanielSchwartzman/FaceGaming/releases/tag/V1) version and simply launch the .exe, Enjoy!

### Python Script:

Clone this repository
```
$ git clone https://github.com/DanielSchwartzman/FaceGaming
```

Download and install [Python 3.11](https://www.python.org/downloads/)

#### Install the following libraries:
```
$ python -m pip install <Library Name>
```
* opencv-python 
* mediapipe
* keyboard
* pywin32
* msvc-runtime
* pyqt6
* pyqttoast
* pymongo

### Launch FaceGaming.py, enjoy!

## Authors
- [@DanielSchwartzman](https://github.com/DanielSchwartzman)
- [@Tomer258](https://github.com/Tomer258)

## Special Thanks
* QToggle checkbox by luandiasrj - [QToggle](https://github.com/luandiasrj/QToggle_-_Advanced_QCheckbox_for_PyQT6)
* pyqt-toast by niklashenning - [pyqt-toast](https://github.com/niklashenning/pyqt-toast)
