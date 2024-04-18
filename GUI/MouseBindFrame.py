from ttkbootstrap.constants import *
import ttkbootstrap as bs
from ttkbootstrap.toast import ToastNotification
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory(name="KeyBindingMapping", size=11, create=False)

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


def MouseMovementSelect(ComboBox):
    global MouseMovement, shared_mem
    if 1 <= shared_mem.buf[8] <= 2 and ComboBox.current() == 2:
        DisplayErrorToast()
        ComboBox.current(MouseMovement)
    else:
        MouseMovement = ComboBox.current()
        shared_mem.buf[9] = 0
        if MouseMovement == 2:
            shared_mem.buf[8] = 3
        elif MouseMovement == 1:
            if shared_mem.buf[8] == 3:
                shared_mem.buf[8] = 0
            shared_mem.buf[9] = 1
        else:
            if shared_mem.buf[8] == 3:
                shared_mem.buf[8] = 0

    return 'break'


def LeftClickSelect(ComboBox):
    global LeftClick, shared_mem
    if shared_mem.buf[ComboBox.current()] != 0:
        DisplayErrorToast()
        ComboBox.current(LeftClick)
    else:
        shared_mem.buf[LeftClick] = 0
        LeftClick = ComboBox.current()
        shared_mem.buf[ComboBox.current()] = 1
    return 'break'


def RightClickSelect(ComboBox):
    global RightClick, shared_mem
    if shared_mem.buf[ComboBox.current()] != 0:
        DisplayErrorToast()
        ComboBox.current(RightClick)
    else:
        shared_mem.buf[RightClick] = 0
        RightClick = ComboBox.current()
        shared_mem.buf[ComboBox.current()] = 2
    return 'break'


def MouseBindFrameInit(WindowFrame):
    MouseBindFrame = bs.Frame(WindowFrame, width=640, height=700)
    MouseBindFrame.pack(side=TOP)

    # Mouse movement Selection
    MouseOption = ["Default", "Eye Tracking", "Head Tracking"]
    MouseSelectComboBox = bs.Combobox(MouseBindFrame, values=MouseOption, state='readonly')
    MouseSelectComboBox.current(MouseMovement)
    MouseSelectComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MouseSelectComboBox: MouseMovementSelect(
        ComboBox=entry))
    MouseSelectLabel = bs.Label(MouseBindFrame, text="Mouse movement method:", font=("Arial", 12))
    MouseSelectLabel.place(x=20, y=75)
    MouseSelectComboBox.place(x=220, y=71.5)

    # Left click Selection
    MouseLeftClickComboBox = bs.Combobox(MouseBindFrame, values=KeyBindingOptions, state='readonly')
    MouseLeftClickComboBox.current(LeftClick)
    MouseLeftClickComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MouseLeftClickComboBox: LeftClickSelect(
        ComboBox=entry))
    MouseLeftClickLabel = bs.Label(MouseBindFrame, text="Mouse Left click trigger:", font=("Arial", 12))
    MouseLeftClickLabel.place(x=20, y=115)
    MouseLeftClickComboBox.place(x=220, y=111.5)

    # Right click Selection
    MouseRightClickComboBox = bs.Combobox(MouseBindFrame, values=KeyBindingOptions, state='readonly')
    MouseRightClickComboBox.current(RightClick)
    MouseRightClickComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MouseRightClickComboBox: RightClickSelect(
        ComboBox=entry))
    MouseRightClickLabel = bs.Label(MouseBindFrame, text="Mouse Right click trigger:", font=("Arial", 12))
    MouseRightClickLabel.place(x=20, y=155)
    MouseRightClickComboBox.place(x=220, y=151.5)
