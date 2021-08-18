
import sys
from matplotlib.backends.backend_qt5 import FigureCanvasQT
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
from PySide2.QtWidgets import QApplication, QWidget
import csv
import pandas as pd
from datetime import datetime
from CustomTime import *
from dateutil.relativedelta import relativedelta
from sklearn.linear_model import LinearRegression

import statsmodels.formula.api as smf



##########################################################################################################
##########################################################################################################
################################################# NEPAL ##################################################
##########################################################################################################
##########################################################################################################




##########################################################################################################
        # Nepal Cases Month
##########################################################################################################

class Canvas_N_Cases_mnth(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','new_cases'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 
        

        #Getting Last month
        lastMnth = datetime.now()+relativedelta(months=-1)

        #Structuring start and end Date
        start_date = datetime.strftime(lastMnth,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        LatestMonthData_s = data.loc[mask]
        
        #making an array of dates
        LatestMonthData['date'] = pd.to_numeric(pd.to_datetime(LatestMonthData['date']) )
        list_Date = LatestMonthData['date'].tolist()
        Data = np.array(list_Date).reshape((-1,1))

        #Making a second array of dates
        LatestMonthData_s['date'] = pd.to_datetime(LatestMonthData_s['date'])
        list_Data_s = LatestMonthData_s['date'].tolist()
        Data_s = np.array(list_Data_s)

        #making a list of y cases
        list_newCases = LatestMonthData['new_cases'].tolist()
        newCases = np.array(list_newCases)

        #fitting a regression model
        model = LinearRegression().fit(Data, newCases)

        #getting latest date from data
        latest = np.amax(Data_s, axis = 0)

        #extending date upto
        extended = latest + relativedelta(months=+1)
        count = latest
        list_extension = []

        #making extra x axis data points
        while count <= extended:
                list_extension.append(count)
                count = count + relativedelta(days=+1)

        tem = pd.to_numeric(pd.to_datetime(list_extension))
        extension = np.array(tem).reshape((-1,1))
        extension_s = np.array(list_extension)

        #making a prediction
        y_pred = model.predict(extension)

        
        temp_r = datetime.strftime(datetime.now(),"%Y-%m-%d")
        temp = datetime.strptime(temp_r,"%Y-%m-%d")

        plt.plot(Data_s, newCases, 'o',label = 'NewCases')
        plt.plot(Data_s, newCases, '-')
        plt.plot(Data_s, y_pred, '-',label = 'Predictions')


        plt.title('Covid Cases latest Month')
        plt.xlabel('Date')
        plt.ylabel('New Cases')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal Cases Week
##########################################################################################################

class Canvas_N_Cases_week(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','new_cases'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Getting Last week
        lastWeek = datetime.now()+relativedelta(weeks=-1)

        #Structuring start and end Date
        start_date = datetime.strftime(lastWeek,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestWeekData = data.loc[mask]
        LatestWeekData_s = data.loc[mask]
        
        #making an array of dates
        LatestWeekData['date'] = pd.to_numeric(pd.to_datetime(LatestWeekData['date']) )
        list_Data = LatestWeekData['date'].tolist()
        Data = np.array(list_Data).reshape((-1,1))

        #Making a second array of dates
        LatestWeekData_s['date'] = pd.to_datetime(LatestWeekData_s['date'])
        list_Data_s = LatestWeekData_s['date'].tolist()
        Data_s = np.array(list_Data_s)

        #making a list of y cases
        list_newCases = LatestWeekData['new_cases'].tolist()
        newCases = np.array(list_newCases)

        TempCount = 0
        for i in Data_s:
            i = datetime.strftime(i,"%m-%d")
            Data_s[TempCount] = i
            TempCount += 1

        #fitting a regression Model
        model = LinearRegression().fit(Data, newCases)

        #making a prediction
        y_pred = model.predict(Data)
    
        plt.plot(Data_s, newCases, 'o',label = 'NewCases')
        plt.plot(Data_s, newCases, '-')
        plt.plot(Data_s, y_pred, '-',label = 'Predictions')

        plt.title('Covid Cases latest Week')
        plt.xlabel('Date')
        plt.ylabel('New Cases')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal Cases Overall
##########################################################################################################

class Canvas_N_Cases_overall(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','total_cases'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Because the data is from 25 Jan 2020 AD
        #Begining = datetime.date(2020,1,25)
        Begining = datetime.strptime("2020-01-25","%Y-%m-%d")        

        #Structuring start and end Date
        start_date = datetime.strftime(Begining,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        
        #making an array of dates
        Date = LatestMonthData['date'].tolist()

        TotalCases = LatestMonthData['total_cases'].tolist()
        plt.plot(Date, TotalCases, 'o',label = 'TotalCases')
        plt.plot(Date, TotalCases, '-')

        plt.title('Total Covid Cases Overall')
        plt.xlabel('Date')
        plt.ylabel('Total Cases')

        

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal Deaths Months
##########################################################################################################        

class Canvas_N_Deaths_mnth(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','new_deaths'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Getting Last month
        lastMnth = datetime.now()+relativedelta(months=-1)

        #Structuring start and end Date
        start_date = datetime.strftime(lastMnth,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        
        #making an array of dates
        Date = LatestMonthData['date'].tolist()

        TempCount = 0
        for i in Date:
            i = datetime.strftime(i,"%m-%d")
            Date[TempCount] = i
            TempCount += 1
        
        newDeaths = LatestMonthData['new_deaths'].tolist()
        plt.plot(Date, newDeaths, 'o',label = 'NewDeaths')
        plt.plot(Date, newDeaths, '-')

        plt.title('Covid Deaths latest Month')
        plt.xlabel('Date')
        plt.ylabel('New Deaths')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal Deaths Week
##########################################################################################################

class Canvas_N_Deaths_week(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','new_deaths'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Getting Last month
        lastMnth = datetime.now()+relativedelta(weeks=-1)

        #Structuring start and end Date
        start_date = datetime.strftime(lastMnth,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        
        #making an array of dates
        Date = LatestMonthData['date'].tolist()

        TempCount = 0
        for i in Date:
            i = datetime.strftime(i,"%m-%d")
            Date[TempCount] = i
            TempCount += 1
        
        newDeaths = LatestMonthData['new_deaths'].tolist()
        plt.plot(Date, newDeaths, 'o',label = 'NewDeaths')
        plt.plot(Date, newDeaths, '-')

        plt.title('Covid Deaths latest Week')
        plt.xlabel('Date')
        plt.ylabel('New Deaths')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal Deaths Overall
##########################################################################################################

class Canvas_N_Deaths_overall(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','total_deaths'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Because the data is from 25 Jan 2020 AD
        #Begining = datetime.date(2020,1,25)
        Begining = datetime.strptime("2020-01-25","%Y-%m-%d")
        

        #Structuring start and end Date
        start_date = datetime.strftime(Begining,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        
        #making an array of dates
        Date = LatestMonthData['date'].tolist()
        
        totalDeaths = LatestMonthData['total_deaths'].tolist()
        plt.plot(Date, totalDeaths, 'o',label = 'TotalDeaths')
        plt.plot(Date, totalDeaths, '-')

        plt.title('Total Covid Deaths Overall')
        plt.xlabel('Date')
        plt.ylabel('Total Deaths')

        #plt.xticks(ticker.AutoLocator())       #This didn't work due to empty values
        

        
        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal Total Vaccination
##########################################################################################################

class Canvas_N_TotalVaccination(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','total_vaccinations'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Because the data is from 25 Jan 2020 AD
        #Begining = datetime.date(2020,1,25)
        Begining = datetime.strptime("2020-01-25","%Y-%m-%d")
        

        #Structuring start and end Date
        start_date = datetime.strftime(Begining,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        
        #making an array of dates
        Date = LatestMonthData['date'].tolist()
        
        totalVaccination = LatestMonthData['total_vaccinations'].tolist()
        plt.plot(Date, totalVaccination, 'o',label = 'Total Vaccinations')
        plt.plot(Date, totalVaccination, '-')

        plt.title('Total Covid Vaccinations')
        plt.xlabel('Date')
        plt.ylabel('N of Vaccinations')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues

##########################################################################################################
        # Nepal People Vaccinated
##########################################################################################################

class Canvas_N_PeopleVaccinated(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """

        #Reading File
        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','people_vaccinated','people_fully_vaccinated'])
        #converting Date to proper datatype (DateTime)
        data['date'] = pd.to_datetime(data['date']) 

        #Because the data is from 25 Jan 2020 AD
        #Begining = datetime.date(2020,1,25)
        Begining = datetime.strptime("2020-01-25","%Y-%m-%d")
        

        #Structuring start and end Date
        start_date = datetime.strftime(Begining,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #Filtering data using mask
        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        #Applying mask
        LatestMonthData = data.loc[mask]
        
        #making an array of dates
        Date = LatestMonthData['date'].tolist()
        
        firstDose = LatestMonthData['people_vaccinated'].tolist()
        fullDose = LatestMonthData['people_fully_vaccinated'].tolist()
        plt.plot(Date, firstDose, 'o',label = 'First Dose')
        plt.plot(Date, firstDose, '-')
        plt.plot(Date, fullDose, 'o',label = 'Full Dose')
        plt.plot(Date, fullDose, '-')

        plt.title('Covid Vaccinations Situation')
        plt.xlabel('Date')
        plt.ylabel('N of Vaccinations')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues
