import pandas as pd
import matplotlib.pyplot as plt

# Load the data
tb_data = pd.read_csv('tb_data.csv')
hiv_data = pd.read_csv('hiv_data.csv')

# Merge the datasets on a common key, e.g., state and year
data = pd.merge(tb_data, hiv_data, on=['state', 'year'])

# Print the first few rows and data types to inspect the data
print("First few rows of the merged data:")
print(data.head())
print("\nData types of the columns:")
print(data.dtypes)

# Ensure that only numeric columns are used for correlation
numeric_data = data.select_dtypes(include=[float, int])

# Handle missing data: fill or drop
# Option 1: Fill missing values with 0 (or another value)
# numeric_data = numeric_data.fillna(0)

# Option 2: Drop rows with missing values
numeric_data = numeric_data.dropna()

# Descriptive statistics
print("\nDescriptive Statistics:")
print(numeric_data.describe())

# Correlation matrix
correlation_matrix = numeric_data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(numeric_data['tb_cases'], numeric_data['hiv_cases'])
plt.xlabel('TB Cases')
plt.ylabel('HIV Cases')
plt.title('Scatter plot of TB Cases vs HIV Cases')
plt.show()
