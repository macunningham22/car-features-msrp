import pandas as pd
import numpy as np

# import a csv file
df = pd.read_csv('data.csv')
df2 = pd.DataFrame(df, columns=['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders', 'Transmission Type', 'Driven_Wheels', 'Number of Doors', 'Market Category', 'Vehicle Size', 'Vehicle Style', 'highway MPG', 'city mpg', 'Popularity', 'MSRP'])
print(df2['Make'])
