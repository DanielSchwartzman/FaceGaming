import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
import InputController

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

flag = True

KeyBindMapping = []
MouseAndWSADMapping = []


def CalculateResult(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    if len(result.face_landmarks) >= 1:
        if KeyBindMapping[1] != 0:
            InputController.FaceLeft(KeyBindMapping[1], result.face_blendshapes[0][13].score * 1000)
        if KeyBindMapping[2] != 0:
            InputController.FaceRight(KeyBindMapping[2], result.face_blendshapes[0][14].score * 1000)
        if KeyBindMapping[3] != 0:
            InputController.MouthLeft(KeyBindMapping[3], result.face_blendshapes[0][33].score * 1000)
        if KeyBindMapping[4] != 0:
            InputController.MouthRight(KeyBindMapping[4], result.face_blendshapes[0][39].score * 1000)
        if KeyBindMapping[5] != 0:
            InputController.MouthOpen(KeyBindMapping[5], result.face_blendshapes[0][27].score * 1000)
        if KeyBindMapping[6] != 0:
            InputController.EyeWide(KeyBindMapping[6],
                                (result.face_blendshapes[0][21].score + result.face_blendshapes[0][22].score) * 1000)
        if KeyBindMapping[7] != 0:
            InputController.BrowsUp(KeyBindMapping[7], result.face_blendshapes[0][3].score * 1000)
        if MouseAndWSADMapping[0] != 0:
            InputController.HeadTracking(MouseAndWSADMapping[0], result.face_landmarks[0])
    # if MouseAndWSADMapping[1] != 0:
    # InputController.EyeTracking()


options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="face_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=CalculateResult,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True)


def DetectFaceLandmarks(KeyBindingTaken, MouseAndWSADTaken):
    global KeyBindMapping, MouseAndWSADMapping
    KeyBindMapping = KeyBindingTaken
    MouseAndWSADMapping = MouseAndWSADTaken
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
