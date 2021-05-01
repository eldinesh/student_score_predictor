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
