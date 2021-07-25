# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-image: url(:/images/images/images/icon.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 2"
                        "49);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147,"
                        " 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px"
                        " solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid"
                        "; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255"
                        ", 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb("
                        "33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb"
                        "(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScroll"
                        "Bar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontro"
                        "l-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-"
                        "image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-p"
                        "osition: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: "
                        "10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButto"
                        "n {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_statistics = QPushButton(self.topMenu)
        self.btn_statistics.setObjectName(u"btn_statistics")
        sizePolicy.setHeightForWidth(self.btn_statistics.sizePolicy().hasHeightForWidth())
        self.btn_statistics.setSizePolicy(sizePolicy)
        self.btn_statistics.setMinimumSize(QSize(0, 45))
        self.btn_statistics.setFont(font)
        self.btn_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_statistics.setLayoutDirection(Qt.LeftToRight)
        self.btn_statistics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_statistics)

        self.btn_hospital = QPushButton(self.topMenu)
        self.btn_hospital.setObjectName(u"btn_hospital")
        sizePolicy.setHeightForWidth(self.btn_hospital.sizePolicy().hasHeightForWidth())
        self.btn_hospital.setSizePolicy(sizePolicy)
        self.btn_hospital.setMinimumSize(QSize(0, 45))
        self.btn_hospital.setFont(font)
        self.btn_hospital.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hospital.setLayoutDirection(Qt.LeftToRight)
        self.btn_hospital.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-medical-cross.png)")

        self.verticalLayout_8.addWidget(self.btn_hospital)

        self.btn_infographics = QPushButton(self.topMenu)
        self.btn_infographics.setObjectName(u"btn_infographics")
        sizePolicy.setHeightForWidth(self.btn_infographics.sizePolicy().hasHeightForWidth())
        self.btn_infographics.setSizePolicy(sizePolicy)
        self.btn_infographics.setMinimumSize(QSize(0, 45))
        self.btn_infographics.setFont(font)
        self.btn_infographics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_infographics.setLayoutDirection(Qt.LeftToRight)
        self.btn_infographics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_8.addWidget(self.btn_infographics)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.home)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_7 = QFrame(self.home)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"aQFrame{\n"
"background-image: url(:/images/images/images/logo.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame_5)

        self.frame_18 = QFrame(self.frame_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 300))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_12 = QFrame(self.frame_18)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border-radius: 50px;\n"
"background-color: rgb(48, 70, 120);\n"
"font: 20px bold;\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(20, -1, 20, -1)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(120, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(50, 50))
        self.frame_14.setMaximumSize(QSize(50, 50))
        self.frame_14.setStyleSheet(u"border-image: url(:/images/images/images/nepal_flag.png);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_14)

        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 40px bold;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_3)


        self.verticalLayout_24.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_5)

        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_15.addWidget(self.label_8)


        self.verticalLayout_24.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_6)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_16.addWidget(self.label_9)


        self.verticalLayout_24.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, -1, 20, -1)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_17.addWidget(self.label_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_24.addWidget(self.frame_12)

        self.frame_15 = QFrame(self.frame_18)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border-radius: 50px;\n"
"background-color: rgb(48, 70, 120);\n"
"font: 20px bold;\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, -1, 20, -1)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(120, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(50, 50))
        self.frame_17.setMaximumSize(QSize(60, 60))
        self.frame_17.setStyleSheet(u"border-image: url(:/images/images/images/world.png);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_17)

        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 40px bold;")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_11)


        self.verticalLayout_25.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_21.addWidget(self.label_13)


        self.verticalLayout_25.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_22.addWidget(self.label_15)


        self.verticalLayout_25.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(20, -1, 20, -1)
        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_23.addWidget(self.label_17)


        self.verticalLayout_25.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_24.addWidget(self.frame_15)


        self.verticalLayout_26.addWidget(self.frame_18)


        self.horizontalLayout_14.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.home)
        self.statistics = QWidget()
        self.statistics.setObjectName(u"statistics")
        self.statistics.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.statistics)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_19 = QFrame(self.statistics)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_25 = QFrame(self.frame_19)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 15, 0)
        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_28)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 35))
        self.label_28.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_28)

        self.comboBox_dateStart = QComboBox(self.frame_26)
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.setObjectName(u"comboBox_dateStart")
        self.comboBox_dateStart.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_12.addWidget(self.comboBox_dateStart)

        self.comboBox_monthStart = QComboBox(self.frame_26)
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.setObjectName(u"comboBox_monthStart")
        self.comboBox_monthStart.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_12.addWidget(self.comboBox_monthStart)

        self.comboBox_yearStart = QComboBox(self.frame_26)
        self.comboBox_yearStart.addItem("")
        self.comboBox_yearStart.addItem("")
        self.comboBox_yearStart.addItem("")
        self.comboBox_yearStart.setObjectName(u"comboBox_yearStart")
        self.comboBox_yearStart.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_12.addWidget(self.comboBox_yearStart)


        self.horizontalLayout_11.addWidget(self.frame_26)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(20, 0))
        self.frame_30.setMaximumSize(QSize(30, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_30)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_27)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 35))
        self.label_30.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.comboBox_dateEnd = QComboBox(self.frame_27)
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.setObjectName(u"comboBox_dateEnd")
        self.comboBox_dateEnd.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.comboBox_dateEnd)

        self.comboBox_monthEnd = QComboBox(self.frame_27)
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.setObjectName(u"comboBox_monthEnd")
        self.comboBox_monthEnd.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.comboBox_monthEnd)

        self.comboBox_yearEnd = QComboBox(self.frame_27)
        self.comboBox_yearEnd.addItem("")
        self.comboBox_yearEnd.addItem("")
        self.comboBox_yearEnd.addItem("")
        self.comboBox_yearEnd.setObjectName(u"comboBox_yearEnd")
        self.comboBox_yearEnd.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.comboBox_yearEnd)


        self.horizontalLayout_11.addWidget(self.frame_27)

        self.btn_select = QPushButton(self.frame_25)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setMinimumSize(QSize(140, 40))
        self.btn_select.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_11.addWidget(self.btn_select)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_29)


        self.verticalLayout_19.addWidget(self.frame_25)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.graph1 = QVBoxLayout()
        self.graph1.setObjectName(u"graph1")

        self.verticalLayout_17.addLayout(self.graph1)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_23)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.graph4 = QVBoxLayout()
        self.graph4.setObjectName(u"graph4")

        self.verticalLayout_18.addLayout(self.graph4)


        self.gridLayout.addWidget(self.frame_23, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_22)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.graph2 = QVBoxLayout()
        self.graph2.setObjectName(u"graph2")

        self.verticalLayout_16.addLayout(self.graph2)


        self.gridLayout.addWidget(self.frame_22, 0, 1, 1, 1)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.graph3 = QVBoxLayout()
        self.graph3.setObjectName(u"graph3")

        self.horizontalLayout_9.addLayout(self.graph3)


        self.gridLayout.addWidget(self.frame_24, 1, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_20)


        self.verticalLayout.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.statistics)
        self.hospitals = QWidget()
        self.hospitals.setObjectName(u"hospitals")
        self.horizontalLayout_18 = QHBoxLayout(self.hospitals)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_11 = QFrame(self.hospitals)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 10, 271, 61))
        self.label_4.setFont(font)

        self.horizontalLayout_18.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.hospitals)
        self.infographics = QWidget()
        self.infographics.setObjectName(u"infographics")
        self.verticalLayout_20 = QVBoxLayout(self.infographics)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tabWidget = QTabWidget(self.infographics)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"    border: 1px solid gray;\n"
