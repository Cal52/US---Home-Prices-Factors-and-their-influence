# -*- coding: utf-8 -*-
"""Model_home

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cYehngZHKIE5RhgXEEJHHRH0YpmAonYN
"""

import pandas as pd
import os

# New  Directory Cleaned data for storing filtered  data from 2003-2024

directory_path = "Cleaned data"
os.makedirs(directory_path, exist_ok=True)

"""Unemployment Rate : Contains data about unemployment records"""

umemployment_rate = pd.read_csv('/UNRATE (1).csv')
umemployment_rate.head()

# Filtering data from 2003-2024 and renaming column
umemployment_rate.set_index('DATE', inplace =True)
umemployment_rate.rename(columns= {'UNRATE': 'umemployment_rate'}, inplace =True)
umemployment_rate.index = pd.to_datetime(umemployment_rate.index)
umemployment_rate = umemployment_rate["2003-01-01":"2024-01-01"]

# transfer to new directory of filitered data
umemployment_rate.to_csv('/content/Cleaned data/umemployment_rate.csv')

"""Personal Income"""

income = pd.read_csv('/PI (2).csv')
income.head()

# filtering data
income.set_index('DATE', inplace =True)
income.rename(columns= {'PI': 'income'}, inplace =True)
income.index = pd.to_datetime(income.index)
income = income["2003-01-01":"2024-01-01"]
# transfer to new directory
income.to_csv('/content/Cleaned data/income.csv')

"""Employment Ratio : Contains records of employment -population ratio"""

emratio = pd.read_csv('/EMRATIO (3).csv')
emratio.head()

!pip install pandas

import pandas as pd

emratio = pd.read_csv('/EMRATIO (3).csv')
emratio.set_index('DATE', inplace =True)
emratio.rename(columns= {'EMRATIO': 'emratio'}, inplace =True) # Rename column to 'emratio'
emratio.index = pd.to_datetime(emratio.index)
emratio = emratio["2003-01-01":"2024-01-01"]

emratio.to_csv('/content/Cleaned data/emratio.csv')

"""Mortage Rate"""

mortage_rate= pd.read_csv('/MORTGAGE30US (3).csv')
mortage_rate.head()

mortage_rate.set_index('DATE', inplace =True)
mortage_rate.rename(columns= {'MORTGAGE30US': 'mortage_rate'}, inplace =True)
mortage_rate.index = pd.to_datetime(mortage_rate.index)
mortage_rate = mortage_rate["2003-01-01":"2024-01-01"]


mortage_rate.to_csv('/content/Cleaned data/mortage_rate.csv')

"""New Home : Construction Completed"""

new_home = pd.read_csv('/COMPUTSA (1).csv')
new_home.head()

new_home = pd.read_csv('/COMPUTSA (1).csv')

# Check the column names to find the correct date column
print(new_home.columns)

# Set index to DATE
new_home.set_index('DATE', inplace=True)

new_home.rename(columns={'COMPUTSA': 'new_home'}, inplace=True)
new_home.index = pd.to_datetime(new_home.index)
new_home = new_home["2003-01-01":"2024-01-01"]

# transfer to cleaned data

new_home.to_csv('/content/Cleaned data/new_home.csv')

"""Personal Saving Interest Rates"""

personal_saving = pd.read_csv('/PSAVERT (2).csv')
personal_saving.head()

personal_saving.set_index('DATE', inplace =True)
personal_saving.rename(columns= {'PSAVERT': 'personal_saving'}, inplace =True)
personal_saving.index = pd.to_datetime(personal_saving.index)
personal_saving = personal_saving["2003-01-01":"2024-01-01"]

personal_saving.to_csv('/content/Cleaned data/personal_saving.csv')

"""Homeowner  Vacany Rate : The homeowner vacancy rate is the proportion of the homeowner inventory that is vacant for sale."""

homeowner_vacancy = pd.read_csv('/RHVRUSQ156N (2).csv')
homeowner_vacancy.head()

homeowner_vacancy.set_index('DATE', inplace =True)
homeowner_vacancy.rename(columns= {'homeowner_vacany_df': 'homeowner_vacancy'}, inplace =True)
homeowner_vacancy.index = pd.to_datetime(homeowner_vacancy.index)
homeowner_vacancy = homeowner_vacancy["2003-01-01":"2024-01-01"]

homeowner_vacancy.to_csv('/content/Cleaned data/homeowner_vacancy.csv')

