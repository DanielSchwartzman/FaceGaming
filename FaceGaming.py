import win32api
import win32con
import keyboard
import cv2
import FaceDetector
import GUI


def main():
    GUI.GUI_Main()
    while True:
        faceLandmarks, frame = FaceDetector.GetFaceLandmarkArray()
        if len(faceLandmarks) > 0:
            print("Facial landmarks found")

        cv2.imshow("FaceGaming", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
