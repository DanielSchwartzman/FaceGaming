import sys
import os
from multiprocessing import shared_memory
shared_mem = shared_memory.SharedMemory(name="KeyBindingMapping", size=11, create=True)
import GUI.GUI as GUI


# Shared_mem indexes correspond to:
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


def main():
    global shared_mem
    os.startfile("FaceDetector.py")
    GUI.GUI_Main()


if __name__ == "__main__":
    main()
