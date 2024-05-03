import os

Frame = []
KeyMapping = [0] * 13
IsMinimized = False
IsCamReady = False

user_id = 0


def CheckIfFileExists():
    global user_id
    if os.path.isfile("UserId.txt"):
        file = open("UserId.txt", "r")
        user_id = file.readline()
        file.close()
        return True
    else:
        return False
