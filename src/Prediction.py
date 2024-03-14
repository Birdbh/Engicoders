import sklearn as sk
import numpy as np
import datetime as dt

class DataPrediction:
    def __init__(self, sensor, prediction_timeframe,model_name):
        self.prediction_timeframe = prediction_timeframe
        self.X = sensor.value.keys()
        self.Y = sensor.value.values()
        self.X_future = None
        self.forcasted_values = sensor.forcasted_values
        self.model = self.select_model(model_name)

    def select_model(model_name):
        if model_name == 'linear_regression':
            return sk.LinearRegression()
        elif model_name == 'random_forest':
            return sk.RandomForestRegressor()
        elif model_name == 'svm':
            return sk.SVR()
        else:
            raise ValueError("Invalid model name. Please choose from 'linear_regression', 'random_forest', or 'svm'.")

    def predict(self):
        self.forcasted_values = self.model.predict(self.X_future)
    
    def re_format_data(self):
        self.X = np.array([date.toordinal() for date in self.X]).reshape(-1, 1)
        self.Y = np.array(self.Y)

    def train_model(self):
        self.model.fit(self.X, self.Y)

    def set_prediction_timeframe(self):
        start_prediction_date = max(self.X + dt.timedelta(days=1))

        time_increment = self.X[-1] - self.X[-2]

        future_dates = [start_prediction_date]

        while start_prediction_date + time_increment <= self.prediction_timeframe:
            start_prediction_date += time_increment
            future_dates.append(start_prediction_date)

        self.X_future = np.array([date.toordinal() for date in future_dates]).reshape(-1, 1)

    def convert_prediction_to_dict(self):
        self.forcasted_values = dict(zip(self.X_future, self.forcasted_values))