"    color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"    color: rgb(191, 191, 191);\n"
"	font-size: 18px;\n"
"	width: 100px;\n"
"	height: 40px;\n"
"	border: 2px solid gray;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: -9px;\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"	background-color: rgb(41, 44, 94);\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(13, 34, 42);\n"
"}\n"
"QTableWidget\n"
"{\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(13, 34, 42);;\n"
"	alternate-background-color: rgb(88, 88, 88);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 17px;\n"
"	gridline-color: gray;\n"
"}\n"
"QHeaderView\n"
"{\n"
"	background-color: rgb(13, 34, 42);\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"	color: rgb(255, 255, 255);\n"
"	f"
                        "ont: bold;\n"
"}\n"
"QTableWidget QTableCornerButton::section \n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"}")
        self.tab_Symptoms = QWidget()
        self.tab_Symptoms.setObjectName(u"tab_Symptoms")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_Symptoms)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea_2 = QScrollArea(self.tab_Symptoms)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 777, 953))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(27, -1, -1, -1)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 400))
        self.frame_6.setMaximumSize(QSize(100000, 100000))
        self.frame_6.setStyleSheet(u"image: url(:/images/images/images/symptoms.png);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tableWidget_symptoms = QTableWidget(self.frame_8)
        if (self.tableWidget_symptoms.columnCount() < 5):
            self.tableWidget_symptoms.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_symptoms.setObjectName(u"tableWidget_symptoms")
        self.tableWidget_symptoms.setMinimumSize(QSize(715, 500))
        self.tableWidget_symptoms.setMaximumSize(QSize(700, 16777215))
        self.tableWidget_symptoms.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.tableWidget_symptoms)


        self.verticalLayout_22.addWidget(self.frame_8)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_7.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_Symptoms, "")
        self.tab_prevention = QWidget()
        self.tab_prevention.setObjectName(u"tab_prevention")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_prevention)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_3 = QScrollArea(self.tab_prevention)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 731, 1002))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"font-size: 30px;\n"
