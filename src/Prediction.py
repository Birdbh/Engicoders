from sklearn import linear_model as lm
import numpy as np
import datetime as dt
from DataGeneration import DataGeneration
from sensors.sensor import Sensor
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from pmdarima import auto_arima
from sensors.Cleanser import cleanser


#Create a class that will predict future values of a sensor
#The class will take in a sensor object and a prediction end date
#The class will calculate the prediction intervals and the prediction start date from the sensor object values


class DataPrediction:
    def __init__(self, sensor, prediction_end_date, model_name):
        
        self.X = list(sensor.value.keys())
        self.prediction_intervals = self.X[-1] - self.X[-2]
        self.prediction_start_date = self.X[-1] + self.prediction_intervals
        self.prediction_end_date = prediction_end_date

        self.Y = list(sensor.value.values())

        self.X_future = None
        self.forcasted_values = sensor.forcasted_values

        self.model = None

    
    def set_prediction_timeframe(self):

        current_date = self.prediction_start_date

        future_dates = [current_date]

        while current_date + self.prediction_intervals <= self.prediction_end_date:
            current_date += self.prediction_intervals
            future_dates.append(current_date)

        self.X_future = future_dates

    def predict(self):

        predictions = self.model.forecast(steps=len(self.X_future))

        self.forcasted_values = predictions.to_list()

    def train_model(self):

        df = pd.DataFrame(data=self.Y, index=self.X, columns=['Value'])

        auto_arima_model = auto_arima(df, seasonal=False, stepwise=True, suppress_warnings=True, error_action="ignore", max_order=None, trace=True)

        best_order = auto_arima_model.order

        model = ARIMA(df, order=best_order)
        fitted_model = model.fit()

        self.model = fitted_model

    def convert_prediction_to_dict(self):
        self.forcasted_values = dict(zip(self.X_future, self.forcasted_values))