from main import *
import pandas as pd


symptoms = []
covid_19 = []
common_cold = []
flu = []
allergies = []


class UIFunctions(MainWindow):
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


    ## EXPAND AND RESTORE LEFT MENU
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


    ## EXPAND AND RESTORE EXTRA LEFT BOX
    def slideExtraLeftBox(self):
        ## GET CURRENT LEFT MENU WIDTH
        width = self.ui.extraLeftBox.width()

        ## IF MINIMIZED
        if width == 0:
            newWidth = 240  ## EXPAND MENU      
        else: ## IF MAXIMIZED
            newWidth = 0  ## RESTORE MENU

        ## ANIMATE THE TRANSITION
        self.animation = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth") ## ANIMATE MINIMUM WIDTH
        self.animation.setDuration(500)
        self.animation.setStartValue(width) ## START VALUE IS THE CURRENT MENU WIDTH
        self.animation.setEndValue(newWidth) ## END VALUE IS THE NEW MENU WIDTH
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()



    ##SELECT/ DESELECT
    def selectMenu(getStyle):
        select = getStyle + """border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0)); background-color: rgb(40, 44, 52);"""
        return select

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("""border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0)); background-color: rgb(40, 44, 52);""", "")
        return deselect



    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
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
        self.ui.leftBox.mouseMoveEvent = moveWindow


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(100)
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
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.restore_or_maximize_window(self))


    ## SHOW WARNING MESSAGE BEFORE EXITING
    def warningMessage(self):
        msg = QMessageBox.warning(self, "Warning!!!", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            self.close()


    ##  LOAD SYMPTOMS FROM CSV TO THE TABLE IN INFROGRAPHICS PAGE
    def loadSymptoms(self):
        data = pd.read_csv('Resources/Symptoms.csv')

        symptoms = data['Symptoms'].tolist()
        covid_19 = data['COVID-19'].tolist()
        common_cold = data['Common Cold'].tolist()
        flu = data['Flu'].tolist()
        allergies = data['Allergies'].tolist()

        row = 0
        self.ui.tableWidget_symptoms.setRowCount(len(symptoms))
        for item in symptoms:    
            self.ui.tableWidget_symptoms.setItem(row, 0, QtWidgets.QTableWidgetItem(symptoms[row]))
            self.ui.tableWidget_symptoms.setItem(row, 1, QtWidgets.QTableWidgetItem(covid_19[row]))
            self.ui.tableWidget_symptoms.setItem(row, 2, QtWidgets.QTableWidgetItem(common_cold[row]))
            self.ui.tableWidget_symptoms.setItem(row, 3, QtWidgets.QTableWidgetItem(flu[row]))
            self.ui.tableWidget_symptoms.setItem(row, 4, QtWidgets.QTableWidgetItem(allergies[row]))
            row = row + 1


    ## LOAD HOSPITALS FROM CSV TO THE TABLE IN HOSPITAL PAGE
    def loadHospitals(self):
        data = pd.read_csv('Resources/Hospitals.csv')

        hospital_name = data['Hospital Name'].tolist()
        contact = data['Contact'].tolist()
        total_beds = data['Total Beds'].tolist()
        icu_beds = data['ICU Beds'].tolist()
        ventilators = data['Ventilators'].tolist()
        isolation_beds = data['Isolation Beds'].tolist()

        row = 0
        self.ui.tableWidget_hospitals.setRowCount(len(hospital_name))
        for item in hospital_name:    
            self.ui.tableWidget_hospitals.setItem(row, 0, QtWidgets.QTableWidgetItem(hospital_name[row]))
            # self.ui.tableWidget_hospitals.setItem(row, 1, QtWidgets.QTableWidgetItem(contact[row]))
            self.ui.tableWidget_hospitals.setItem(row, 2, QtWidgets.QTableWidgetItem(total_beds[row]))
            self.ui.tableWidget_hospitals.setItem(row, 3, QtWidgets.QTableWidgetItem(icu_beds[row]))
            self.ui.tableWidget_hospitals.setItem(row, 4, QtWidgets.QTableWidgetItem(ventilators[row]))
            # self.ui.tableWidget_hospitals.setItem(row, 5, QtWidgets.QTableWidgetItem(isolation_beds[row]))
            row = row + 1


    ## GET START AND END DATE FROM THE USER
    def getDate_NationalStatistics_Cases(self):
        date_start_ns_cases = self.ui.comboBox_dateStart.currentText()
        month_start_ns_cases = self.ui.comboBox_monthStart.currentText()
        year_start_ns_cases =  self.ui.comboBox_yearStart.currentText()

        date_end_ns_cases = self.ui.comboBox_dateEnd.currentText()
        month_end_ns_cases = self.ui.comboBox_monthEnd.currentText()
        year_end_ns_cases =  self.ui.comboBox_yearEnd.currentText()
        
        print(date_start_ns_cases, month_start_ns_cases, year_start_ns_cases)
        print(date_end_ns_cases, month_end_ns_cases, year_end_ns_cases)

    def getDate_NationalStatistics_Deaths(self):
        date_start_ns_deaths = self.ui.comboBox_dateStart_2.currentText()
        month_start_ns_deaths = self.ui.comboBox_monthStart_2.currentText()
        year_start_ns_deaths =  self.ui.comboBox_yearStart_2.currentText()

        date_end_ns_deaths = self.ui.comboBox_dateEnd_2.currentText()
        month_end_ns_deaths = self.ui.comboBox_monthEnd_2.currentText()
        year_end_ns_deaths =  self.ui.comboBox_yearEnd_2.currentText()
        
        print(date_start_ns_deaths, month_start_ns_deaths, year_start_ns_deaths)
        print(date_end_ns_deaths, month_end_ns_deaths, year_end_ns_deaths)

    def getDate_NationalStatistics_Recovered(self):
        date_start_ns_recovered = self.ui.comboBox_dateStart_3.currentText()
        month_start_ns_recovered = self.ui.comboBox_monthStart_3.currentText()
        year_start_ns_recovered =  self.ui.comboBox_yearStart_3.currentText()

        date_end_ns_recovered = self.ui.comboBox_dateEnd_3.currentText()
        month_end_ns_recovered = self.ui.comboBox_monthEnd_3.currentText()
        year_end_ns_recovered =  self.ui.comboBox_yearEnd_3.currentText()
        
        print(date_start_ns_recovered, month_start_ns_recovered, year_start_ns_recovered)
        print(date_end_ns_recovered, month_end_ns_recovered, year_end_ns_recovered)

    def getDate_WorldStatistics_Cases(self):
        date_start_ws_cases = self.ui.comboBox_dateStart_4.currentText()
        month_start_ws_cases = self.ui.comboBox_monthStart_4.currentText()
        year_start_ws_cases =  self.ui.comboBox_yearStart_4.currentText()

        date_end_ws_cases = self.ui.comboBox_dateEnd_4.currentText()
        month_end_ws_cases = self.ui.comboBox_monthEnd_4.currentText()
        year_end_ws_cases =  self.ui.comboBox_yearEnd_4.currentText()
        
        print(date_start_ws_cases, month_start_ws_cases, year_start_ws_cases)
        print(date_end_ws_cases, month_end_ws_cases, year_end_ws_cases)

    def getDate_WorldStatistics_Deaths(self):
        date_start_ws_deaths = self.ui.comboBox_dateStart_5.currentText()
        month_start_ws_deaths = self.ui.comboBox_monthStart_5.currentText()
        year_start_ws_deaths =  self.ui.comboBox_yearStart_5.currentText()

        date_end_ws_deaths = self.ui.comboBox_dateEnd_5.currentText()
        month_end_ws_deaths = self.ui.comboBox_monthEnd_5.currentText()
        year_end_ws_deaths =  self.ui.comboBox_yearEnd_5.currentText()
        
        print(date_start_ws_deaths, month_start_ws_deaths, year_start_ws_deaths)
        print(date_end_ws_deaths, month_end_ws_deaths, year_end_ws_deaths)

    def getDate_WorldStatistics_Recovered(self):
        date_start_ws_recovered = self.ui.comboBox_dateStart_6.currentText()
        month_start_ws_recovered = self.ui.comboBox_monthStart_6.currentText()
        year_start_ws_recovered =  self.ui.comboBox_yearStart_6.currentText()

        date_end_ws_recovered = self.ui.comboBox_dateEnd_6.currentText()
        month_end_ws_recovered = self.ui.comboBox_monthEnd_6.currentText()
        year_end_ws_recovered =  self.ui.comboBox_yearEnd_6.currentText()
        
        print(date_start_ws_recovered, month_start_ws_recovered, year_start_ws_recovered)
        print(date_end_ws_recovered, month_end_ws_recovered, year_end_ws_recovered)

