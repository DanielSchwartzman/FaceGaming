import cv2
import mediapipe as mp
import win32api
import win32con
import keyboard

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


class FaceMeshDetector:
    def __init__(self):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh()
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, frame):
        imgRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRgb)
        face = []
        if results.multi_face_landmarks:
            for faceLm in results.multi_face_landmarks:
                for lm in faceLm.landmark:
                    ih, iw, ic = frame.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
        return frame, face


def main():
    detector = FaceMeshDetector()

    while True:
        ret, frame = cap.read()
        frame, face = detector.findFaceMesh(frame)
        if len(face) > 0:
            faceCenterX = (face[123][0] + face[352][0]) / 2
            faceCenterY = (face[152][1] + face[151][1]) / 2

            xDiff = int(faceCenterX - face[4][0])
            yDiff = -int(faceCenterY - face[4][1])
            print(xDiff, yDiff)

            if abs(yDiff) > 5:
                keyboard.press('shift')
            else:
                keyboard.release('shift')

            if abs(yDiff) < 2.5:
                keyboard.release('w')
                keyboard.release('s')
            elif yDiff < 0:
                keyboard.press('s')
                keyboard.release('w')
            elif yDiff > 0:
                keyboard.press('w')
                keyboard.release('s')

            if abs(xDiff) < 5:
                keyboard.release('d')
                keyboard.release('a')
            elif xDiff < 0:
                keyboard.press('a')
                keyboard.release('d')
            elif xDiff > 0:
                keyboard.press('d')
                keyboard.release('a')

        cv2.imshow("FaceGaming", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
