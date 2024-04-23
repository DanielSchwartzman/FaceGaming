import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
import InputController
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory(name="KeyBindingMapping", size=13, create=False)

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

flag = True
ActivationFlag = False
ReleaseFlag = False


def CalculateResult(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global shared_mem, ActivationFlag, ReleaseFlag
    if len(result.face_landmarks) >= 1:
        if ActivationFlag:
            if shared_mem.buf[1] != 0:
                InputController.FaceLeft(shared_mem.buf[1], result.face_landmarks[0])
            if shared_mem.buf[2] != 0:
                InputController.FaceRight(shared_mem.buf[2], result.face_landmarks[0])
            if shared_mem.buf[3] != 0:
                InputController.MouthLeft(shared_mem.buf[3], result.face_blendshapes[0][33].score * 1000)
            if shared_mem.buf[4] != 0:
                InputController.MouthRight(shared_mem.buf[4], result.face_blendshapes[0][39].score * 1000)
            if shared_mem.buf[5] != 0:
                InputController.MouthOpen(shared_mem.buf[5], result.face_blendshapes[0][27].score * 1000)
            if shared_mem.buf[6] != 0:
                InputController.EyeWide(shared_mem.buf[6], (
                        result.face_blendshapes[0][21].score + result.face_blendshapes[0][22].score) * 1000)
            if shared_mem.buf[7] != 0:
                InputController.BrowsUp(shared_mem.buf[7], result.face_blendshapes[0][3].score * 1000)
            if shared_mem.buf[8] != 0:
                InputController.HeadTracking(shared_mem.buf[8], result.face_landmarks[0])
            if shared_mem.buf[9] != 0:
                InputController.EyeTracking(result.face_landmarks[0])
        if result.face_blendshapes[0][27].score * 1000 > 0.9 and (
                result.face_blendshapes[0][1].score + result.face_blendshapes[0][
            2].score) * 1000 > 200 and not ReleaseFlag:
            ActivationFlag = not ActivationFlag
            ReleaseFlag = True
        elif result.face_blendshapes[0][27].score * 1000 < 0.9 and (
                result.face_blendshapes[0][1].score + result.face_blendshapes[0][2].score) * 1000 < 200 and ReleaseFlag:
            ReleaseFlag = False


options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="face_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=CalculateResult,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True)


def findAvailableCameras():
    flg = True
    CamIndex = 0
    NumOfCameras = 0
    while flg:
        cap = cv2.VideoCapture(CamIndex, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1)
        ret, frame = cap.read()
        if ret:
            NumOfCameras += 1
            CamIndex += 1
        else:
            flg = False
    shared_mem.buf[11] = NumOfCameras


def DetectFaceLandmarks():
    findAvailableCameras()
    CurrCamera = shared_mem.buf[12]
    cap = cv2.VideoCapture(CurrCamera, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    with FaceLandmarker.create_from_options(options) as landmarker:
        while flag:
            if CurrCamera != shared_mem.buf[12]:
                CurrCamera = shared_mem.buf[12]
                cap = cv2.VideoCapture(CurrCamera, cv2.CAP_DSHOW)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            ms = time.time() * 1000
            ret, frame = cap.read()
            if ret:
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
                landmarker.detect_async(mp_image, int(ms))
                cv2.imshow("FaceGaming", frame)
            key = cv2.waitKey(1)
            if key == ord('q') or shared_mem.buf[10] == 1:
                break
        cv2.destroyAllWindows()


if __name__ == "__main__":
    DetectFaceLandmarks()
