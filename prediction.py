# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:31 2019

@author: Chaitra
"""
#execute everyting in jupyter stepwise 
#recommended to use google colab

import pandas as pd
data_croma = pd.read_csv("oppo f11 pro croma1.csv",index_col=0)
data_flip = pd.read_csv("oppo fll pro flipkart 1.csv", index_col = 0)
data_snap = pd.read_csv("oppo fll pro snapdeal1.csv", index_col=0)

data_croma.head()
data_flip.head()
data_snap.head()

data_croma.index
data_flip.index
data_snap.index

data_croma.index = pd.to_datetime(data_croma.index)
data_flip.index = pd.to_datetime(data_flip.index)
data_snap.index = pd.to_datetime(data_snap.index)

data_croma.head()
data_flip.head()
data_snap.head()

data_croma.index
data_flip.index
data_snap.index

data_croma.columns = ['price']
data_flip.columns = ['price']
data_snap.columns = ['price']

data_croma.head()
data_flip.head()
data_snap.head()

import plotly
from plotly.plotly import plot_mpl
from statsmodels.tsa.seasonal import seasonal_decompose

result_croma = seasonal_decompose(data_croma, model='multiplicative', freq=1)
result_flip = seasonal_decompose(data_flip, model='multiplicative', freq=1)
result_snap = seasonal_decompose(data_snap, model='multiplicative', freq=1)

plotly.tools.set_credentials_file(username='sahana369', api_key='qN7b19SDafUpo4hPsXZP')

fig1_croma = result_croma.plot()
fig1_flip = result_flip.plot()
fig1_snap = result_snap.plot()

import plotly.plotly as ply
import cufflinks as cf

data_croma.iplot(title="price range", theme='pearl')
data_flip.iplot(title="price range", theme='pearl')
data_snap.iplot(title="price range", theme='pearl')

pip install pmdarima

from pmdarima.arima import auto_arima

stepwise_model_croma = auto_arima(data_croma, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=1,
                           start_P=0, seasonal=False,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

stepwise_model_flip = auto_arima(data_flip, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=1,
                           start_P=0, seasonal=False,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

stepwise_model_snap = auto_arima(data_snap, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=1,
                           start_P=0, seasonal=False,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

stepwise_model_croma.aic()

stepwise_model_flip.aic()

stepwise_model_snap.aic()

data_croma.head()
data_flip.head()
data_snap.head()

train_croma = data_croma.loc['2019-03-19':'2019-04-30']
train_flip = data_flip.loc['2019-03-19':'2019-04-30']
train_snap = data_snap.loc['2019-03-19':'2019-04-30']

train_croma.tail()
train_flip.tail()
train_snap.tail()

test_croma = data_croma.loc['2019-04-30':]
test_flip = data_flip.loc['2019-04-30':]
test_snap = data_snap.loc['2019-04-30':]

test_croma.head()
test_flip.head()
test_snap.head()

test_croma.tail()
test_flip.tail()
test_snap.tail()


len(test_croma)

len(train_croma)
#fitting model to data

stepwise_model_flip.fit(train_flip)

stepwise_model_snap.fit(train_snap)

#forecasting

#croma
future_forecast_croma = stepwise_model_croma.predict(n_periods=5)
future_forecast_croma

#flipkart
future_forecast_flip = stepwise_model_flip.predict(n_periods=5)
future_forecast_flip

#snapdeal
future_forecast_snap = stepwise_model_snap.predict(n_periods=5)
future_forecast_snap