from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as bs

GUI = bs.Window(themename="cerculean")
GUI.title("FaceGaming")
GUI.resizable(False, False)
GUI.geometry("480x320")
GUI.iconbitmap("res/Icons/FaceGamingIcon.ico")
WindowFrame = bs.Frame(GUI, width=640, height=700)

s = bs.Style()
s.configure('my.Tframe', background="#B1EBF7")


def DestroyPreviousFrame():
    for frame in WindowFrame.winfo_children():
        frame.destroy()


def EyeCalibrationFrameInit():
    DestroyPreviousFrame()
    EyeCalibrationFrame = bs.Frame(WindowFrame, width=640, height=700)
    EyeCalibrationFrame.pack(side=TOP)


def MouseBindFrameInit():
    DestroyPreviousFrame()
    MouseBindFrame = bs.Frame(WindowFrame, width=640, height=700)
    MouseBindFrame.pack(side=TOP)

    MouseOption = ["Default", "Eye Tracking", "Head Tracking"]
    MouseSelectComboBox = bs.Combobox(MouseBindFrame, values=MouseOption, state='readonly')
    MouseSelectComboBox.current(0)
    MouseSelectLabel = bs.Label(MouseBindFrame, text="Mouse movement method:", font=("Arial", 12))
    MouseSelectLabel.place(x=20, y=75)
    MouseSelectComboBox.place(x=220, y=71.5)

    MouseLeftClickOption = ["Default", "Left cheek up", "Left eye blink"]
    MouseLeftClickComboBox = bs.Combobox(MouseBindFrame, values=MouseLeftClickOption, state='readonly')
    MouseLeftClickComboBox.current(0)
    MouseLeftClickLabel = bs.Label(MouseBindFrame, text="Mouse Left click trigger:", font=("Arial", 12))
    MouseLeftClickLabel.place(x=20, y=115)
    MouseLeftClickComboBox.place(x=220, y=111.5)

    MouseRightClickOption = ["Default", "Right cheek up", "Right eye blink"]
    MouseRightClickComboBox = bs.Combobox(MouseBindFrame, values=MouseRightClickOption, state='readonly')
    MouseRightClickComboBox.current(0)
    MouseRightClickLabel = bs.Label(MouseBindFrame, text="Mouse Right click trigger:", font=("Arial", 12))
    MouseRightClickLabel.place(x=20, y=155)
    MouseRightClickComboBox.place(x=220, y=151.5)


def KeyboardFrameInit():
    DestroyPreviousFrame()
    KeyboardBindFrame = bs.Frame(WindowFrame, width=640, height=700)
    KeyboardBindFrame.pack(side=TOP)

    MovementOption = ["Default", "Head Tracking (forward up)", "Head Tracking (forward down)"]
    MovementSelectComboBox = bs.Combobox(KeyboardBindFrame, values=MovementOption, state='readonly', width=27)
    MovementSelectComboBox.current(0)
    MovementSelectLabel = bs.Label(KeyboardBindFrame, text="Movement method (WSAD):", font=("Arial", 12))
    MovementSelectLabel.place(x=20, y=75)
    MovementSelectComboBox.place(x=230, y=71.5)

    SpaceBarOption = ["Default", "Mouth open"]
    SpaceBarSelectComboBox = bs.Combobox(KeyboardBindFrame, values=SpaceBarOption, state='readonly')
    SpaceBarSelectComboBox.current(0)
    SpaceBarSelectLabel = bs.Label(KeyboardBindFrame, text="Spacebar input method:", font=("Arial", 12))
    SpaceBarSelectLabel.place(x=20, y=115)
    SpaceBarSelectComboBox.place(x=230, y=111.5)

    CtrlOption = ["Default", "Face look left", "Face look right"]
    CtrlSelectComboBox = bs.Combobox(KeyboardBindFrame, values=CtrlOption, state='readonly')
    CtrlSelectComboBox.current(0)
    CtrlSelectLabel = bs.Label(KeyboardBindFrame, text="Control (Button) input method:", font=("Arial", 12))
    CtrlSelectLabel.place(x=20, y=155)
    CtrlSelectComboBox.place(x=230, y=151.5)

    EOption = ["Default", "Face look left", "Face look right"]
    ESelectComboBox = bs.Combobox(KeyboardBindFrame, values=EOption, state='readonly')
    ESelectComboBox.current(0)
    ESelectLabel = bs.Label(KeyboardBindFrame, text="Interact (Button) input method:", font=("Arial", 12))
    ESelectLabel.place(x=20, y=195)
    ESelectComboBox.place(x=230, y=191.5)


def OptionsFrameInit():
    DestroyPreviousFrame()
    OptionsFrame = bs.Frame(WindowFrame, width=640, height=700)
    OptionsFrame.pack(side=TOP)


def SelectFrameInit():
    SelectFrame = bs.Frame(GUI, width=640, height=50)
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
    LineFrame = bs.Frame(GUI, width=640, height=1, relief="solid")
    LineFrame.pack(side=TOP)


def GUI_Main():
    SelectFrameInit()
    WindowFrame.pack(side=TOP)

    GUI.mainloop()


if __name__ == "__main__":
    GUI_Main()
