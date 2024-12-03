import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import numpy as np

# Load the dataset
# Assume the dataset has columns: 'latitude', 'longitude', 'time', 'weather', 'road_condition', 'severity'
data = pd.read_csv('traffic_accidents.csv')

# Convert 'time' to datetime format and extract hour of the day
data['time'] = pd.to_datetime(data['time'])
data['hour'] = data['time'].dt.hour

# Drop rows with missing values in critical columns
data.dropna(subset=['latitude', 'longitude', 'weather', 'road_condition', 'severity'], inplace=True)
plt.figure(figsize=(12, 6))
sns.histplot(data['hour'], bins=24, kde=True)
plt.title('Accidents by Time of Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='weather', hue='road_condition')
plt.title('Accidents by Weather and Road Condition')
plt.xlabel('Weather')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.legend(title='Road Condition')
plt.show()
plt.figure(figsize=(12, 6))
sns.violinplot(data=data, x='weather', y='severity', hue='road_condition', split=True)
plt.title('Severity of Accidents by Weather and Road Condition')
plt.xlabel('Weather')
plt.ylabel('Severity')
plt.xticks(rotation=45)
plt.legend(title='Road Condition')
plt.show()
# Create a base map centered on the average location of the accidents
accident_map = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=10)

# Prepare data for the heatmap
heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]

# Add heatmap layer to the map
HeatMap(heat_data).add_to(accident_map)

# Save the map to an HTML file or display it inline if using a Jupyter notebook
accident_map.save("accident_hotspot_map.html")
accident_map
# Encode categorical variables
data_encoded = pd.get_dummies(data[['hour', 'severity', 'road_condition', 'weather']], drop_first=True)

# Compute correlation matrix
correlation_matrix = data_encoded.corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Accident Factors')
plt.show()
