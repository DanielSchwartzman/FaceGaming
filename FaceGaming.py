import win32api
import win32con
import keyboard
import FaceDetector
import GUI.GUI as GUI


def main():
    GUI.GUI_Main()
    FaceDetector.DetectFaceLandmarks()


if __name__ == "__main__":
    main()

