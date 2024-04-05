import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
import math

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

flag = True


def Distance(firstX, firstY, secondX, secondY):
    return math.sqrt(math.pow(firstX - secondX, 2) + math.pow(firstY - secondY, 2))*1000


def print_result(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print((result.face_blendshapes[0][21].score + result.face_blendshapes[0][22].score)*1000)
    if result.face_blendshapes[0][33].score >= 0.3:
        print("Mouth left Detected")
    elif result.face_blendshapes[0][39].score >= 0.3:
        print("Mouth right Detected")
    else:
        print("Not Detected")


options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="face_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
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
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
