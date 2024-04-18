import ttkbootstrap as bs
from ttkbootstrap.constants import *
import OptionsFrame
import EyeCalibrationFrame
import KeyBoardFrame
import MouseBindFrame
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory(name="KeyBindingMapping", size=11, create=False)

GUIFrame = bs.Window(themename="cerculean")
GUIFrame.title("FaceGaming")
GUIFrame.resizable(False, False)
GUIFrame.geometry("480x320")
GUIFrame.iconbitmap("res/Icons/FaceGamingIcon.ico")

WindowFrame = bs.Frame(GUIFrame, width=640, height=700)


def DestroyPreviousFrame():
    for frame in WindowFrame.winfo_children():
        frame.destroy()


def EyeCalibrationFrameInit():
    DestroyPreviousFrame()
    EyeCalibrationFrame.EyeCalibrationFrameInit(WindowFrame)


def MouseBindFrameInit():
    DestroyPreviousFrame()
    MouseBindFrame.MouseBindFrameInit(WindowFrame)


def KeyboardFrameInit():
    DestroyPreviousFrame()
    KeyBoardFrame.KeyboardFrameInit(WindowFrame)


def OptionsFrameInit():
    DestroyPreviousFrame()
    OptionsFrame.OptionsFrameInit(WindowFrame)


def SelectFrameInit():
    SelectFrame = bs.Frame(GUIFrame, width=640, height=50)
    SelectFrame.pack(side=TOP)
    EyeCalibrationButton = bs.Radiobutton(SelectFrame, text="Eye Calibration", bootstyle="default, toolbutton, outline",
                                          value=0,
                                          command=EyeCalibrationFrameInit)
    MouseBindButton = bs.Radiobutton(SelectFrame, text="Mouse binds", bootstyle="default, toolbutton, outline", value=1,
                                     command=MouseBindFrameInit)
    KeyboardBindButton = bs.Radiobutton(SelectFrame, text="Keyboard binds", bootstyle="default, toolbutton, outline",
                                        value=2,
                                        command=KeyboardFrameInit)
    OptionsButton = bs.Radiobutton(SelectFrame, text="Options", bootstyle="default, toolbutton, outline", value=4,
                                   command=OptionsFrameInit)
    EyeCalibrationButton.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))
    MouseBindButton.grid(column=1, row=0, padx=(5, 5), pady=(5, 5))
    KeyboardBindButton.grid(column=2, row=0, padx=(5, 5), pady=(5, 5))
    OptionsButton.grid(column=3, row=0, padx=(5, 5), pady=(5, 5))
    LineFrame = bs.Frame(GUIFrame, width=640, height=1, relief="solid")
    LineFrame.pack(side=TOP)


def GUI_Main():
    global shared_mem
    SelectFrameInit()
    WindowFrame.pack(side=TOP)
    GUIFrame.mainloop()


if __name__ == "__main__":
    GUI_Main()
