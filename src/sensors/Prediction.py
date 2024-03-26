from sklearn import linear_model as lm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
from pmdarima import auto_arima

import sys 
sys.path.append("src")

from sensors.DecoratorPattern import SensorDataDecorator

#Create a class that will predict future values of a sensor
#The class will take in a sensor object and a prediction end date
#The class will calculate the prediction intervals and the prediction start date from the sensor object values


class DataPrediction(SensorDataDecorator):
    def __init__(self, sensor, prediction_end_date):
        
        super().__init__(sensor)
        self.X = sensor.get_date_range()
        self.prediction_intervals = self.X[-1] - self.X[-2]
        self.prediction_start_date = self.X[-1] + self.prediction_intervals
        self.prediction_end_date = prediction_end_date

        self.Y = sensor.get_value()

        self.X_future = None
        self.forcasted_values = None

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

        auto_arima_model = auto_arima(df, seasonal=True, stepwise=True, suppress_warnings=True, error_action="ignore", trace=True)

        best_order = auto_arima_model.order
        best_seasonal_order = auto_arima_model.seasonal_order

        model = SARIMAX(df, order=best_order, seasonal_order=best_seasonal_order)

        fitted_model = model.fit()

        self.model = fitted_model

    def process_data(self):
        super().process_data()
        X = self.sensor.get_date_range()
        Y = self.sensor.get_value()
        self.set_prediction_timeframe()
        self.train_model()
        self.predict()
        X_future = self.X_future
        Y_future = self.forcasted_values
        return X+X_future, Y+Y_future

