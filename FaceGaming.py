import threading
import GUI.GUI as GUI
from Services import FaceDetector


############################################################################
def main():
    # Run the face detection module on a separate thread
    threading.Thread(target=FaceDetector.DetectFaceLandmarks).start()

    # Start GUI menu
    GUI.GUI_Main()
############################################################################


if __name__ == "__main__":
    main()
