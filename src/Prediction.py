import sklearn as sk

class DataPrediction:
    def __init__(self, sensor):
        self.sensor = sensor
    
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
        return self.model.predict(self.data)