from sklearn.linear_model import LinearRegression

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

#making an array of dates
Date = LatestMonthData['date'].tolist()

TempCount = 0
for i in Date:
    i = datetime.strftime(i,"%m-%d")
    Date[TempCount] = i
    TempCount += 1

newCases = LatestMonthData['new_cases'].tolist()
plt.plot(Date, newCases, 'o',label = 'NewCases')
plt.plot(Date, newCases, '-')

plt.title('Covid Cases latest Month')
plt.xlabel('Date')
plt.ylabel('New Cases')

plt.legend()
plt.grid(True)

plt.tight_layout() # works for small screen; solves padding issues
