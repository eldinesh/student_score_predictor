#importing libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#read DataSet
addr = "student_scores.csv"
s_data = pd.read_csv(addr)
print("Data imported successfully")
dataS = s_data.head(10)
#print(dataS)

#plotting score distribution
s_data.plot(x='Hours', y='Scores', style='o')
plt.title('Studied Hours Graph')
plt.xlabel('Hours')
plt.ylabel('Marks %')
#plt.show()

#classification of data for in and out
x = s_data.iloc[:, :-1].values
y = s_data.iloc[:, 1].values

from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#Training Algorithm
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(x_train, y_train) 
print("Training Completed")

# Plotting the regression line
line = regressor.predict(x)

# Plotting for the test data
plt.scatter(x, y)
plt.plot(x, line);
plt.show()