under_const = pd.read_csv('/UNDCONTSA (3).csv')
under_const.head()

under_const = pd.read_csv('/UNDCONTSA (3).csv')
# Print the columns to verify the correct column name for the date
print(under_const.columns)

under_const.set_index('DATE', inplace =True)
under_const.rename(columns= {'UNDCONTSA': 'under_const'}, inplace =True)
under_const.index = pd.to_datetime(under_const.index)
under_const = under_const["2003-01-01":"2024-01-01"]

under_const.to_csv('/content/Cleaned data/under_const.csv')

"""Population of United States"""

population = pd.read_csv('/POPTHM (2).csv')
population.head()

!pip install pandas

import pandas as pd

population = pd.read_csv('/POPTHM (2).csv')

# Print the columns to verify the correct column name for the date
print(population.columns)

population.set_index('DATE', inplace=True)
population.rename(columns={'POPTHM': 'population'}, inplace=True)
population.index = pd.to_datetime(population.index)
population = population["2003-01-01":"2024-01-01"]

population.to_csv('/content/Cleaned data/population.csv')

"""The S&P CoreLogic Case-Shiller U.S. National Home Price Index (“the U.S. national index”) measures the value of single-family housing within the United States. The index is a composite of single-family home price indices for the nine U.S. Census divisions and is calculated monthly."""

shiller_index = pd.read_csv('/CSUSHPINSA.csv')
shiller_index.head()

shiller_index = pd.read_csv('/CSUSHPINSA.csv')
# Print the columns to verify the correct column name for the date
print(shiller_index.columns)

shiller_index.set_index('DATE', inplace =True)
shiller_index.rename(columns= {'CSUSHPISA': 'shiller_index'}, inplace =True)
shiller_index.index = pd.to_datetime(shiller_index.index)
shiller_index = shiller_index["2003-01-01":"2024-01-01"]

# Save the cleaned data
shiller_index.to_csv('/content/Cleaned data/shiller_index.csv')

"""Gross Domestic Product"""

gdp = pd.read_csv('/GDP (2).csv')
gdp.head()

# Setting DATE as index, column renaming, setting DATE as index, filtering data from "1987-01-01":"2024-07-01"

gdp.set_index('DATE', inplace =True)
gdp.index = pd.to_datetime(gdp.index)

# Resampling
gdp =gdp.resample('M').ffill()

# # Set the day of the index to 1
gdp.index = gdp.index.map(lambda x: x.replace(day=1))
gdp = gdp["2003-01-01":"2024-01-01"]

gdp.to_csv('/content/Cleaned data/gdp.csv')

"""Homeowner Rates : Includes record of population percentage owning a house"""

homeowner_rate = pd.read_csv('/RSAHORUSQ156S.csv')
homeowner_rate.head()

# Setting DATE as index, column renaming, setting DATE as index, filtering data from "1987-01-01":"2023-07-01"

homeowner_rate.set_index('DATE', inplace =True)
homeowner_rate.index = pd.to_datetime(homeowner_rate.index)
homeowner_rate.rename(columns= {'RSAHORUSQ156S': 'homeowner_rate'}, inplace =True)

# Resampling
homeowner_rate = homeowner_rate.resample('M').ffill()

# # Set the day of the index to 1
homeowner_rate.index = homeowner_rate.index.map(lambda x: x.replace(day=1))
homeowner_rate = homeowner_rate["2003-01-01":"2023-07-01"]

homeowner_rate.to_csv('/content/Cleaned data/homeowner_rate.csv')

"""Sales Prices for Homes"""

sales_rate = pd.read_csv('/MSPUS.csv')
sales_rate.head()

# Setting DATE as index, column renaming, setting DATE as index, filtering data from "1987-01-01":"2023-07-01"

sales_rate.set_index('DATE', inplace =True)
sales_rate.index = pd.to_datetime(sales_rate.index)

# Resampling
sales_rate = sales_rate.resample('M').ffill()

# # Set the day of the index to 1
sales_rate.index = sales_rate.index.map(lambda x: x.replace(day=1))
sales_rate = sales_rate["2003-01-01":"2023-07-01"]

sales_rate.to_csv('/content/Cleaned data/sales_rate.csv')

"""Load the Filtered Data"""

directory_name = "cleaned_data"

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

path = '/content/Cleaned data'

csv_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

dfs = [pd.read_csv(f) for f in csv_files]

