import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import csv
import pandas as pd

import KaggleData



# from splashScreen import SplashScreen
from statistics import *
from ui_functions import *
from infographics import Seriousness_of_Symptoms, Agewise_Risk_Analysis, Best_Household_Materials_For_a_Mask

# # SET AS GLOBAL WIDGETS
# # ///////////////////////////////////////////////////////////////
# widgets = None

## ==> SPLASH SCREEN
from ui_SplashScreen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

from qt_material import *

## ==> GLOBALS
counter = 0

############################ CSV #######################################

######### 24hr Nepal ###################################################
with open(os.path.join("Resources","NepalDailyData.csv"), "r") as f:
    for row in csv.reader(f, delimiter=','):
        if row[0] == "New Cases":
            NewCases_N_24 = row[1]
        if row[0] == "Recovered":
           Recovered_N_24 = row[1]
        if row[0] == "Deaths":
            Deaths_N_24 = row[1]

######### Overall Nepal ################################################
with open(os.path.join("Resources","NepalOverallData.csv"), "r") as f:
    for row in csv.reader(f, delimiter=','):
        if row[0] == "Total Infected":
            NewCases_N_ov = row[1]
        if row[0] == "Recovered":
           Recovered_N_ov = row[1]
        if row[0] == "Deaths":
            Deaths_N_ov = row[1]

######## World ##########################################################
with open(os.path.join("Resources","WorldDailyData.csv"), "r") as f:
    WorldData = list(csv.reader(f, delimiter=','))
    NewCases_W_24 = WorldData[1][1]
    Recovered_W_24 = WorldData[1][3]
    Deaths_W_24 = WorldData[1][2]

    NewCases_W_ov = WorldData[1][0]
    Recovered_W_ov = WorldData[1][5]
    Deaths_W_ov = WorldData[1][4]
##########################################################################

