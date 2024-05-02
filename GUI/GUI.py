from PyQt6 import QtCore, QtGui, QtWidgets
from pyqttoast import Toast, ToastPreset, ToastIcon, ToastPosition, ToastButtonAlignment
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import DbManager
import os
import DataManager
import cv2

user_id = 0


class Ui_MainWindow(object):
    Mouse = 0
    LeftClick = 0
    RightClick = 0
    Interact = 0
    Ctrl = 0
    Space = 0
    WASD = 0
    MainWindow = 0

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 450))
        MainWindow.setMaximumSize(QtCore.QSize(450, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/Icons/FaceGamingIcon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 500, 400))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QWidget{\n"
                                     "rgb(29, 255, 67)\n"
                                     "}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 421, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.LBL_MovemetMethod = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_MovemetMethod.setFont(font)
        self.LBL_MovemetMethod.setObjectName("LBL_MovemetMethod")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_MovemetMethod)
        self.CB_MovemetMethod = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_MovemetMethod.setFont(font)
        self.CB_MovemetMethod.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.CB_MovemetMethod.setPlaceholderText("")
        self.CB_MovemetMethod.setObjectName("CB_MovemetMethod")
        self.CB_MovemetMethod.addItem("")
        self.CB_MovemetMethod.addItem("")
        self.CB_MovemetMethod.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_MovemetMethod)
        self.LBL_Spacebar = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_Spacebar.setFont(font)
        self.LBL_Spacebar.setObjectName("LBL_Spacebar")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_Spacebar)
        self.CB_Spacebar = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_Spacebar.setFont(font)
        self.CB_Spacebar.setObjectName("CB_Spacebar")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.CB_Spacebar.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_Spacebar)
        self.LBL_Control = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_Control.setFont(font)
        self.LBL_Control.setObjectName("LBL_Control")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_Control)
        self.LBL_Interact = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_Interact.setFont(font)
        self.LBL_Interact.setObjectName("LBL_Interact")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_Interact)
        self.CB_Ctrl = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_Ctrl.setFont(font)
        self.CB_Ctrl.setObjectName("CB_Ctrl")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.CB_Ctrl.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_Ctrl)
        self.CB_Interact = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_Interact.setFont(font)
        self.CB_Interact.setObjectName("CB_Interact")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.CB_Interact.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_Interact)
        self.IMG_ActivationBanner_2 = QtWidgets.QLabel(parent=self.tab)
        self.IMG_ActivationBanner_2.setGeometry(QtCore.QRect(10, 280, 421, 41))
        self.IMG_ActivationBanner_2.setText("")
        self.IMG_ActivationBanner_2.setPixmap(QtGui.QPixmap("./res/Icons/ActivationBanner.png"))
        self.IMG_ActivationBanner_2.setScaledContents(True)
        self.IMG_ActivationBanner_2.setObjectName("IMG_ActivationBanner_2")
        self.LBL_ActivationText = QtWidgets.QLabel(parent=self.tab)
        self.LBL_ActivationText.setGeometry(QtCore.QRect(20, 290, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_ActivationText.setFont(font)
        self.LBL_ActivationText.setObjectName("LBL_ActivationText")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 421, 211))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.LBL_MouseMethod = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_MouseMethod.setFont(font)
        self.LBL_MouseMethod.setStyleSheet(
            "QLabel{\\nqlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255))\\n}")
        self.LBL_MouseMethod.setObjectName("LBL_MouseMethod")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_MouseMethod)
        self.CB_MouseMethod = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_MouseMethod.setFont(font)
        self.CB_MouseMethod.setPlaceholderText("")
        self.CB_MouseMethod.setObjectName("CB_MouseMethod")
        self.CB_MouseMethod.addItem("")
        self.CB_MouseMethod.addItem("")
        self.CB_MouseMethod.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_MouseMethod)
        self.LBL_LeftClick = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_LeftClick.setFont(font)
        self.LBL_LeftClick.setObjectName("LBL_LeftClick")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_LeftClick)
        self.CB_LeftClick = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_LeftClick.setFont(font)
        self.CB_LeftClick.setObjectName("CB_LeftClick")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.CB_LeftClick.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_LeftClick)
        self.LBL_RightClick = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_RightClick.setFont(font)
        self.LBL_RightClick.setObjectName("LBL_RightClick")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LBL_RightClick)
        self.CB_RightClick = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_RightClick.setFont(font)
        self.CB_RightClick.setObjectName("CB_RightClick")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.CB_RightClick.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CB_RightClick)
        self.IMG_ActivationBanner = QtWidgets.QLabel(parent=self.tab_2)
        self.IMG_ActivationBanner.setGeometry(QtCore.QRect(10, 280, 421, 41))
        self.IMG_ActivationBanner.setText("")
        self.IMG_ActivationBanner.setPixmap(QtGui.QPixmap("./res/Icons/ActivationBanner.png"))
        self.IMG_ActivationBanner.setScaledContents(True)
        self.IMG_ActivationBanner.setObjectName("IMG_ActivationBanner")
        self.LBL_ActivationText_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.LBL_ActivationText_2.setGeometry(QtCore.QRect(20, 290, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_ActivationText_2.setFont(font)
        self.LBL_ActivationText_2.setObjectName("LBL_ActivationText_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.Tab3 = QtWidgets.QWidget()
        self.Tab3.setObjectName("Tab3")
        self.LBL_SaveSettings = QtWidgets.QLabel(parent=self.Tab3)
        self.LBL_SaveSettings.setGeometry(QtCore.QRect(10, 20, 81, 25))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_SaveSettings.setFont(font)
        self.LBL_SaveSettings.setObjectName("LBL_SaveSettings")
        self.LBL_InputDevice = QtWidgets.QLabel(parent=self.Tab3)
        self.LBL_InputDevice.setGeometry(QtCore.QRect(10, 60, 81, 25))
        self.LBL_CameraOutput = QtWidgets.QLabel(parent=self.Tab3)
        self.LBL_CameraOutput.setGeometry(QtCore.QRect(70, 70, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.LBL_InputDevice.setFont(font)
        self.LBL_InputDevice.setObjectName("LBL_InputDevice")
        self.LBL_CameraOutput.setFont(font)
        self.LBL_CameraOutput.setObjectName("LBL_CameraOutput")
        self.BTN_SaveSettings = QtWidgets.QPushButton(parent=self.Tab3)
        self.BTN_SaveSettings.setGeometry(QtCore.QRect(100, 20, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.BTN_SaveSettings.setFont(font)
        self.BTN_SaveSettings.setObjectName("BTN_SaveSettings")
        self.CB_InputDevice = QtWidgets.QComboBox(parent=self.Tab3)
        self.CB_InputDevice.setGeometry(QtCore.QRect(100, 60, 248, 25))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.CB_InputDevice.setFont(font)
        self.CB_InputDevice.setCurrentText("")
        self.CB_InputDevice.setPlaceholderText("")
        self.CB_InputDevice.setObjectName("CB_InputDevice")
        self.tabWidget.addTab(self.Tab3, "")
        self.LogoPlaceholder = QtWidgets.QLabel(parent=self.centralwidget)
        self.LogoPlaceholder.setGeometry(QtCore.QRect(100, 10, 251, 61))
        self.LogoPlaceholder.setText("")
        self.LogoPlaceholder.setPixmap(QtGui.QPixmap("./res/Icons/FaceGamingDisplayLogo.png"))
        self.LogoPlaceholder.setObjectName("LogoPlaceholder")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def MovementSelect(self):
        if DataManager.KeyMapping[8] > 0 and self.WASD == 0 and self.CB_MovemetMethod.currentIndex() > 0:
            self.CB_MovemetMethod.setCurrentIndex(self.WASD)
            self.MainWindow.show_toast()
        else:
            if self.WASD != 0 and self.CB_MovemetMethod.currentIndex() == 0:
                DataManager.KeyMapping[8] = 0
                self.WASD = 0
            elif DataManager.KeyMapping[8] == 0 or DataManager.KeyMapping[8] == 1 or DataManager.KeyMapping[8] == 2:
                DataManager.KeyMapping[8] = self.CB_MovemetMethod.currentIndex()
                self.WASD = self.CB_MovemetMethod.currentIndex()

    def MouseSelect(self):
        if self.CB_MouseMethod.currentIndex() == 1:
            if DataManager.KeyMapping[8] > 0:
                self.CB_MouseMethod.setCurrentIndex(self.Mouse)
                self.MainWindow.show_toast()
            else:
                DataManager.KeyMapping[8] = 3
                self.Mouse = self.CB_MouseMethod.currentIndex()
        else:
            if self.Mouse == 1:
                DataManager.KeyMapping[8] = 0
            if self.CB_MouseMethod.currentIndex() == 0:
                DataManager.KeyMapping[9] = 0
                DataManager.KeyMapping[8] = 0
            else:
                DataManager.KeyMapping[9] = 1
            self.Mouse = self.CB_MouseMethod.currentIndex()

    def InteractSelect(self):
        if DataManager.KeyMapping[
            self.CB_Interact.currentIndex()] > 0 and self.CB_Interact.currentIndex() != self.Interact and self.CB_Interact.currentIndex() != 0:
            self.CB_Interact.setCurrentIndex(self.Interact)
            self.MainWindow.show_toast()
            return
        if self.CB_Interact.currentIndex() != self.Interact:
            DataManager.KeyMapping[self.Interact] = 0
        DataManager.KeyMapping[self.CB_Interact.currentIndex()] = 5
        self.Interact = self.CB_Interact.currentIndex()

    def CtrlSelect(self):
        if DataManager.KeyMapping[
            self.CB_Ctrl.currentIndex()] > 0 and self.CB_Ctrl.currentIndex() != self.Ctrl and self.CB_Ctrl.currentIndex() != 0:
            self.CB_Ctrl.setCurrentIndex(self.Ctrl)
            self.MainWindow.show_toast()
            return
        if self.CB_Ctrl.currentIndex() != self.Ctrl:
            DataManager.KeyMapping[self.Ctrl] = 0
        DataManager.KeyMapping[self.CB_Ctrl.currentIndex()] = 4
        self.Ctrl = self.CB_Ctrl.currentIndex()

    def SpaceSelect(self):
        if DataManager.KeyMapping[
            self.CB_Spacebar.currentIndex()] > 0 and self.CB_Spacebar.currentIndex() != self.Space and self.CB_Spacebar.currentIndex() != 0:
            self.CB_Spacebar.setCurrentIndex(self.Space)
            self.MainWindow.show_toast()
            return
        if self.CB_Spacebar.currentIndex() != self.Space:
            DataManager.KeyMapping[self.Space] = 0
        DataManager.KeyMapping[self.CB_Spacebar.currentIndex()] = 3
        self.Space = self.CB_Spacebar.currentIndex()

    def LeftClickSelect(self):
        if DataManager.KeyMapping[
            self.CB_LeftClick.currentIndex()] > 0 and self.CB_LeftClick.currentIndex() != self.LeftClick and self.CB_LeftClick.currentIndex() != 0:
            self.CB_LeftClick.setCurrentIndex(self.LeftClick)
            self.MainWindow.show_toast()
            return
        DataManager.KeyMapping[self.CB_LeftClick.currentIndex()] = 1
        if self.CB_LeftClick.currentIndex() != self.LeftClick:
            DataManager.KeyMapping[self.LeftClick] = 0
        self.LeftClick = self.CB_LeftClick.currentIndex()

    def RightClickSelect(self):
        if DataManager.KeyMapping[
            self.CB_RightClick.currentIndex()] > 0 and self.CB_RightClick.currentIndex() != self.RightClick and self.CB_RightClick.currentIndex() != 0:
            self.CB_RightClick.setCurrentIndex(self.RightClick)
            self.MainWindow.show_toast()
            return
        if self.CB_RightClick.currentIndex() != self.RightClick:
            DataManager.KeyMapping[self.RightClick] = 0
        DataManager.KeyMapping[self.CB_RightClick.currentIndex()] = 2
        self.RightClick = self.CB_RightClick.currentIndex()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FaceGaming"))
        self.LBL_MovemetMethod.setText(_translate("MainWindow", "Movement method (WSAD):"))
        self.CB_MovemetMethod.setCurrentText(_translate("MainWindow", "Default"))
        self.CB_MovemetMethod.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_MovemetMethod.setItemText(1, _translate("MainWindow", "Head Tracking (Forward Up)"))
        self.CB_MovemetMethod.setItemText(2, _translate("MainWindow", "Head Tracking (Forward Down)"))
        self.LBL_Spacebar.setText(_translate("MainWindow", "Spacebar Input method:"))
        self.CB_Spacebar.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_Spacebar.setItemText(1, _translate("MainWindow", "Face Left"))
        self.CB_Spacebar.setItemText(2, _translate("MainWindow", "Face Right"))
        self.CB_Spacebar.setItemText(3, _translate("MainWindow", "Mouth Left"))
        self.CB_Spacebar.setItemText(4, _translate("MainWindow", "Mouth Right"))
        self.CB_Spacebar.setItemText(5, _translate("MainWindow", "Mouth Open"))
        self.CB_Spacebar.setItemText(6, _translate("MainWindow", "Eye Wide"))
        self.CB_Spacebar.setItemText(7, _translate("MainWindow", "Brows Up"))
        self.LBL_Control.setText(_translate("MainWindow", "Control (Button) input method:"))
        self.LBL_Interact.setText(_translate("MainWindow", "Interact (Button) input method:"))
        self.CB_Ctrl.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_Ctrl.setItemText(1, _translate("MainWindow", "Face Left"))
        self.CB_Ctrl.setItemText(2, _translate("MainWindow", "Face Right"))
        self.CB_Ctrl.setItemText(3, _translate("MainWindow", "Mouth Left"))
        self.CB_Ctrl.setItemText(4, _translate("MainWindow", "Mouth Right"))
        self.CB_Ctrl.setItemText(5, _translate("MainWindow", "Mouth Open"))
        self.CB_Ctrl.setItemText(6, _translate("MainWindow", "Eye Wide"))
        self.CB_Ctrl.setItemText(7, _translate("MainWindow", "Brows Up"))
        self.CB_Interact.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_Interact.setItemText(1, _translate("MainWindow", "Face Left"))
        self.CB_Interact.setItemText(2, _translate("MainWindow", "Face Right"))
        self.CB_Interact.setItemText(3, _translate("MainWindow", "Mouth Left"))
        self.CB_Interact.setItemText(4, _translate("MainWindow", "Mouth Right"))
        self.CB_Interact.setItemText(5, _translate("MainWindow", "Mouth Open"))
        self.CB_Interact.setItemText(6, _translate("MainWindow", "Eye Wide"))
        self.CB_Interact.setItemText(7, _translate("MainWindow", "Brows Up"))
        self.LBL_ActivationText.setText(_translate("MainWindow", "   To toggle controls : Brows Down + Mouth Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Keyboard Configuration"))
        self.LBL_MouseMethod.setText(_translate("MainWindow", "Mouse Movement method:"))
        self.CB_MouseMethod.setCurrentText(_translate("MainWindow", "Default"))
        self.CB_MouseMethod.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_MouseMethod.setItemText(1, _translate("MainWindow", "Head Tracking"))
        self.CB_MouseMethod.setItemText(2, _translate("MainWindow", "Eye Tracking"))
        self.LBL_LeftClick.setText(_translate("MainWindow", "Left Click:"))
        self.CB_LeftClick.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_LeftClick.setItemText(1, _translate("MainWindow", "Face Left"))
        self.CB_LeftClick.setItemText(2, _translate("MainWindow", "Face Right"))
        self.CB_LeftClick.setItemText(3, _translate("MainWindow", "Mouth Left"))
        self.CB_LeftClick.setItemText(4, _translate("MainWindow", "Mouth Right"))
        self.CB_LeftClick.setItemText(5, _translate("MainWindow", "Mouth Open"))
        self.CB_LeftClick.setItemText(6, _translate("MainWindow", "Eye Wide"))
        self.CB_LeftClick.setItemText(7, _translate("MainWindow", "Brows Up"))
        self.LBL_RightClick.setText(_translate("MainWindow", "Right Click:"))
        self.CB_RightClick.setItemText(0, _translate("MainWindow", "Default"))
        self.CB_RightClick.setItemText(1, _translate("MainWindow", "Face Left"))
        self.CB_RightClick.setItemText(2, _translate("MainWindow", "Face Right"))
        self.CB_RightClick.setItemText(3, _translate("MainWindow", "Mouth Left"))
        self.CB_RightClick.setItemText(4, _translate("MainWindow", "Mouth Right"))
        self.CB_RightClick.setItemText(5, _translate("MainWindow", "Mouth Open"))
        self.CB_RightClick.setItemText(6, _translate("MainWindow", "Eye Wide"))
        self.CB_RightClick.setItemText(7, _translate("MainWindow", "Brows Up"))
        self.LBL_ActivationText_2.setText(_translate("MainWindow", "   To toggle controls : Brows Down + Mouth Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mouse Configuration"))
        self.LBL_SaveSettings.setText(_translate("MainWindow", "Save settings:"))
        self.LBL_InputDevice.setText(_translate("MainWindow", "Input Device:"))
        self.BTN_SaveSettings.setText(_translate("MainWindow", "Save Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab3), _translate("MainWindow", "Options"))
        self.CB_LeftClick.currentIndexChanged.connect(self.LeftClickSelect)
        self.CB_RightClick.currentIndexChanged.connect(self.RightClickSelect)
        self.CB_MouseMethod.currentIndexChanged.connect(self.MouseSelect)
        self.CB_Ctrl.currentIndexChanged.connect(self.CtrlSelect)
        self.CB_Spacebar.currentIndexChanged.connect(self.SpaceSelect)
        self.CB_Interact.currentIndexChanged.connect(self.InteractSelect)
        self.CB_MovemetMethod.currentIndexChanged.connect(self.MovementSelect)
        self.BTN_SaveSettings.clicked.connect(self.SaveSettings)


# Main window class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.UpdateCameraCB)
        self.timer.start()
        self.timer2 = QTimer()
        self.timer2.setInterval(33)
        self.timer2.timeout.connect(self.ShowCameraOutput)
        self.timer2.start()
        self.IsFirstTime = False
        self.Save = []
        self.Db = DbManager.DbManager()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() and Qt.WindowMinimized:
                DataManager.IsMinimized = False
            elif event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
                DataManager.IsMinimized = True

    def closeEvent(self, event):
        DataManager.KeyMapping[10] = 1

    def show_toast(self):
        toast = Toast(self)
        toast.setDuration(5000)  # Hide after 5 seconds
        toast.setTitle('ERROR')
        toast.setText('The selected facial expression is already used')
        toast.applyPreset(ToastPreset.ERROR)  # Apply style preset
        toast.show()

    def ShowCameraOutput(self):
        if len(DataManager.Frame) > 0:
            if not DataManager.IsMinimized:
                Image = cv2.cvtColor(DataManager.Frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                           QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(300, 300, Qt.KeepAspectRatio)
                self.LBL_CameraOutput.setPixmap(QPixmap.fromImage(Pic))

    def ChangeCamInput(self):
        DataManager.KeyMapping[12] = self.CB_InputDevice.currentIndex()

    def UpdateCameraCB(self):
        if DataManager.IsCamReady:
            DataManager.IsCamReady = False
            self.CB_InputDevice.clear()
            iterator = 0
            while iterator < DataManager.KeyMapping[11]:
                self.CB_InputDevice.addItem(f"Camera {iterator}")
                iterator += 1
            self.CB_InputDevice.currentIndexChanged.connect(self.ChangeCamInput)

    def SaveSettings(self):
        DatForDb = [0]
        index = 1
        while index < 14:
            DatForDb.append(DataManager.KeyMapping[index])
            index += 1
        if self.IsFirstTime:
            self.Db.PostToDB({"KeyMapping": DatForDb})
        else:
            self.Db.UpdateDB(user_id, DatForDb)

    def LoadSettings(self):
        results = self.Db.ReadFromDbById(user_id)
        for result in results:
            self.Save = result["KeyMapping"]
        if len(self.Save) > 0:
            self.ComboBoxUpdate()
            index = 0
            while index < 14:
                DataManager.KeyMapping[index] = self.Save[index]
                index += 1
        else:
            self.IsFirstTime = True

    def ComboBoxUpdate(self):
        index = 1
        while index < 8:
            match self.Save[index]:
                case 1:
                    self.CB_LeftClick.setCurrentIndex(index)
                case 2:
                    self.CB_RightClick.setCurrentIndex(index)
                case 3:
                    self.CB_Spacebar.setCurrentIndex(index)
                case 4:
                    self.CB_Ctrl.setCurrentIndex(index)
                case 5:
                    self.CB_Interact.setCurrentIndex(index)
            index += 1
        if self.Save[8] < 3:
            self.CB_MovemetMethod.setCurrentIndex(self.Save[8])
        elif self.Save[8] == 3:
            self.CB_MouseMethod.setCurrentIndex(1)
        if self.Save[9] == 1:
            self.CB_MouseMethod.setCurrentIndex(2)


def GUI_Main():
    global user_id
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    if os.path.isfile("UserId.txt"):
        file = open("UserId.txt", "r")
        user_id = file.readline()
        file.close()
        win.LoadSettings()
    else:
        win.IsFirstTime = True
    win.show()
    sys.exit(app.exec())
