import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('Solar.csv')
X = dataset.iloc[:, [2,3,4,6,7,8,11,12,13]].values
y = dataset.iloc[:, -1].values
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)

def predict(attri):
    attri = attri[1:-1]
    attri = attri.split(',')
    print(attri)
    for i in range(len(attri)):
        attri[i] = int(attri[i])
    predictions = regressor.predict([attri])
    response = int(predictions[0])
    return response
