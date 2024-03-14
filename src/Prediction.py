from sklearn import linear_model as lm
import numpy as np
import datetime as dt
from DataGeneration import DataGeneration
from sensors.sensor import Sensor

class DataPrediction:
    def __init__(self, sensor, prediction_end_date, model_name):
        self.X = list(sensor.value.keys())
        self.prediction_intervals = self.X[-1] - self.X[-2]
        self.prediction_start_date = self.X[-1] + self.prediction_intervals
        self.prediction_end_date = prediction_end_date

        self.Y = list(sensor.value.values())
        self.X_future = None
        self.forcasted_values = sensor.forcasted_values

        self.model = self.select_model(model_name)

    def select_model(self, model_name):
        if model_name == 'linear_regression':
            return lm.LinearRegression()
        elif model_name == 'random_forest':
            return lm.RandomForestRegressor()
        elif model_name == 'svm':
            return lm.SVR()
        else:
            raise ValueError("Invalid model name. Please choose from 'linear_regression', 'random_forest', or 'svm'.")

    def predict(self):
        number_past_entries = len(self.X)
        number_of_future_entries = len(self.X_future)

        prediction_times = [i for i in range(number_past_entries, number_past_entries + number_of_future_entries)]

        self.forcasted_values = self.model.predict(np.array(prediction_times).reshape(-1,1))

    def train_model(self):
        train_times = np.array([i for i in range(len(self.X))]).reshape(-1,1)

        x = np.nan_to_num(train_times, copy=True, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float)
        print(x)
        y = np.nan_to_num(np.array(self.Y).reshape(-1,1), copy=True, nan=0.0, posinf=0.0, neginf=0.0)
        print(y)

        for i in range(0,len(y)):
            if y[i] == None:
                y[i] = (y[i-1].astype(np.float)+y[i+1].astype(np.float))/2

        self.model.fit(x.reshape(-1,1), y.reshape(-1,1))

    def set_prediction_timeframe(self):

        current_date = self.prediction_start_date

        future_dates = [current_date]

        while current_date + self.prediction_intervals <= self.prediction_end_date:
            current_date += self.prediction_intervals
            future_dates.append(current_date)

        self.X_future = future_dates

    def convert_prediction_to_dict(self):
        self.forcasted_values = dict(zip(self.X_future, self.forcasted_values))


time_series = DataGeneration(9, 30, 1, '2024-03-13 00:00:00').get_time_series()

sensor = Sensor(1, 'Temperature Sensor', 'A sensor that measures temperature', 'float', time_series)

predict = DataPrediction(sensor, dt.datetime(2024, 3, 17, 0, 0, 0), 'linear_regression')

predict.set_prediction_timeframe()
predict.train_model()
predict.predict()
predict.convert_prediction_to_dict()

print(predict.forcasted_values)


