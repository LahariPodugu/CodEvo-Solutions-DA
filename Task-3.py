import pandas as pd

# Load the datasets
hour_data = pd.read_csv("C:\\Users\\lahar\\Downloads\\hour.csv")
day_data = pd.read_csv("C:\\Users\\lahar\\Downloads\\day.csv")

# Preview the data
print(hour_data.head())
print(day_data.head())


# Check for missing values
print(hour_data.isnull().sum())
print(day_data.isnull().sum())

# Convert 'dteday' to datetime format
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])


# Group data by hour and calculate the average ridership
hourly_ridership = hour_data.groupby('hr')['cnt'].mean()

# Plot hourly ridership
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
hourly_ridership.plot(kind='line', color='blue')
plt.title('Average Bike Rentals by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Rentals')
plt.show()


# Group by weekday to identify daily trends
weekday_ridership = day_data.groupby('weekday')['cnt'].mean()

plt.figure(figsize=(10, 6))
weekday_ridership.plot(kind='bar', color='green')
plt.title('Average Rentals by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Average Rentals')
plt.show()

# Monthly Analysis
monthly_ridership = day_data.groupby('mnth')['cnt'].mean()
plt.figure(figsize=(10, 6))
monthly_ridership.plot(kind='bar', color='orange')
plt.title('Average Rentals by Month')
plt.xlabel('Month')
plt.ylabel('Average Rentals')
plt.show()


import seaborn as sns

# Create a boxplot for rentals across different weather conditions
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=hour_data)
plt.title('Bike Rentals Across Different Weather Conditions')
plt.xlabel('Weather Situation (1=Clear, 2=Mist, 3=Light Snow/Rain)')
plt.ylabel('Count of Rentals')
plt.show()

# Correlation between temperature and ridership
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=hour_data, color='red')
plt.title('Temperature vs Bike Rentals')
plt.xlabel('Temperature')
plt.ylabel('Count of Rentals')
plt.show()


# Analyze casual and registered users over different time periods
hourly_users = hour_data.groupby('hr')[['casual', 'registered']].mean()

plt.figure(figsize=(10, 6))
hourly_users.plot(kind='line')
plt.title('Casual vs Registered Users by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Rentals')
plt.show()


# Save the cleaned or grouped data to CSV for Tableau or Power BI
hourly_ridership.to_csv('hourly_ridership.csv')
