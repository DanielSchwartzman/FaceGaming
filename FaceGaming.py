import threading
import GUI.GUI as GUI
import FaceDetector

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
# 9 = "EyeTracking"
# 10 = "Process state flag on/off"
# 11 = "Num of available cameras"
# 12 = "Current Chosen Camera"


def main():
    threading.Thread(target=FaceDetector.DetectFaceLandmarks).start()
    GUI.GUI_Main()


if __name__ == "__main__":
    main()
