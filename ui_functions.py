from main import *
import pandas as pd

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


    ## SHOW WARNING MESSAGE BEFORE EXITING
    def warningMessage(self):
        msg = QMessageBox.warning(self, "Warning!!!", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            self.close()


    ##  LOAD SYMPTOMS FROM CSV TO THE TABLE IN INFROGRAPHICS
    def loadSymptoms(self):
        data = pd.read_csv('Symptoms.csv')

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

    ## GET START AND END DATE FROM THE USER
    def getDate(self):
        date_start = self.ui.comboBox_dateStart.currentText()
        month_start = self.ui.comboBox_monthStart.currentText()
        year_start =  self.ui.comboBox_yearStart.currentText()

        date_end = self.ui.comboBox_dateEnd.currentText()
        month_end = self.ui.comboBox_monthEnd.currentText()
        year_end =  self.ui.comboBox_yearEnd.currentText()
        
        print(date_start, month_start, year_start)
        print(date_end, month_end, year_end)
