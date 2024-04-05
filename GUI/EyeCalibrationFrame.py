from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as bs


def EyeCalibrationFrameInit(WindowFrame):
    EyeCalibrationFrame = bs.Frame(WindowFrame, width=640, height=700)
    EyeCalibrationFrame.pack(side=TOP)
