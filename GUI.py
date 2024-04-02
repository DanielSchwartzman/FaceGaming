from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as bs

GUI = bs.Window(themename="cerculean")
GUI.title("FaceGaming")
GUI.resizable(False,False)
GUI.geometry("1080x720")
GUI.iconbitmap("res/Icons/FaceGamingIcon.ico")
WindowFrame = bs.Frame(GUI, width=1080, height=700)

s = bs.Style()
s.configure('my.Tframe', background="#B1EBF7")


def DestroyPreviousFrame():
    for frame in WindowFrame.winfo_children():
        frame.destroy()


def EyeCalibrationFrameInit():
    DestroyPreviousFrame()
    EyeCalibrationFrame = bs.Frame(WindowFrame, width=1080, height=700)
    EyeCalibrationFrame.pack(side=TOP)
    lbl1 = Label(EyeCalibrationFrame, text="Botten")
    lbl1.place(x=10, y=500)


def MouseBindFrameInit():
    DestroyPreviousFrame()
    MouseBindFrame = bs.Frame(WindowFrame, width=1080, height=700)
    MouseBindFrame.pack(side=TOP)
    lbl2 = Label(MouseBindFrame, text="Cock")
    lbl2.place(x=100, y=500)


def KeyboardFrameInit():
    DestroyPreviousFrame()
    KeyboardBindFrame = bs.Frame(WindowFrame, width=1080, height=700)
    KeyboardBindFrame.pack(side=TOP)
    lbl3 = Label(KeyboardBindFrame, text="Boiler")
    lbl3.place(x=200, y=500)


def OptionsFrameInit():
    DestroyPreviousFrame()
    OptionsFrame = bs.Frame(WindowFrame, width=1080, height=700)
    OptionsFrame.pack(side=TOP)
    lbl4 = Label(OptionsFrame, text="Beer")
    lbl4.place(x=300, y=500)


def SelectFrameInit():
    SelectFrame = bs.Frame(GUI, width=1080, height=50)
    SelectFrame.pack(side=TOP)
    EyeCalibrationButton = bs.Radiobutton(SelectFrame, text="Eye Calibration", bootstyle="default, toolbutton, outline", value=0,
                                     command=EyeCalibrationFrameInit)
    MouseBindButton = bs.Radiobutton(SelectFrame, text="Mouse binds", bootstyle="default, toolbutton, outline", value=1,
                                command=MouseBindFrameInit)
    KeyboardBindButton = bs.Radiobutton(SelectFrame, text="Keyboard binds", bootstyle="default, toolbutton, outline", value=2,
                                   command=KeyboardFrameInit)
    OptionsButton = bs.Radiobutton(SelectFrame, text="Options", bootstyle="default, toolbutton, outline", value=4, command=OptionsFrameInit)
    EyeCalibrationButton.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))
    MouseBindButton.grid(column=1, row=0, padx=(5, 5), pady=(5, 5))
    KeyboardBindButton.grid(column=2, row=0, padx=(5, 5), pady=(5, 5))
    OptionsButton.grid(column=3, row=0, padx=(5, 5), pady=(5, 5))
    LineFrame = bs.Frame(GUI, width=5000, height=1, relief="solid")
    LineFrame.pack(side=TOP)


def GUI_Main():
    SelectFrameInit()
    WindowFrame.pack(side=TOP)

    GUI.mainloop()


if __name__ == "__main__":
    GUI_Main()
