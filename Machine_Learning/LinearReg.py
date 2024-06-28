import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


data = pd.read_csv(r'C:\Users\akans\Downloads\ames.csv')
data = data.dropna(subset = ['SalePrice'])
data = data.dropna(subset = ['Lot.Frontage'])

y = data['SalePrice']
x = data['Lot.Frontage']

x = x.values.reshape(len(x),1)
y = y.values.reshape(len(y),1)

# Split data into training and testing sets
x_train = x[:-2000]
x_test = x[-2000:]
y_train = y[:-2000]
y_test = y[-2000:]

# Create and train a linear regression model
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

# Plot the test data and the regression line predicted by the model
plt.scatter(x_test,y_test, color = 'green')
plt.plot(x_test,regr.predict(x_test), color = 'red', linewidth = 3)
plt.title('Test Data')
plt.xlabel('size')
plt.ylabel('price')
plt.show()
