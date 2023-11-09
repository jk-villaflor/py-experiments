import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Create a new figure
plt.figure(figsize=(8, 6))

# Define the map projection (e.g., Plate Carrée projection)
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map
ax.set_extent([-125, -66.5, 20, 50], crs=ccrs.PlateCarree())

# Add coastlines
ax.coastlines()

# Plot a point (e.g., New York City)
plt.plot(-74, 40.7, 'ro', markersize=8, transform=ccrs.PlateCarree())

# Set a title
plt.title('Map Plot Example')

# Show the plot
plt.show()

