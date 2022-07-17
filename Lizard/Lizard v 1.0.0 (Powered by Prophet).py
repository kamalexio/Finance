#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install yfinance
#!pip install prophet
#!pip install ipywidgets
#!pip install plotly

import yfinance as yf
import datetime
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from datetime import datetime, timedelta


# In[ ]:


ticker = input("Enter ticker:")
data = yf.download(ticker, period = 'max',  interval = '1d')['Adj Close']
data1 = data.reset_index()
data2 = data1.rename(columns={"Date": "ds", "Adj Close": "y"})

m = Prophet()
m.fit(data2)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)

startdate = datetime.today().strftime('%Y-%m-%d')
enddate = datetime.today() + timedelta(days = 4)
mask = (forecast['ds'] >= startdate) & (forecast['ds'] <= enddate)
forecast2 = forecast.loc[mask]
forecast3 = forecast2.rename(columns={"ds": "Date", "yhat_lower": "Low", "yhat": "Fit", "yhat_upper": "High", "trend": "Trend",})
print(forecast3[['Date','Low','Fit','High','Trend']])


# In[ ]:


plot_plotly(m,forecast)


# In[ ]:


plot_components_plotly(m,forecast)

