#importing libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#read DataSet
addr = "student_scores.csv"
s_data = pd.read_csv(addr)
print("Data imported successfully")
dataS = s_data.head(10)
print(dataS)

#plotting score distribution
s_data.plot(x='Hours', y='Scores', style='o')
plt.title('Studied Hours Graph')
plt.xlabel('Hours')
plt.ylabel('Marks %')
plt.show()

#classification of data for in and out
X = s_data.iloc[:, :-1].values
y = s_data.iloc[:, 1].values
