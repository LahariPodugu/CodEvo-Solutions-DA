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
import pandas as pd
import matplotlib.pyplot as plt

# Example data (replace this with your actual DataFrame)
data = pd.DataFrame({
    'YEAR': [2018, 2019, 2020, 2021, 2022],  # Example years
    'ACCIDENTS': [100, 150, 120, 170, 200]   # Example accident counts
})

# Group by year and count accidents each year
yearly_trend = data.groupby('YEAR').size()

# Plot yearly trend of accidents
plt.figure(figsize=(10, 5))
yearly_trend.plot(kind='line', marker='o')  # Added marker for clarity
plt.title('Yearly Traffic Accidents')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()


# 2. Weather Condition Analysis: Countplot of accidents by weather conditions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset (adjust the path if needed)
data = pd.read_csv(r'C://Users//lahar//OneDrive//Documents//Task-4.csv' )

# Clean column names (optional, to remove spaces)
data.columns = data.columns.str.strip()

# Drop rows with missing weather data
data = data.dropna(subset=['A_WEATHER'])

# Plot the countplot with 'A_WEATHER' assigned to 'hue'
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='A_WEATHER', hue='A_WEATHER', legend=False, palette='coolwarm')

# Add labels and title
plt.title('Accidents by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.show()



# 3. Correlation Matrix Analysis: Explore relationships between numeric variables
corr_matrix = data.corr()

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Accident Data')
plt.show()

# 4. Geographic Analysis: Choropleth map of accidents by state
import plotly.express as px
import pandas as pd

# Example data (replace this with your actual DataFrame)
data = pd.DataFrame({
    'STATE': ['CA', 'TX', 'FL'],  # Example state codes
    'FATALS': [500, 700, 300]
})

# Choropleth map visualization
fig = px.choropleth(
    data,
    locations='STATE',
    locationmode='USA-states',
    color='FATALS',
    scope='usa',
    title='Traffic Accidents by State'
)

# Ensure it displays in your browser
fig.show()