# MAIN APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        ## SET MAIN BACKGROUND TO TRANSPARENT
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)


        ## STACKED PAGES NAVIGATION

        ## DEFAULT PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))


        ## LEFT MENU BUTTON CLICKED
        self.ui.btn_home.clicked.connect(self.buttonClick)
        self.ui.btn_nationalStatistics.clicked.connect(self.buttonClick)
        self.ui.btn_worldStatistics.clicked.connect(self.buttonClick)
        self.ui.btn_hospitals.clicked.connect(self.buttonClick)
        self.ui.btn_infographics.clicked.connect(self.buttonClick)
        ## EXIT WINDOW CLICKED
        self.ui.btn_exit.clicked.connect(lambda: UIFunctions.warningMessage(self))

        
        ## SET DEFAULT TAB
        self.ui.tabWidget_nationalStatistics.setCurrentIndex(0)
        self.ui.tabWidget_worldStatistics.setCurrentIndex(0)
        self.ui.tabWidget_infographics.setCurrentIndex(0)


        #TABLEWIGET WIDGET SHOW
        self.ui.tableWidget_hospitals.horizontalHeader().setVisible(True)
        self.ui.tableWidget_symptoms.horizontalHeader().setVisible(True)


        ## ADD CLICK EVENT/MOUSE MOVE EVENT/DRAG EVENT TO THE TOP HEADER TO MOVE THE WINDOW
        # self.ui.leftBox.mouseMoveEvent = UIFunctions.moveWindow(self)


        ## LEFT MENU TOGGLE BUTTON
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.slideLeftMenu(self))

        ## SETTINGS BUTTON CLICKED
        self.ui.btn_Settings.clicked.connect(lambda: UIFunctions.slideExtraLeftBox(self))
        self.ui.extraCloseColumnBtn.clicked.connect(lambda: UIFunctions.slideExtraLeftBox(self))


        


        ##TABLE WIDGET CUSTOM SETTINGS
        # self.ui.tableWidget_symptoms.setColumnWidth(0, 175)
        # self.ui.tableWidget_symptoms.setColumnWidth(1, 120)
        # self.ui.tableWidget_symptoms.setColumnWidth(2, 120)
        # self.ui.tableWidget_symptoms.setColumnWidth(3, 120)
        # self.ui.tableWidget_symptoms.setColumnWidth(4, 120)
        UIFunctions.loadSymptoms(self)
        UIFunctions.loadHospitals(self)


        ######################################
        ############### GRAPH  ###############
        ##### IMPORTED FROM statistics.py ####
        ######################################

        ## NEPAL CASES
        self.N_Cases_mnth = Canvas_N_Cases_mnth(self)
        self.N_Cases_week = Canvas_N_Cases_week(self)
        self.N_Cases_overall = Canvas_N_Cases_overall(self)
        #self.N_Cases_custom = Canvas_N_Cases_custom(self)
        self.N_Cases_custom = Canvas_N_Cases_mnth(self)


        self.ui.graph_Cases_LatestMonth.addWidget(self.N_Cases_mnth)
        self.ui.graph_Cases_LatestWeek.addWidget(self.N_Cases_week)
        self.ui.graph_Cases_Overall.addWidget(self.N_Cases_overall)
        self.ui.graph_Cases_CustomTimeFrame.addWidget(self.N_Cases_custom)

        #NEPAL DEATHS
        self.N_Deaths_mnth = Canvas_N_Deaths_mnth(self)
        self.N_Deaths_week = Canvas_N_Deaths_week(self)
        self.N_Deaths_overall = Canvas_N_Deaths_overall(self)
        #self.N_Deaths_custom = Canvas_N_Deaths_custom(self)
        self.N_Deaths_custom = Canvas_N_Deaths_mnth(self)

        self.ui.graph_Deaths_LatestMonth.addWidget(self.N_Deaths_mnth)
        self.ui.graph_Deaths_LatestWeek.addWidget(self.N_Deaths_week)
        self.ui.graph_Deaths_Overall.addWidget(self.N_Deaths_overall)
        self.ui.graph_Deaths_CustomTimeFrame.addWidget(self.N_Deaths_custom)

        
        #NEPAL VACCINE
        self.N_TotalVaccination = Canvas_N_TotalVaccination(self)
        self.N_PeopleVaccinated = Canvas_N_PeopleVaccinated(self)

        self.ui.graph1_10.addWidget(self.N_TotalVaccination)
        self.ui.graph2_10.addWidget(self.N_PeopleVaccinated)



        ######################################
        ############### GRAPH  ###############
        ##### IMPORTED FROM infographics.py ####
        ######################################
        self.graph5 = Seriousness_of_Symptoms(self)
        self.ui.graph5.addWidget(self.graph5)


        self.graph6 = Agewise_Risk_Analysis(self)
        self.ui.graph6.addWidget(self.graph6)


        self.graph7 = Best_Household_Materials_For_a_Mask(self)
        self.ui.graph7.addWidget(self.graph7)



        ##DATE SELECTED FOR CUSTOM TIME FRAME
        self.ui.btn_select.clicked.connect(lambda: UIFunctions.getDate_NationalStatistics_Cases(self))
        self.ui.btn_select_2.clicked.connect(lambda: UIFunctions.getDate_NationalStatistics_Deaths(self))
        self.ui.btn_select_3.clicked.connect(lambda: UIFunctions.getDate_NationalStatistics_Recovered(self))
        self.ui.btn_select_4.clicked.connect(lambda: UIFunctions.getDate_WorldStatistics_Cases(self))
        self.ui.btn_select_5.clicked.connect(lambda: UIFunctions.getDate_WorldStatistics_Deaths(self))
        self.ui.btn_select_6.clicked.connect(lambda: UIFunctions.getDate_WorldStatistics_Recovered(self))

        ################################### UPDATING DASHBOARD #######################
        self.ui.label_44.setText(str(NewCases_N_24))
        self.ui.label_46.setText(str(Recovered_N_24))
        self.ui.label_48.setText(str(Deaths_N_24))

        self.ui.label_51.setText(str(NewCases_N_ov))
        self.ui.label_53.setText(str(Recovered_N_ov))
        self.ui.label_55.setText(str(Deaths_N_ov))


        self.ui.label_12.setText(str(NewCases_W_24))
        self.ui.label_15.setText(str(Recovered_W_24))
        self.ui.label_17.setText(str(Deaths_W_24))

        self.ui.label_36.setText(str(NewCases_W_ov))
        self.ui.label_38.setText(str(Recovered_W_ov))
        self.ui.label_40.setText(str(Deaths_W_ov))
        #############################################################

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()


        # MAIN WINDOW LABEL
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        # QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        ## NAVIGATE TO HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        ## NAVIGATE TO NATIONAL STATISTICS PAGE
        if btnName == "btn_nationalStatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.national_Statistics)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

         ## NAVIGATE TO WORLD STATISTICS PAGE
        if btnName == "btn_worldStatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.world_statistics)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        ## NAVIGATE TO HOSPITALS PAGE
        if btnName == "btn_hospitals":
            self.ui.stackedWidget.setCurrentWidget(self.ui.hospitals)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        ## NAVIGATE TO INFOGRAPHICS PAGE
        if btnName == "btn_infographics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.infographics)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



    ## ADD MOUSE EVENTS TO THE WINDOW
    def mousePressEvent(self, event):
        ## GET THE CURRENT POSTITION OF THE MOUSE
        self.clickPosition = event.globalPos() 
        ## WE USE THIS VALUT TO MOVE THE WINDOW   







# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        # global widgets
        # widgets = self.ui
        

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
        self.timer.start(20)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>COVID-19</strong> Situation Analysis Application")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATA"))
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
    #KaggleData.ScrapeKaggleData()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()
    sys.exit(app.exec_())