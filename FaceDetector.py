import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


class FaceMeshDetector:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

    def findFaceMesh(self, frame):
        faceLandmarks = []
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = self.face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        if landmark_points is not None:
            landmarks = landmark_points[0].landmark
            for lm in landmarks:
                ih, iw, ic = frame.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                faceLandmarks.append([x, y])
        return faceLandmarks


def GetFaceLandmarkArray():
    ret, frame = cap.read()
    detector = FaceMeshDetector()
    return detector.findFaceMesh(frame), frame
