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
LatestMonthData['date'] = pd.to_numeric(pd.to_datetime(LatestMonthData['date']))
list_Data = LatestMonthData['date'].tolist()
Data = np.array(list_Data).reshape((-1,1))

#Making a second array of dates
LatestMonthData_s['date'] = pd.to_datetime(LatestMonthData_s['date'])
list_Data_s = LatestMonthData_s['date'].tolist()
Data_s = np.array(list_Data_s)

#making a list of y cases
list_newCases = LatestMonthData['new_cases'].tolist()
newCases = np.array(list_newCases)

#fitting a regression Model
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

print(extension_s,y_pred)

plt.plot(extension_s, y_pred, 'x', label = 'Prediction')
plt.plot(extension_s, y_pred, '--')
plt.plot(Data_s, newCases, 'o', label = 'New Cases')
plt.plot(Data_s, newCases, '-')

plt.title('Covid Cases latest Week')
plt.xlabel('Date')
plt.ylabel('New Cases')

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()

