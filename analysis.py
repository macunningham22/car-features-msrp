import pandas as pd
import numpy as np
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression

# import a csv file
dataset = pd.read_csv('data.csv')
df = pd.DataFrame(dataset, columns=['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders', 'Transmission Type', 'Driven_Wheels', 'Number of Doors', 'Market Category', 'Vehicle Size', 'Vehicle Style', 'highway MPG', 'city mpg', 'Popularity', 'MSRP'])


target1 = pd.DataFrame(df, columns=['Highway MPG'])
target2 = pd.DataFrame(df, columns=['City MPG'])

y_highway_mpg = target1['Highway MPG']
y_city_mpg = target2['City MPG']
x = df['Year']

reg_city_mpg = LinearRegression()


# add a constant to the independent variable
# x = sm.add_constant(x)



# write a function to perform a linear regression 
def linear_regression(x, y):
    # fit the model
    reg_city_mpg.fit(x, y)
    # print the intercept
    print(reg_city_mpg.intercept_)
    # print the coefficient
    print(reg_city_mpg.coef_)
    # print the R-squared
    print(reg_city_mpg.score(x, y))
    # print the p-value
    print(reg_city_mpg.pvalues_)

# call the function
linear_regression(x, y_city_mpg)