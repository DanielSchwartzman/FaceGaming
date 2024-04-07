import win32api
import win32con
import keyboard
import math

ACCEPTABLE_MOUTH_SCORE = 200

InputFlagArray = [False, False, False, False, False, False, False]


def Distance(firstX, firstY, secondX, secondY):
    return math.sqrt(math.pow(firstX - secondX, 2) + math.pow(firstY - secondY, 2)) * 1000


def SendInputToPC(Key, ToPress):
    match Key:
        case 1:
            if ToPress:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        case 2:
            if ToPress:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        # case 3:

        # case 4:

        # case 5:


# def FaceLeft():


# def FaceRight():


def MouthLeft(Key, Score):
    if Score >= ACCEPTABLE_MOUTH_SCORE and InputFlagArray[2] == False:
        SendInputToPC(Key, True)
        InputFlagArray[2] = True
    elif Score < ACCEPTABLE_MOUTH_SCORE and InputFlagArray[2] == True:
        SendInputToPC(Key, False)
        InputFlagArray[2] = False


def MouthRight(Key, Score):
    print(Score)
    if Score >= ACCEPTABLE_MOUTH_SCORE and InputFlagArray[3] == False:
        SendInputToPC(Key, True)
        InputFlagArray[3] = True
    elif Score < ACCEPTABLE_MOUTH_SCORE and InputFlagArray[3] == True:
        SendInputToPC(Key, False)
        InputFlagArray[3] = False


# def MouthOpen():

# def EyeWide():

# def BrowsUp():

def HeadTracking(Type, Landmarks):
    faceCenterX = (Landmarks[123].x + Landmarks[352].x) / 2
    faceCenterY = (Landmarks[152].y + Landmarks[10].y) / 2

    xDiff = (faceCenterX - Landmarks[4].x) * 1000
    yDiff = -(faceCenterY - Landmarks[4].y) * 1000

    if abs(yDiff) > 25:
        keyboard.press('shift')
    else:
        keyboard.release('shift')

    if abs(yDiff) < 15:
        keyboard.release('w')
        keyboard.release('s')
    elif yDiff < 0:
        keyboard.press('s')
        keyboard.release('w')
    elif yDiff > 0:
        keyboard.press('w')
        keyboard.release('s')

# def EyeTracking():