# Merging the dataframes on the 'DATE' column
df_final = pd.concat(dfs, ignore_index=False).groupby('DATE').sum()

df_final.head()

df_final.info()

df_final.describe()

"""Exploratory Data Analysis : Visualization and Insights"""

#Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Understanding distribution of every factor over the years
plt.figure(figsize=(12, 6))
for col in df_final.columns.tolist():
    plt.figure(figsize=(6, 4))
    sns.displot(data=df_final, x=col, kde =True)
    plt.xlabel(f"{col}")
    plt.ylabel("DATE")
    plt.title(f'Distribution Plot for {col}')
    plt.show()



"""The main Factors which contribute to House Pricing are -


1.  Population over time
2. Shiller Index
3. Employment Over Time



"""

# How does income and population have been impacted over years ?
plt.figure(figsize=(10,6))
sns.set(style='whitegrid')

sns.scatterplot(y='population_df', x='income', data = df_final ,color ='orange')
plt.title('Income by population')
plt.ylabel('population')
plt.xlabel('income')
plt.show()

plt.figure(figsize=(10,6))
sns.set(style='whitegrid')

sns.regplot(x='MSPUS', y='CSUSHPINSA', data = df_final ,color ='green')
plt.title('Shiller Index and Sales Prices ')
plt.ylabel('Sales Price')
plt.xlabel('Shiller Index')
plt.show()

plt.figure(figsize=(10,6))
sns.set(style='whitegrid')

sns.scatterplot(y='population_df', x='homeowner_rate', data = df_final ,color ='orange')
plt.title('Homeowner Ship Rate  by population')
plt.ylabel('population')
plt.xlabel('homeowner_rate')
plt.show()

# Line plot to show trends over time
plt.figure(figsize=(14, 8))

sns.lineplot(data=df_final, x=df_final.index , y='MSPUS', label='House Prices', color='orange')
sns.lineplot(data=df_final, x=df_final.index, y='personal_saving', label='Interest Rate', color='red')
sns.lineplot(data=df_final, x=df_final.index, y='income', label='Income', color='blue')

plt.title('Trends of House Prices, Interest Rates, and Income Over Time')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.show()

# import the necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


# Define the data
X = df_final.drop('CSUSHPINSA', axis=1)
# You were predicting all the columns in your dataframe.
# This line changes it to just predict the 'CSUSHPINSA' column
y = df_final['CSUSHPINSA']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Feature importance
importance = model.coef_ # This should now be a 1D array
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importance})
print(feature_importance)

"""Key Highlights from this model -


1.   Mortgage Rate: 19.987

This coefficient is the largest positive, indicating that an increase in mortgage rates strongly correlates with an increase in the housing index price. This may seem counterintuitive since higher mortgage rates typically reduce housing affordability.
2.   Personal Saving Rate: -2.787

A negative coefficient indicates that an increase in the personal saving rate is associated with a decrease in housing index prices. This makes sense as higher savings rates could mean less spending on housing.

3. Unemployment Rate: 0.963

A positive coefficient suggests that higher unemployment rates are associated with higher housing index prices.

4. Also , similar for Income too , it is positivitve but small suggesting that higher incomes contributes to higher house index.

"""

# Trying other models - Decision Tree
# importing required libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import plot_tree

# Initialize and train the model
tree_model = DecisionTreeRegressor(max_depth=5, random_state=42)  # max_depth can be tuned
tree_model.fit(X_train, y_train)

# Make predictions
y_pred = tree_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)



# Plot the tree
plt.figure(figsize=(20,10))
plot_tree(tree_model, feature_names=X.columns, filled=True, rounded=True)

# K-nearest model
from sklearn.neighbors import KNeighborsRegressor

# Initialize the KNeighborsRegressor model
knn = KNeighborsRegressor(n_neighbors=1)

# Fit the model
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

nearest_neighbor_indices = knn.kneighbors(X_test, return_distance=False)

# Access the corresponding 'MSPUS' values from df_final
predicted_mspus_values = df_final['MSPUS'].iloc[nearest_neighbor_indices.flatten()]

# Print the predictions
print("Predicted MSPUS values:", predicted_mspus_values)

y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

# find all the keys from the dataset
print("df_final.keys(): \n{}".format(df_final.keys()))
#shape of data
print("Shape of final data: {}".format(df_final.shape))

!pip install mglearn

import mglearn
mglearn.plots.plot_knn_classification(n_neighbors=3)