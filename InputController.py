import win32api
import win32con
import keyboard
import math

ACCEPTABLE_MOUTH_SCORE = 200
ACCEPTABLE_FACE_ORIENTATION_SCORE = 200
ACCEPTABLE_FACE_RIGHT_ORIENTATION_SCORE = 800
ACCEPTABLE_EYE_WIDE_SCORE = 35
ACCEPTABLE_BROWS_SCORE = 300
ACCEPTABLE_MOUTH_OPEN_SCORE = 1

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
        case 3:
            if ToPress:
                keyboard.press("space")
            else:
                keyboard.release("space")
        case 4:
            if ToPress:
                keyboard.press("ctrl")
            else:
                keyboard.release("ctrl")
        case 5:
            if ToPress:
                keyboard.press("e")
            else:
                keyboard.release("e")


def FaceLeft(Key, Score):
    if Score >= ACCEPTABLE_FACE_ORIENTATION_SCORE and InputFlagArray[0] == False:
        SendInputToPC(Key, True)
        InputFlagArray[0] = True
    elif Score < ACCEPTABLE_FACE_ORIENTATION_SCORE and InputFlagArray[0] == True:
        SendInputToPC(Key, False)
        InputFlagArray[0] = False


def FaceRight(Key, Score):
    if Score >= ACCEPTABLE_FACE_RIGHT_ORIENTATION_SCORE and InputFlagArray[1] == False:
        SendInputToPC(Key, True)
        InputFlagArray[1] = True
    elif Score < ACCEPTABLE_FACE_RIGHT_ORIENTATION_SCORE and InputFlagArray[1] == True:
        SendInputToPC(Key, False)
        InputFlagArray[1] = False


def MouthLeft(Key, Score):
    if Score >= ACCEPTABLE_MOUTH_SCORE and InputFlagArray[2] == False:
        SendInputToPC(Key, True)
        InputFlagArray[2] = True
    elif Score < ACCEPTABLE_MOUTH_SCORE and InputFlagArray[2] == True:
        SendInputToPC(Key, False)
        InputFlagArray[2] = False


def MouthRight(Key, Score):
    if Score >= ACCEPTABLE_MOUTH_SCORE and InputFlagArray[3] == False:
        SendInputToPC(Key, True)
        InputFlagArray[3] = True
    elif Score < ACCEPTABLE_MOUTH_SCORE and InputFlagArray[3] == True:
        SendInputToPC(Key, False)
        InputFlagArray[3] = False


def MouthOpen(Key, Score):
    print(Score)
    if Score >= ACCEPTABLE_MOUTH_OPEN_SCORE and InputFlagArray[4] == False:
        SendInputToPC(Key, True)
        InputFlagArray[4] = True
    elif Score < ACCEPTABLE_MOUTH_OPEN_SCORE and InputFlagArray[4] == True:
        SendInputToPC(Key, False)
        InputFlagArray[4] = False


def EyeWide(Key, Score):
    if Score >= ACCEPTABLE_EYE_WIDE_SCORE and InputFlagArray[5] == False:
        SendInputToPC(Key, True)
        InputFlagArray[5] = True
    elif Score < ACCEPTABLE_EYE_WIDE_SCORE and InputFlagArray[5] == True:
        SendInputToPC(Key, False)
        InputFlagArray[5] = False


def BrowsUp(Key, Score):
    if Score >= ACCEPTABLE_BROWS_SCORE and InputFlagArray[6] == False:
        SendInputToPC(Key, True)
        InputFlagArray[6] = True
    elif Score < ACCEPTABLE_BROWS_SCORE and InputFlagArray[6] == True:
        SendInputToPC(Key, False)
        InputFlagArray[6] = False


def HeadTrackingForMouse(Landmarks):
    faceCenterX = (Landmarks[123].x + Landmarks[352].x) / 2
    faceCenterY = (Landmarks[152].y + Landmarks[10].y) / 2

    xDiff = (faceCenterX - Landmarks[4].x) * 1000
    yDiff = -(faceCenterY - Landmarks[4].y) * 1000


def HeadTrackingForMovement(Type, Landmarks):
    print("cocks")


def HeadTracking(Type, Landmarks):
    if Type == 3:
        HeadTrackingForMouse(Landmarks)
    else:
        HeadTrackingForMovement(Type,Landmarks)

# def EyeTracking():