"font: bold;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_21.addWidget(self.label)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 450))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 300))
        self.frame_3.setMaximumSize(QSize(400, 600))
        self.frame_3.setStyleSheet(u"border-image: url(:/images/images/images/things_you_should_do.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(650, 16777215))
        self.frame.setStyleSheet(u"font: 75 18pt \"Lato\";\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_23.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_23.addWidget(self.label_19)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_23.addWidget(self.label_25)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_23.addWidget(self.label_21)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_23.addWidget(self.label_24)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_23.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_23.addWidget(self.label_23)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_23.addWidget(self.label_20)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_23.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_23.addWidget(self.label_27)


        self.horizontalLayout_6.addWidget(self.frame)


        self.verticalLayout_21.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 450))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(400, 600))
        self.frame_10.setStyleSheet(u"border-image: url(:/images/images/images/get_vaccinated.png);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_10)


        self.verticalLayout_21.addWidget(self.frame_2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"font: 25px;\n"
"text: bold;")

        self.verticalLayout_21.addWidget(self.label_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_8.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.tab_prevention, "")

        self.verticalLayout_20.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.infographics)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"COVINFO", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Stay Safe", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.btn_hospital.setText(QCoreApplication.translate("MainWindow", u"Hospitals", None))
        self.btn_infographics.setText(QCoreApplication.translate("MainWindow", u"Infographics", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">COVINFO</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; ma"
                        "rgin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"COVID-19 Situation Analysis Application", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nepal", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Active Cases:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Recovered:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Active Cases:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Recovered:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Start Date: ", None))
        self.comboBox_dateStart.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_dateStart.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_dateStart.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_dateStart.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_dateStart.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_dateStart.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_dateStart.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_dateStart.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_dateStart.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_dateStart.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_dateStart.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_dateStart.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_dateStart.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_dateStart.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_dateStart.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_dateStart.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_dateStart.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_dateStart.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_dateStart.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_dateStart.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_dateStart.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_dateStart.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_dateStart.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_dateStart.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_dateStart.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_dateStart.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox_dateStart.setItemText(26, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_dateStart.setItemText(27, QCoreApplication.translate("MainWindow", u"29", None))
        self.comboBox_dateStart.setItemText(28, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_dateStart.setItemText(29, QCoreApplication.translate("MainWindow", u"31", None))

        self.comboBox_monthStart.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.comboBox_monthStart.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.comboBox_monthStart.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.comboBox_monthStart.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.comboBox_monthStart.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.comboBox_monthStart.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.comboBox_monthStart.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.comboBox_monthStart.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.comboBox_monthStart.setItemText(8, QCoreApplication.translate("MainWindow", u"September", None))
        self.comboBox_monthStart.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.comboBox_monthStart.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.comboBox_monthStart.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.comboBox_yearStart.setItemText(0, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_yearStart.setItemText(1, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_yearStart.setItemText(2, QCoreApplication.translate("MainWindow", u"2021", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"End Date: ", None))
        self.comboBox_dateEnd.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_dateEnd.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_dateEnd.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_dateEnd.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_dateEnd.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_dateEnd.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_dateEnd.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_dateEnd.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_dateEnd.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_dateEnd.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_dateEnd.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_dateEnd.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_dateEnd.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_dateEnd.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_dateEnd.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_dateEnd.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_dateEnd.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_dateEnd.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_dateEnd.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_dateEnd.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_dateEnd.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_dateEnd.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_dateEnd.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_dateEnd.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_dateEnd.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_dateEnd.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox_dateEnd.setItemText(26, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_dateEnd.setItemText(27, QCoreApplication.translate("MainWindow", u"29", None))
        self.comboBox_dateEnd.setItemText(28, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_dateEnd.setItemText(29, QCoreApplication.translate("MainWindow", u"31", None))

        self.comboBox_monthEnd.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.comboBox_monthEnd.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.comboBox_monthEnd.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.comboBox_monthEnd.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.comboBox_monthEnd.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.comboBox_monthEnd.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.comboBox_monthEnd.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.comboBox_monthEnd.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.comboBox_monthEnd.setItemText(8, QCoreApplication.translate("MainWindow", u"September", None))
        self.comboBox_monthEnd.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.comboBox_monthEnd.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.comboBox_monthEnd.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.comboBox_yearEnd.setItemText(0, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_yearEnd.setItemText(1, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_yearEnd.setItemText(2, QCoreApplication.translate("MainWindow", u"2021", None))

        self.btn_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hospitals", None))
        ___qtablewidgetitem = self.tableWidget_symptoms.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None));
        ___qtablewidgetitem1 = self.tableWidget_symptoms.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"COVID-19", None));
        ___qtablewidgetitem2 = self.tableWidget_symptoms.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Common Cold", None));
        ___qtablewidgetitem3 = self.tableWidget_symptoms.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Flu", None));
        ___qtablewidgetitem4 = self.tableWidget_symptoms.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Allergies", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Symptoms), QCoreApplication.translate("MainWindow", u"Symptoms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Preventions:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u2022 Wear your mask", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u2022 Stay socially distant", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u2022 Keep washing your hands", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u2022 Keep holiday gatherings small", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u2022 Dine out carefully", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u2022 Get your flu shot", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u2022 Seek routine medical care", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u2022 Be mindful of your mental health", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u2022 Watch your weight", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u2022 Keep up the good (safety) work", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Prevention is Better than Cure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prevention), QCoreApplication.translate("MainWindow", u"Prevention", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: DASS", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

