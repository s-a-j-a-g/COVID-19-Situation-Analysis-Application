import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

# from modules import *

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

## ==> SPLASH SCREEN
from ui_SplashScreen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

from qt_material import *

## ==> GLOBALS
counter = 0

# MAIN APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # apply_stylesheet(app, theme = 'dark_cyan.xml')

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        ## SET MAIN BACKGROUND TO TRANSPARENT
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.bgApp.setGraphicsEffect(self.shadow)


        ## WINDOW SIZE GRIP TO RESIZE WINDOW
        QSizeGrip(self.ui.frame_size_grip)

        ## MINIMIZE WINDOW
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        ## CLOSE WINDOW
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

        ## MAXIMIZE/RESTORE WINDOW
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.restore_or_maximize_window())


        ## STACKED PAGES NAVIGATION

        ## DEFAULT PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        ## NAVIGATE TO HOME PAGE
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))

        ## NAVIGATE TO GRAPH PAGE
        self.ui.btn_graph.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.graph))

        ## NAVIGATE TO INFOGRAPHICS PAGE
        self.ui.btn_infographics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.infographics))


        ## EXIT WINDOW PRESSED
        self.ui.btn_exit.clicked.connect(lambda: self.warningMessage())


        ## DRAG HANDLER - FUNCTION TO MOVE WINDOW ON MOUSE DRAG EVENT ON THE TITLE BAR
        def moveWindow(event):
            # DETECT IF THE WINDOW IS NORMAL SIZE 
            if self.isMaximized() == False: # (NOT MAXIMIZED - NORMAL SIZE) /// MOVE WINDOW ONLY WHEN WINDOW IS NORMAL SIZE
                ## ONLY ACCEPT LEFT MOUSE BUTTON CLICKS
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
                    # if self.isMaximized() == True:
                    #     self.showNormal()


        ## ADD CLICK EVENT/MOUSE MOVE EVENT/DRAG EVENT TO THE TOP HEADER TO MOVE THE WINDOW
        self.ui.leftBox.mouseMoveEvent = moveWindow


        ## LEFT MENU TOGGLE BUTTON
        self.ui.toggleButton.clicked.connect(lambda: self.slideLeftMenu())


        # # BUTTONS CLICK
        # # ///////////////////////////////////////////////////////////////

        # # LEFT MENUS
        # widgets.btn_home.clicked.connect(self.buttonClick)
        # widgets.btn_widgets.clicked.connect(self.buttonClick)
        # widgets.btn_new.clicked.connect(self.buttonClick)
        # widgets.btn_save.clicked.connect(self.buttonClick)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()


        # MAIN WINDOW LABEL
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        # QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))


    ## UPDATE RESTORE BUTTON ICON ON MAXIMIZINGOR MINIMIZING WINDOW
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            ## CHANGE ICON
            self.ui.maximizeRestoreAppBtn.setIcon(QtGui.QIcon(u":/icons/images/icons/icon_maximize.png"))
        else:
            self.showMaximized()
            ## CHANGE ICON
            self.ui.maximizeRestoreAppBtn.setIcon(QtGui.QIcon(u":/icons/images/icons/icon_restore.png"))


    ## ADD MOUSE EVENTS TO THE WINDOW
    def mousePressEvent(self, event):
        ## GET THE CURRENT POSTITION OF THE MOUSE
        self.clickPosition = event.globalPos() 
        ## WE USE THIS VALUT TO MOVE THE WINDOW   


    def slideLeftMenu(self):
        ## GET CURRENT LEFT MENU WIDTH
        width = self.ui.leftMenuBg.width()

        ## IF MINIMIZED
        if width == 60:
            newWidth = 240  ## EXPAND MENU      
        else: ## IF MAXIMIZED
            newWidth = 60  ## RESTORE MENU

        ## ANIMATE THE TRANSITION
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth") ## ANIMATE MINIMUM WIDTH
        self.animation.setDuration(500)
        self.animation.setStartValue(width) ## START VALUE IS THE CURRENT MENU WIDTH
        self.animation.setEndValue(newWidth) ## END VALUE IS THE NEW MENU WIDTH
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    def warningMessage(self):
        # msg = QMessageBox()
        # msg.setIcon(QMes/sageBox.Warning)
        # msg.setText("Are you sure you want to exit?")
        # msg.setWindowTitle("Warning!!!")
        msg = QMessageBox.warning(self, "Warning!!!", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            self.close()




# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>COVID-19</strong> Situation Analysis Application")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()
    sys.exit(app.exec())