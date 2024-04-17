import win32api
import win32con
import keyboard
import math
import time

ACCEPTABLE_MOUTH_SCORE = 200
ACCEPTABLE_EYE_WIDE_SCORE = 35
ACCEPTABLE_BROWS_SCORE = 300
ACCEPTABLE_MOUTH_OPEN_SCORE = 1

InputFlagArray = [False, False, False, False, False, False, False]

flag = 0


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


def FaceLeft(Key, Landmarks):
    faceCenterX = (Landmarks[123].x + Landmarks[352].x) / 2
    xDiff = int((faceCenterX - Landmarks[4].x) * 1000)

    if xDiff <= 0 and abs(xDiff) >= 10 and InputFlagArray[0] == False:
        SendInputToPC(Key, True)
        InputFlagArray[0] = True
    elif xDiff <= 0 and abs(xDiff) <= 10 and InputFlagArray[0] == True:
        SendInputToPC(Key, False)
        InputFlagArray[0] = False


def FaceRight(Key, Landmarks):
    faceCenterX = (Landmarks[123].x + Landmarks[352].x) / 2
    xDiff = int((faceCenterX - Landmarks[4].x) * 1000)

    if xDiff >= 0 and abs(xDiff) >= 10 and InputFlagArray[1] == False:
        SendInputToPC(Key, True)
        InputFlagArray[1] = True
    elif xDiff >= 0 and abs(xDiff) <= 10 and InputFlagArray[1] == True:
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

    xDiff = int((faceCenterX - Landmarks[4].x) * 1000)
    yDiff = -int((faceCenterY - Landmarks[4].y) * 1000)

    if xDiff > 0:
        xChange = 1
    else:
        xChange = -1

    if yDiff > 0:
        yChange = 1
    else:
        yChange = -1

    i = 0
    j = 0
    if abs(xDiff) >= 8 or abs(yDiff) >= 8:
        while i != xDiff or j != yDiff:
            if i != xDiff:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, xChange, 0)
                i += xChange
            if j != yDiff:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, yChange)
                j += yChange
            time.sleep(0.0002)


def HeadTrackingForMovement(Type, Landmarks):
    faceCenterY = (Landmarks[152].y + Landmarks[10].y) / 2
    yDiff = -int((faceCenterY - Landmarks[4].y) * 1000)

    tilt = int((Landmarks[10].x - Landmarks[152].x) * 1000)
    print(Type)

    if abs(yDiff) >= 8:
        if yDiff >= 0:
            if Type == 1:
                keyboard.press('s')
            else:
                keyboard.press('w')
        else:
            if Type == 1:
                keyboard.press('w')
            else:
                keyboard.press('s')
    else:
        keyboard.release('w')
        keyboard.release('s')

    if abs(tilt) >= 50:
        if tilt >= 0:
            keyboard.press('a')
        else:
            keyboard.press('d')
    else:
        keyboard.release('a')
        keyboard.release('d')


def HeadTracking(Type, Landmarks):
    if Type == 3:
        HeadTrackingForMouse(Landmarks)
    else:
        HeadTrackingForMovement(Type, Landmarks)


distUpThresh = 0
distDownThresh = 0


def EyeTracking(Landmarks):
    global distUpThresh, distDownThresh
    lx = int((Landmarks[130].x * 640) * 1000)
    rx = int((Landmarks[133].x * 640) * 1000)
    uy = int((Landmarks[104].y * 480) * 1000)
    by = int((Landmarks[230].y * 480) * 1000)

    mx = int((Landmarks[468].x * 640) * 1000)
    my = int((Landmarks[159].y * 480) * 1000)

    distLeft = abs(lx - mx)
    distRight = abs(rx - mx)

    distUp = abs(uy - my)
    distDown = abs(by - my)

    if keyboard.is_pressed('e'):
        distUpThresh = distUp
    if keyboard.is_pressed('r'):
        distDownThresh = distDown

    if abs(distLeft - distRight) >= 100000:
        if distLeft > distRight:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -10, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 10, 0)
    if abs(distUp - distDown) >= 400:
        if distUp <= distUpThresh:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -10)
        elif distDown >= distDownThresh != 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 10)
