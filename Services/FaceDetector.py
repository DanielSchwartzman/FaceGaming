import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
from Services import InputController
from Utils import DataManager

############################################################################
# Mediapipe initialization parameters
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode
############################################################################


############################################################################
# OpenCV initialization parameters
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
############################################################################


############################################################################
# Global parameters
flag = True
ActivationFlag = False
ReleaseFlag = False
lock = 0
############################################################################


############################################################################
def CalculateResult(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    """
    Mediapipe callback method, for each frame we send Mediapipe,
    Mediapipe finds and extracts Facial landmarks and BlendShapes(Facial gestures).
    """
    global ActivationFlag, ReleaseFlag, lock
    if len(result.face_landmarks) >= 1:
        if DataManager.KeyMapping[9] == 1:
            if abs(result.face_landmarks[0][11].y * 480 - result.face_landmarks[0][16].y * 480) > 30 and (
                    result.face_blendshapes[0][1].score + result.face_blendshapes[0][
                2].score) * 1000 > 200 and not ReleaseFlag:
                ActivationFlag = not ActivationFlag
                ReleaseFlag = True
            elif abs(result.face_landmarks[0][11].y * 480 - result.face_landmarks[0][16].y * 480) < 30 and (
                    result.face_blendshapes[0][1].score + result.face_blendshapes[0][
                2].score) * 1000 < 200 and ReleaseFlag:
                ReleaseFlag = False

            if DataManager.KeyMapping[1] != 0:
                InputController.FaceLeft(DataManager.KeyMapping[1], result.face_landmarks[0])
            if DataManager.KeyMapping[2] != 0:
                InputController.FaceRight(DataManager.KeyMapping[2], result.face_landmarks[0])
            if DataManager.KeyMapping[3] != 0:
                InputController.MouthLeft(DataManager.KeyMapping[3], result.face_blendshapes[0][33].score * 1000)
            if DataManager.KeyMapping[4] != 0:
                InputController.MouthRight(DataManager.KeyMapping[4], result.face_blendshapes[0][39].score * 1000)
            if DataManager.KeyMapping[5] != 0:
                InputController.MouthOpen(DataManager.KeyMapping[5], result.face_landmarks[0])
            if DataManager.KeyMapping[6] != 0:
                InputController.EyeWide(DataManager.KeyMapping[6], (
                        result.face_blendshapes[0][21].score + result.face_blendshapes[0][22].score) * 1000)
            if DataManager.KeyMapping[7] != 0:
                InputController.BrowsUp(DataManager.KeyMapping[7], result.face_blendshapes[0][3].score * 1000)
            if DataManager.KeyMapping[8] != 0:
                InputController.HeadTracking(DataManager.KeyMapping[8], result.face_landmarks[0], ActivationFlag)
    lock = False
############################################################################


############################################################################
# Additional Mediapipe parameters
options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="Services/face_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=CalculateResult,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True)
############################################################################


############################################################################
def findAvailableCameras():
    """
    Function to find how many cameras the user has, by trying to access every possible camera
    index and if we get an image, increment the amount of available camera devices.
    """
    global cap
    flg = True
    CamIndex = 0
    while flg:
        cap = cv2.VideoCapture(CamIndex, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        ret, frame = cap.read()
        if ret:
            DataManager.KeyMapping[11] += 1
            CamIndex += 1
        else:
            flg = False
        cv2.destroyAllWindows()
    DataManager.IsCamReady = True
############################################################################


############################################################################
def DetectFaceLandmarks():
    """
    Main detection function, Takes a frame(What the camera currently sees) and sends it to the Mediapipe SDK
    Runs infinitely or until the GUI window is destroyed
    """

    global cap, lock
    findAvailableCameras()
    DataManager.KeyMapping[12] = 0
    CurrCamera = 0
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    with FaceLandmarker.create_from_options(options) as landmarker:
        while flag:
            if CurrCamera != DataManager.KeyMapping[12]:
                CurrCamera = DataManager.KeyMapping[12]
                cap = cv2.VideoCapture(CurrCamera, cv2.CAP_DSHOW)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            ms = time.time() * 1000
            ret, frame = cap.read()
            if ret:
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
                if not DataManager.IsMinimized:
                    DataManager.Frame = frame
                if not lock:
                    lock = True
                    landmarker.detect_async(mp_image, int(ms))
            if DataManager.KeyMapping[10] == 1:
                break
        cv2.destroyAllWindows()
############################################################################


if __name__ == "__main__":
    DetectFaceLandmarks()
