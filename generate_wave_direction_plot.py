import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import numpy as np
import os

# Load the dataset
file = "C:/Users/Nicol/Desktop/Software/ENSO/data/wave_direction_data.nc"
data = xr.open_dataset(file)

# Define output directories
output_dir_1997_1998 = "data/mwd_plots_1997_1998"
output_dir_2015_2016 = "data/mwd_plots_2015_2016"
os.makedirs(output_dir_1997_1998, exist_ok=True)
os.makedirs(output_dir_2015_2016, exist_ok=True)

# Define time periods
time_periods = {
    "1997_1998": ("1997-01-01", "1998-12-31"),
    "2015_2016": ("2015-01-01", "2016-12-31")
}

# Generate plots for each time period
for period, (start_date, end_date) in time_periods.items():
    output_dir = output_dir_1997_1998 if period == "1997_1998" else output_dir_2015_2016
    data_period = data.sel(valid_time=slice(start_date, end_date))
    
    for i, time in enumerate(data_period['valid_time'].values):
        data_for_time = data_period.sel(valid_time=time)
        
        # Extract latitude, longitude, and wave direction
        lats = data_for_time['latitude'].values
        lons = data_for_time['longitude'].values
        wave_dir = data_for_time['mwd'].values

        # Reduce the number of arrows by slicing the arrays
        step = 5  # Adjust this value to change the density of arrows
        lats = lats[::step]
        lons = lons[::step]
        wave_dir = wave_dir[::step, ::step]

        # Convert wave direction to u and v components for quiver plot
        u = np.cos(np.deg2rad(wave_dir))
        v = np.sin(np.deg2rad(wave_dir))

        # Create the plot
        plt.figure(figsize=(12, 6))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.coastlines()
        ax.set_xticks(range(-180, 181, 60), crs=ccrs.PlateCarree())
        ax.set_yticks(range(-90, 91, 30), crs=ccrs.PlateCarree())
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')

        # Plot the wave direction using quiver
        plt.quiver(lons, lats, u, v, transform=ccrs.PlateCarree())
        plt.title(f'Mean Wave Direction on {str(time)[:7]}')  
        plt.savefig(os.path.join(output_dir, f'wave_direction_{i:04d}.png'))
        plt.close()