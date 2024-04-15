import FaceDetector
import sys
sys.path.append("GUI/")
import GUI


def main():
    GUI.GUI_Main()
    FaceDetector.DetectFaceLandmarks(GUI.KeyBindingTaken, GUI.MouseAndWSADTaken)


if __name__ == "__main__":
    main()
