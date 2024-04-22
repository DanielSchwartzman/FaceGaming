import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
import InputController
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory(name="KeyBindingMapping", size=11, create=False)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

flag = True


def CalculateResult(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global shared_mem
    if len(result.face_landmarks) >= 1:
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


options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="face_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=CalculateResult,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True)


def DetectFaceLandmarks():
    with FaceLandmarker.create_from_options(options) as landmarker:
        while flag:
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
