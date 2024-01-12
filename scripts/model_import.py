import pickle
import pandas as pd
import joblib
from datetime import datetime, timedelta


class ModelPredictor:
    def __init__(self):
        self.model_path = 'svm_model.pkl'
        self.scaler_path = 'scaler.pkl'
        self.data_path = "../csv/runtime.csv"
        

    def load_model(self):
        with open(self.model_path, 'rb') as file:
            self.loaded_model = pickle.load(file)

    def load_data(self):
        self.df = pd.read_csv(self.data_path)
        self.Xq = self.df.iloc[:, :16]  # Features
        self.yq = self.df.iloc[:, 16]  # Labels

    def load_scaler(self):
        self.scaler = joblib.load(self.scaler_path)

    def transform_data(self):
        self.Xq = self.scaler.transform(self.Xq)

    def make_predictions(self):
        self.predictions = self.loaded_model.predict(self.Xq)
        return self.predictions
    
    
        
        

    def process(self):
        self.load_model()
        self.load_data()
        self.load_scaler()
        self.transform_data()
        pred = self.make_predictions()
        
        return pred



