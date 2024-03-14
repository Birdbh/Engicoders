import sklearn as sk
import numpy as np

class DataPrediction:
    def __init__(self, sensor):
        self.X = sensor.value.keys()
        self.Y = sensor.value.values()
        self.X_future = None
        self.forcasted_values = sensor.forcasted_values
        self.model = None

    def select_model(self, model_name):
        if model_name == 'linear_regression':
            self.model = sk.LinearRegression()
        elif model_name == 'random_forest':
            self.model = sk.RandomForestRegressor()
        elif model_name == 'svm':
            self.model = sk.SVR()
        else:
            raise ValueError("Invalid model name. Please choose from 'linear_regression', 'random_forest', or 'svm'.")

    def predict(self):
        self.forcasted_values = self.model.predict(self.X)
        return self.model.predict(self.data)
    
    def re_format_data(self):
        self.X = np.array([date.toordinal() for date in self.X]).reshape(-1, 1)
        self.Y = np.array(self.Y)

    def train_model(self):
        self.model.fit(self.X, self.Y)