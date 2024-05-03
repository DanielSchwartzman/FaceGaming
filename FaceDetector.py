import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
import InputController
import DataManager

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

flag = True
ActivationFlag = False
ReleaseFlag = False

lock = False


def CalculateResult(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global ActivationFlag, ReleaseFlag, lock
    if len(result.face_landmarks) >= 1:
        if ActivationFlag:
            if DataManager.KeyMapping[1] != 0:
                InputController.FaceLeft(DataManager.KeyMapping[1], result.face_landmarks[0])
            if DataManager.KeyMapping[2] != 0:
                InputController.FaceRight(DataManager.KeyMapping[2], result.face_landmarks[0])
            if DataManager.KeyMapping[3] != 0:
                InputController.MouthLeft(DataManager.KeyMapping[3], result.face_blendshapes[0][33].score * 1000)
            if DataManager.KeyMapping[4] != 0:
                InputController.MouthRight(DataManager.KeyMapping[4], result.face_blendshapes[0][39].score * 1000)
            if DataManager.KeyMapping[5] != 0:
                InputController.MouthOpen(DataManager.KeyMapping[5], result.face_blendshapes[0][27].score * 1000)
            if DataManager.KeyMapping[6] != 0:
                InputController.EyeWide(DataManager.KeyMapping[6], (
                        result.face_blendshapes[0][21].score + result.face_blendshapes[0][22].score) * 1000)
            if DataManager.KeyMapping[7] != 0:
                InputController.BrowsUp(DataManager.KeyMapping[7], result.face_blendshapes[0][3].score * 1000)
            if DataManager.KeyMapping[8] != 0:
                InputController.HeadTracking(DataManager.KeyMapping[8], result.face_landmarks[0])
            if DataManager.KeyMapping[9] != 0:
                InputController.EyeTracking(result.face_landmarks[0])
        if result.face_blendshapes[0][27].score * 1000 > 0.9 and (
                result.face_blendshapes[0][1].score + result.face_blendshapes[0][
            2].score) * 1000 > 200 and not ReleaseFlag:
            ActivationFlag = not ActivationFlag
            ReleaseFlag = True
        elif result.face_blendshapes[0][27].score * 1000 < 0.9 and (
                result.face_blendshapes[0][1].score + result.face_blendshapes[0][2].score) * 1000 < 200 and ReleaseFlag:
            ReleaseFlag = False
        lock = False


options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="face_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=CalculateResult,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True)


def findAvailableCameras():
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


def DetectFaceLandmarks():
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
            key = cv2.waitKey(1)
            if key == ord('q') or DataManager.KeyMapping[10] == 1:
                break
        cv2.destroyAllWindows()


if __name__ == "__main__":
    DetectFaceLandmarks()
