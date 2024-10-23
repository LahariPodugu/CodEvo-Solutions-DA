import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
file_path = r'C://Users//lahar//OneDrive//Documents//Task-4.csv'  # Updated for Task-4 file
data = pd.read_csv(file_path)

# Preview the dataset
print("Preview of the dataset:")
print(data.head())

# Check data types and missing values
print("\nDataset information:")
print(data.info())

print("\nSummary statistics:")
print(data.describe())

# Handle missing values (drop or fill them)
print("\nMissing values in each column:")
print(data.isnull().sum())

# Drop rows with missing values or fill them accordingly
data = data.dropna()  # Drop rows with any missing values

# Alternatively, you can fill missing values (example for a specific column)
# data['column_name'].fillna('Unknown', inplace=True)

# Extract time-related information (if applicable)
data['Hour'] = pd.to_numeric(data['A_TOD'], errors='coerce')

# Preview the updated data
print("\nUpdated dataset with Hour column:")
print(data[['A_TOD', 'Hour']].head())

# 1. Trend Analysis: Group by year and count accidents each year
yearly_trend = data.groupby('YEAR').size()

# Plot yearly trend of accidents
plt.figure(figsize=(10, 5))
yearly_trend.plot(kind='line')
plt.title('Yearly Traffic Accidents')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()

# 2. Weather Condition Analysis: Countplot of accidents by weather conditions
plt.figure(figsize=(10, 5))
sns.countplot(x='A_WEATHER', data=data)
plt.title('Accidents by Weather Conditions')
plt.xlabel('Weather Condition')
plt.ylabel('Accident Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Correlation Matrix Analysis: Explore relationships between numeric variables
corr_matrix = data.corr()

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Accident Data')
plt.show()

# 4. Geographic Analysis: Choropleth map of accidents by state
fig = px.choropleth(
    data,
    locations='STATE',
    locationmode='USA-states',  # Use state codes (USA)
    color='FATALS',  # Use 'FATALS' to indicate accident severity
    scope='usa',  # Focus on USA map
    title='Traffic Accidents by State'
)
fig.show()

