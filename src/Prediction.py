<<<<<<< HEAD
from sklearn import linear_model as lm
import numpy as np
import datetime as dt
from DataGeneration import DataGeneration
from sensors.sensor import Sensor
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


#Create a class that will predict future values of a sensor
#The class will take in a sensor object and a prediction end date
#The class will calculate the prediction intervals and the prediction start date from the sensor object values
#


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
=======
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
<<<<<<< HEAD
            self.model = sk.SVR()
>>>>>>> 0ad22b0 (Create Prediction class that will take a sensor object and fill the prediction field based on a set of possible prediction algorithms.)
=======
            return sk.SVR()
>>>>>>> 959ddc5 (Create Prediction class that will take a sensor object and fill the prediction field based on a set of possible prediction algorithms.)
        else:
            raise ValueError("Invalid model name. Please choose from 'linear_regression', 'random_forest', or 'svm'.")

    def predict(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        number_past_entries = len(self.X)
        number_of_future_entries = len(self.X_future)

        prediction_times = [i for i in range(number_past_entries, number_past_entries + number_of_future_entries)]

        self.forcasted_values = self.model.predict(np.array(prediction_times).reshape(-1,1))

    def train_model(self):
        train_times = np.array([i for i in range(len(self.X))]).reshape(-1,1)

        x = np.nan_to_num(train_times, copy=True, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float)

        y = np.nan_to_num(np.array(self.Y).reshape(-1,1), copy=True, nan=0.0, posinf=0.0, neginf=0.0)

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

dates1 = list(sensor.value.keys())
dates2 = list(predict.forcasted_values.keys())

values1 = list(sensor.value.values())

for i in range(0,len(values1)):
    if values1[i] == None:
        values1[i] = (float(values1[i-1])+float(values1[i+1]))/2

values2 = list(predict.forcasted_values.values())
             

plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
plt.plot(dates1, values1, label='Dataset 1')  # Plot the first dataset
plt.plot(dates2, values2, label='Dataset 2', linestyle='--')  # Plot the second dataset with a different style

# Formatting the plot
plt.xlabel('Date')  # Set x-axis label
plt.ylabel('Value')  # Set y-axis label
plt.title('Comparison of Two Datasets')  # Set title
plt.legend()  # Show legend to differentiate the datasets
plt.grid(True)  # Show grid for better readability
plt.xticks(rotation=45)  # Rotate dates for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated date labels

plt.show() 
=======
        return self.model.predict(self.data)
>>>>>>> 0ad22b0 (Create Prediction class that will take a sensor object and fill the prediction field based on a set of possible prediction algorithms.)
=======
        self.forcasted_values = self.model.predict(self.X)
        return self.model.predict(self.data)
=======
        self.forcasted_values = self.model.predict(self.X_future)
>>>>>>> b363158 (Added code to control prediction making)
    
    def re_format_data(self):
        self.X = np.array([date.toordinal() for date in self.X]).reshape(-1, 1)
        self.Y = np.array(self.Y)

    def train_model(self):
        self.model.fit(self.X, self.Y)
<<<<<<< HEAD
>>>>>>> 1d851bf (Create Prediction class that will take a sensor object and fill the prediction field based on a set of possible prediction algorithms.)
=======

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

>>>>>>> b363158 (Added code to control prediction making)
