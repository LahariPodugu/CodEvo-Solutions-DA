import pandas as pd
import pandas as pd

# Load data
file_path = r'C:\Users\lahar\Downloads\Task-5.xlsx'
data = pd.read_excel(file_path)

# Check structure and initial rows
print(data.info())
print(data.head())


# Load the Excel file
file_path = r'C:\Users\lahar\Downloads\Task-5.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows to understand the structure
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Fill missing values with 0 (if applicable)
data.fillna(0, inplace=True)

# Check data types
print(data.info())

# Group by Minor Heads to analyze total murders by reason
total_by_reason = data.groupby('Minor Heads')['During the current year upto the end of month under review'].sum()
print(total_by_reason)

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load your dataset
file_path = r'C:\Users\lahar\Downloads\Task-5.xlsx'
data = pd.read_excel(file_path)

# Select numeric columns for PCA
numeric_data = data.iloc[:, 4:]  # Assuming relevant numeric data starts from the 4th column

# Standardize the data (important for PCA)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Apply PCA to reduce to 2 dimensions
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Create a DataFrame with the PCA results
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])

# Add the crime category (Minor Heads) for labeling purposes
pca_df['Minor Heads'] = data['Minor Heads']
print(pca_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot with PCA components
plt.figure(figsize=(10, 6))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Minor Heads', palette='viridis', s=100)

# Add plot title and labels
plt.title('PCA of Crime Data (2D Projection)', fontsize=16)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(loc='best', bbox_to_anchor=(1, 1))  # Adjust legend placement
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = r'C:\Users\lahar\Downloads\Task-5.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows to ensure data is loaded correctly
print(data.head())

# Group data by 'Minor Heads' and sum up 'During the current year upto the end of month under review'
# Dropping any NaN values for PCA to work properly
data_grouped = data.groupby('Minor Heads').sum(numeric_only=True).dropna()

# Standardize the numerical data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_grouped)

# Basic summary statistics
print(data.describe())

print(data.columns)

if 'major_heads' in data.columns:
    major_crimes_summary = data.groupby('major_heads')['during_the_current_year_upto_the_end_of_month_under_review'].sum()
    print(major_crimes_summary)
else:
    print("The column 'major_heads' was not found in the data.")

# Group by 'Major Heads' to analyze overall trends in different crime categories
major_crimes_summary = data.groupby('Major Heads')['During the current year upto the end of month under review'].sum()
print(major_crimes_summary)

# Group by 'Minor Heads' to see the top reasons for crime
minor_crimes_summary = data.groupby('Minor Heads')['During the current year upto the end of month under review'].sum().nlargest(10)
print(minor_crimes_summary)

# Apply PCA
pca = PCA()
pca.fit(data_scaled)

# Get explained variance ratio for each principal component
explained_variance_ratio = pca.explained_variance_ratio_

# Create a DataFrame to store the explained variance
pca_df = pd.DataFrame({
    'Principal Component': [f'PC{i+1}' for i in range(len(explained_variance_ratio))],
    'Explained Variance Ratio': explained_variance_ratio
})

# Plot the explained variance ratio as a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Principal Component', y='Explained Variance Ratio', hue='Principal Component', data=pca_df, palette='Blues', legend=False)

# Customize the plot
plt.title('Explained Variance Ratio of Principal Components')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Group data and select top 10 categories
total_by_reason = data.groupby('Minor Heads')['During the current year upto the end of month under review'].sum()
top_10 = total_by_reason.sort_values(ascending=False).head(10)

# Plot the bar chart
plt.figure(figsize=(14, 7))  # Increase figure size
sns.barplot(x=top_10.index, y=top_10.values, hue=top_10.index, palette='Blues', legend=False)

# Rotate x-axis labels to avoid clutter
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Crime Reasons (Current Year)', fontsize=16)
plt.xlabel('Reason for Crime', fontsize=14)
plt.ylabel('Number of Cases', fontsize=14)
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Minor crimes summary plot
sns.barplot(x=minor_crimes_summary.index, y=minor_crimes_summary.values, hue=minor_crimes_summary.index, palette='Reds', dodge=False, legend=False)
plt.xticks(rotation=90)
plt.title('Total Minor Crimes by Category')
plt.show()

# Assuming that data has columns like "During the current month" and "During the previous month"
monthly_trends = data[['During the current month', 'During the previous month']].sum()

plt.figure(figsize=(8, 5))
monthly_trends.plot(kind='line', marker='o', color=['blue', 'orange'])
plt.title('Monthly Crime Trends')
plt.xlabel('Month')
plt.ylabel('Total Incidents')
plt.legend(['Current Month', 'Previous Month'])
plt.show()



