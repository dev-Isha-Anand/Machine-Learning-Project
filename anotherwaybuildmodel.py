import os
import pickle
import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Reading the data from the given raw file
raw_dat = pd.read_csv('./DSDataLastThreeMonths.csv')

# Removing null values for further analysis
raw_dat = raw_dat.dropna().reset_index()

# Extracting the independent variable, X
x_data = raw_dat.loc[:, ['HM_WT', 'AIM_S', 'HM_S', 'HM_C', 'HM_SI', 'HM_TI', 'HM_MN', 'CAC2', 'MG', 
                         'HM_TEMP', 'CAC2_INJ_TIME', 'MG_INJ_TIME']]

# Extracting the dependent variable, y
y_data = raw_dat.loc[:, 'DS_S']

random_seed = 42
random.seed(random_seed)

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.33, random_state=random_seed)

# Scaling the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def build_model(X, y):
    clf = LinearRegression()
    clf.fit(X, y)
    return clf

def evaluate_model(model, X, y, dataset_type):
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    hit_rate = np.mean(np.abs(y_pred - y) <= 0.003)
    print(f'{dataset_type} Mean Squared Error: {mse}')
    print(f'{dataset_type} R-squared: {r2}')
    print(f'{dataset_type} Model Hit Rate: {hit_rate * 100:.2f}%')
    return y_pred, mse, r2, hit_rate

# Build the model
model = build_model(X_train, y_train)

# Evaluate model on train dataset
print("Evaluating model on training data...")
pred_train, mse_train, r2_train, hit_rate_train = evaluate_model(model, X_train, y_train, 'Train')

# Evaluate model on test dataset
print("Evaluating model on testing data...")
pred_test, mse_test, r2_test, hit_rate_test = evaluate_model(model, X_test, y_test, 'Test')

# Tolerance range
check = 0.003

# Finding the error on the predictions
err_test = [x - y for x, y in zip(pred_test, y_test)]
err_train = [x - y for x, y in zip(pred_train, y_train)]

# Finding the strike rates on the datasets
strike_rate_test = 100 * sum([np.abs(x) <= check for x in err_test]) / len(err_test)
strike_rate_train = 100 * sum([np.abs(x) <= check for x in err_train]) / len(err_train)

# Printing the results
print("Final results:")
print("Test strike rate: {}\nTrain strike rate: {}".format(strike_rate_test, strike_rate_train))

# Saving the model and results
save_object = (model, pred_test, strike_rate_test, strike_rate_train, random_seed)
with open("team_name.pkl", "wb") as pickle_out:
    pickle.dump(save_object, pickle_out)
