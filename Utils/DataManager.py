import os

"""
Used to pass quick and efficient communication between the "Services" and "GUI" Modules

CheckIfFileExists : Simply True or False if the UserId.txt file exists
"""

# Contains the current frame captured by the camera, used by the GUI to display a picture
Frame = []

# Array of currently mapped inputs
# DataManger.KeyMapping indexes correspond to:
# 0 = "Default",
# 1 = "Face Left",
# 2 = "Face Right",
# 3 = "Mouth Left",
# 4 = "Mouth Right",
# 5 = "Mouth Open",
# 6 = "Eye wide",
# 7 = "Brows up"
# 8 = "FaceTracking"
# 9 = "Activation Flag"
# 10 = "Process state flag on/off"
# 11 = "Num of available cameras"
# 12 = "Current Chosen Camera"
KeyMapping = [0] * 13

# Used to determine if the GUI is currently minimized or not, used to know if the frame from the camera should be stored or/and displayed
IsMinimized = False

# Used to indicate to the GUI that the FaceDetection module scanned all available cameras and is now ready to use
IsCamReady = False

# Used to know under which User id key should any Data be stored/updated
user_id = 0


############################################################################
def CheckIfFileExists():
    global user_id
    if os.path.isfile("UserId.txt"):
        file = open("UserId.txt", "r")
        user_id = file.readline()
        file.close()
        return True
    else:
        return False
############################################################################
