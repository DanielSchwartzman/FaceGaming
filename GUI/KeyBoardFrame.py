from ttkbootstrap.constants import *
import ttkbootstrap as bs
from ttkbootstrap.toast import ToastNotification
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory(name="KeyBindingMapping", size=11, create=False)

WASDMovement = 0
Space = 0
Ctrl = 0
Interact = 0

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


def WASDSelect(ComboBox):
    global WASDMovement, shared_mem
    if shared_mem.buf[8] != 0 and ComboBox.current() != 0 and WASDMovement == 0:
        DisplayErrorToast()
        ComboBox.current(WASDMovement)
    else:
        WASDMovement = ComboBox.current()
        shared_mem.buf[8] = ComboBox.current()
    return 'break'


def InteractSelect(ComboBox):
    global Interact, shared_mem
    if shared_mem.buf[ComboBox.current()] != 0:
        DisplayErrorToast()
        ComboBox.current(Interact)
    else:
        shared_mem.buf[Interact] = 0
        Interact = ComboBox.current()
        shared_mem.buf[ComboBox.current()] = 5
    return 'break'


def CtrlSelect(ComboBox):
    global Ctrl, shared_mem
    if shared_mem.buf[ComboBox.current()] != 0:
        DisplayErrorToast()
        ComboBox.current(Ctrl)
    else:
        shared_mem.buf[Ctrl] = 0
        Ctrl = ComboBox.current()
        shared_mem.buf[ComboBox.current()] = 4
    return 'break'


def SpaceSelect(ComboBox):
    global Space, shared_mem
    if shared_mem.buf[ComboBox.current()] != 0:
        DisplayErrorToast()
        ComboBox.current(Space)
    else:
        shared_mem.buf[Space] = 0
        Space = ComboBox.current()
        shared_mem.buf[ComboBox.current()] = 3
    return 'break'


def KeyboardFrameInit(WindowFrame):
    KeyboardBindFrame = bs.Frame(WindowFrame, width=640, height=700)
    KeyboardBindFrame.pack(side=TOP)

    # WASD movement Selection
    MovementOption = ["Default", "Head Tracking (forward up)", "Head Tracking (forward down)"]
    MovementSelectComboBox = bs.Combobox(KeyboardBindFrame, values=MovementOption, state='readonly', width=27)
    MovementSelectComboBox.current(WASDMovement)
    MovementSelectComboBox.bind('<<ComboboxSelected>>', lambda event, entry=MovementSelectComboBox: WASDSelect(
        ComboBox=entry))
    MovementSelectLabel = bs.Label(KeyboardBindFrame, text="Movement method (WSAD):", font=("Arial", 12))
    MovementSelectLabel.place(x=20, y=75)
    MovementSelectComboBox.place(x=230, y=71.5)

    # SpaceBat Selection
    SpaceBarSelectComboBox = bs.Combobox(KeyboardBindFrame, values=KeyBindingOptions, state='readonly')
    SpaceBarSelectComboBox.current(Space)
    SpaceBarSelectComboBox.bind('<<ComboboxSelected>>', lambda event, entry=SpaceBarSelectComboBox: SpaceSelect(
        ComboBox=entry))
    SpaceBarSelectLabel = bs.Label(KeyboardBindFrame, text="Spacebar input method:", font=("Arial", 12))
    SpaceBarSelectLabel.place(x=20, y=115)
    SpaceBarSelectComboBox.place(x=230, y=111.5)

    # Control Selection
    CtrlSelectComboBox = bs.Combobox(KeyboardBindFrame, values=KeyBindingOptions, state='readonly')
    CtrlSelectComboBox.current(Ctrl)
    CtrlSelectComboBox.bind('<<ComboboxSelected>>', lambda event, entry=CtrlSelectComboBox: CtrlSelect(
        ComboBox=entry))
    CtrlSelectLabel = bs.Label(KeyboardBindFrame, text="Control (Button) input method:", font=("Arial", 12))
    CtrlSelectLabel.place(x=20, y=155)
    CtrlSelectComboBox.place(x=230, y=151.5)

    # Interact Selection
    ESelectComboBox = bs.Combobox(KeyboardBindFrame, values=KeyBindingOptions, state='readonly')
    ESelectComboBox.current(Interact)
    ESelectComboBox.bind('<<ComboboxSelected>>', lambda event, entry=ESelectComboBox: InteractSelect(
        ComboBox=entry))
    ESelectLabel = bs.Label(KeyboardBindFrame, text="Interact (Button) input method:", font=("Arial", 12))
    ESelectLabel.place(x=20, y=195)
    ESelectComboBox.place(x=230, y=191.5)
