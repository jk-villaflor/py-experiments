import folium
import pandas as pd

# Sample data (latitude and longitude coordinates)
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Manila'],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604 ,14.599512],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, 120.984222]
}

# Creating a pandas DataFrame from the data
df = pd.DataFrame(data)

# Create a map centered at a location
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Center of the United States

# Add markers to the map based on data points
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(m)

# Save the map as an HTML file
m.save('datapoints_map.html')

