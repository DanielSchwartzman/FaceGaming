from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as bs
from ttkbootstrap.toast import ToastNotification

MouseMovement = 0
LeftClick = 0
RightClick = 0

KeyBindingOptions = ["Default", "Face Left", "Face Right", "Mouth Left", "Mouth Right", "Mouth Open", "Eye wide",
                     "Brows up"]


def DisplayErrorToast():
    toast = ToastNotification(
        title="ERROR",
        message="The Keybind you selected has already been assigned",
        position=(400, 300, "n"),
        alert=True,
        duration=3000,
        bootstyle=DANGER
    )
    toast.show_toast()


def MouseMovementSelect(ComboBox, HeadTrackingTaken):
    global MouseMovement
    if HeadTrackingTaken[0] == 1 and ComboBox.current() == 2:
        DisplayErrorToast()
        ComboBox.current(MouseMovement)
    else:
        MouseMovement = ComboBox.current()
        if MouseMovement == 2:
            HeadTrackingTaken[0] = 1
        else:
            HeadTrackingTaken[0] = 0
    return 'break'


def LeftClickSelect(ComboBox, KeyBindingTaken):
    global LeftClick
    if KeyBindingTaken[ComboBox.current()] == 1:
        DisplayErrorToast()
        ComboBox.current(LeftClick)
    else:
        KeyBindingTaken[LeftClick] = 1
        LeftClick = ComboBox.current()
        KeyBindingTaken[ComboBox.current()] = 1
    return 'break'


def RightClickSelect(ComboBox, KeyBindingTaken):
    global RightClick
    if KeyBindingTaken[ComboBox.current()] == 1:
        DisplayErrorToast()
        ComboBox.current(RightClick)
    else:
        KeyBindingTaken[RightClick] = 1
        RightClick = ComboBox.current()
        KeyBindingTaken[ComboBox.current()] = 1
    return 'break'


def MouseBindFrameInit(WindowFrame, KeyBindingTaken, HeadTrackingTaken):
    MouseBindFrame = bs.Frame(WindowFrame, width=640, height=700)
    MouseBindFrame.pack(side=TOP)

    # Mouse movement Selection
    MouseOption = ["Default", "Eye Tracking", "Head Tracking"]
    MouseSelectComboBox = bs.Combobox(MouseBindFrame, values=MouseOption, state='readonly')
    MouseSelectComboBox.current(MouseMovement)
    MouseSelectComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MouseSelectComboBox: MouseMovementSelect(
        ComboBox=entry, HeadTrackingTaken=HeadTrackingTaken))
    MouseSelectLabel = bs.Label(MouseBindFrame, text="Mouse movement method:", font=("Arial", 12))
    MouseSelectLabel.place(x=20, y=75)
    MouseSelectComboBox.place(x=220, y=71.5)

    # Left click Selection
    MouseLeftClickComboBox = bs.Combobox(MouseBindFrame, values=KeyBindingOptions, state='readonly')
    MouseLeftClickComboBox.current(LeftClick)
    MouseLeftClickComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MouseLeftClickComboBox: LeftClickSelect(
        ComboBox=entry, KeyBindingTaken=KeyBindingTaken))
    MouseLeftClickLabel = bs.Label(MouseBindFrame, text="Mouse Left click trigger:", font=("Arial", 12))
    MouseLeftClickLabel.place(x=20, y=115)
    MouseLeftClickComboBox.place(x=220, y=111.5)

    # Right click Selection
    MouseRightClickComboBox = bs.Combobox(MouseBindFrame, values=KeyBindingOptions, state='readonly')
    MouseRightClickComboBox.current(RightClick)
    MouseRightClickComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MouseRightClickComboBox: RightClickSelect(
        ComboBox=entry, KeyBindingTaken=KeyBindingTaken))
    MouseRightClickLabel = bs.Label(MouseBindFrame, text="Mouse Right click trigger:", font=("Arial", 12))
    MouseRightClickLabel.place(x=20, y=155)
    MouseRightClickComboBox.place(x=220, y=151.5)
