import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Sample data (latitude and longitude coordinates)
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698]
}

# Creating a pandas DataFrame from the data
df = pd.DataFrame(data)

# Create a map centered at a location
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Center of the United States

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(m)

# Add markers to the MarkerCluster object based on data points
for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['City']).add_to(marker_cluster)

# Save the map as an HTML file
m.save('clustered_map.html')
