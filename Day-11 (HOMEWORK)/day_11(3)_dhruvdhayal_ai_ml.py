# -*- coding: utf-8 -*-
"""Day-11(3)_DHRUVDHAYAL_AI/ML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X5ME3MJ5dEfVEDhvjhrw-8gul4xvQks2

#Time Series ForeCasting.
"""

#Importing the Inbuilt Libraries.
from statsmodels.tsa import seasonal,arima_model;
import pandas as pd;
import numpy as np;

#Importing the Values of the Data.
data=pd.read_csv("/content/AirPassengers.csv");

#printing the Values of the data.
print("\n 1. Total Length of the Data: ",data.shape);
data.head();

#Information of the Data Values.
data.info();

#Convert the Month Column into Text and into the DataTime.
data["Month"]=pd.to_datetime(data["Month"]);
data.head();

data.head(50);

#Set the Month Column as the Index of the Pandas DataFiles.
data.set_index("Month",inplace=True);
data.head();

#Let's Visualise the Data.
import matplotlib.pyplot as plt;
data["#Passengers"].plot(figsize=(5,3));
plt.title("Passengers");
plt.xlabel("Month");
plt.ylabel("Passengers");
plt.show();

tempData=data["#Passengers"];
OrigData=tempData.copy();

var=seasonal.seasonal_decompose(tempData);
plt.figure(1,figsize=(10,10));
plt.subplot(2,2,1);
var.observed.plot();
plt.title("Original Plot");

plt.subplot(2,2,2);
var.trend.plot();
plt.title("Trend Plot");

plt.subplot(2,2,3);
var.seasonal.plot();
plt.title("Seasonal Plot");

plt.subplot(2,2,4);
var.resid.plot();
plt.title("Residual Plot");

#Let's Create the ForeCaster.
import statsmodels.api as st;

sarima_model = st.tsa.statespace.SARIMAX(tempData,order=(1,1,1),seasonal_order=(1,1,1,12))
#Train the Model.
sarima_model = sarima_model.fit()

# forecaste the value
value_for= sarima_model.forecast()
print(value_for)

tempData.tail();

# i want to forecast the one year data

num_samples = 12

for i in range(num_samples):
  sarima_model = st.tsa.statespace.SARIMAX(tempData,order=(1,1,1),seasonal_order=(1,1,1,12))
  # train the model
  sarima_model = sarima_model.fit()
  # forecast the value
  value_for= sarima_model.forecast()
  tempData

tempData = pd.concat([tempData, value_for])
tempData.tail()

plt.figure(1)
tempData.plot(label='forecasted')
OrigData.plot(label='Original')
plt.legend()
plt.grid('on')

!pip install pmdarima

from pmdarima import auto_arima;
auto_arima(tempData,seasonal=True,m=12,trace=True)

# i want to forecast the one year data
tempData = data['#Passengers']
num_samples = 12

for i in range(num_samples):
  sarima_model = st.tsa.statespace.SARIMAX(tempData,order=(2,1,1),seasonal_order=(2,1,0,12))
  # train the model
  sarima_model = sarima_model.fit()
  # forecast the value
  value_for= sarima_model.forecast()
  tempData = pd.concat([tempData, value_for])

plt.figure(1)
tempData.plot(label='forecasted')
OrigData.plot(label='Original')
plt.legend()
plt.grid('on')

"""#Now, we Need to Drop the 2-Years of Data and then we have to predict and compatre it with the Original Values of the Data."""

newData = data.iloc[:-24] # -24 means from the end 24 samples deducted
newData.tail()
# i want to forecast the one year data
tempData = newData['#Passengers']
num_samples = 24

for i in range(num_samples):
  sarima_model = st.tsa.statespace.SARIMAX(tempData,order=(2,1,1),seasonal_order=(2,1,0,12))
  # train the model
  sarima_model = sarima_model.fit()
  # forecast the value
  value_for= sarima_model.forecast()
  tempData = pd.concat([tempData, value_for])

plt.figure(1)
tempData.plot(label='forecasted')
newData.plot(label='Original')
plt.legend()
plt.grid('on')

plt.figure(1)
tempData.plot(label='forecasted')
newData.plot(label='Original')
plt.legend()
plt.grid('on')

plt.figure(1)
plt.plot(tempData,label='forecasted')
plt.plot(data,label='Original')
ax = plt.legend()
ax = plt.grid('on')

"""#Milk-Productions Data."""

#Importing the Inbuilt Libraries.
from statsmodels.tsa import seasonal,arima_model;
import pandas as pd;
import numpy as np;

#Importing the Values of the Data.
data=pd.read_csv("/content/milk_production_dataset.csv");

#printing the Values of the data.
print("\n 1. Total Length of the Data: ",data.shape);
data.head();

#Information of the Data.
data.info();

# Remove the first row (assumed to be a header) and reset the index
data = data.iloc[1:].reset_index(drop=True)
# Now try converting the 'Month' column to 'datetime'
# Handle potential format variations using 'infer_datetime_format'
data['Month'] = pd.to_datetime(data['Month'], infer_datetime_format=True, errors='coerce')
# 'errors='coerce'' will set invalid parsing to NaT (Not a Time) which can be handled later
data.info()

data.head(50);

#Set the Month Column as the Index of the Pandas DataFiles.
data.set_index("Month",inplace=True);
data.head();

#Let's Visualise the Data.
import matplotlib.pyplot as plt
# visualise the data
data['Monthly milk production'].plot(figsize=(5,3))

import matplotlib.pyplot as plt
from statsmodels.tsa import seasonal

tempData = data['Monthly milk production']
OrigData = tempData.copy()

# Handle missing values (e.g., fill with the mean)
tempData = tempData.fillna(tempData.mean())  # Or use another method like forward fill or interpolation

# Check for and remove duplicate dates
tempData = tempData[~tempData.index.duplicated()] #This line removes duplicate dates

# Ensure the Datetime Index is complete for monthly frequency
tempData = tempData.asfreq('MS') # This line is added to ensure the DatetimeIndex has a monthly frequency

# Now you can set the frequency explicitly
tempData.index.freq = 'MS'

var = seasonal.seasonal_decompose(tempData);
plt.figure(1,(8,10))
plt.subplot(2,2,1)
var.observed.plot()
plt.title('Original Plot');

plt.subplot(2,2,2)
var.trend.plot()
plt.title('Trend identification');

plt.subplot(2,2,3)
var.seasonal.plot()
plt.title('Seasonality identification');

plt.subplot(2,2,4)
var.resid.plot()
plt.title('Residual');

# lets create the forecaster

sarima_model = st.tsa.statespace.SARIMAX(tempData,order=(1,1,1),seasonal_order=(1,1,1,12))
# train the model
sarima_model = sarima_model.fit()

# forecaste the value
value_for= sarima_model.forecast()
print(value_for)

tempData.tail()

# i want to forecast the one year data
tempData = data['Monthly milk production']
num_samples = 12

for i in range(num_samples):
  sarima_model = st.tsa.statespace.SARIMAX(tempData,order=(1,1,1),seasonal_order=(1,1,1,12))
  # train the model
  sarima_model = sarima_model.fit()
  # forecast the value
  value_for= sarima_model.forecast()
  tempData = pd.concat([tempData, value_for])

plt.figure(1)
tempData.plot(label='forecasted')
OrigData.plot(label='Original')
plt.legend()
plt.grid('on')
