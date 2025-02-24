import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import os

file = "C:/Users/nijordia/Desktop/Software/ENSO/data/sst_historical_events.nc"
data = xr.open_dataset(file)

# Define output directories
output_dir_1997_1998 = "data/sst_plots_1997_1998"
output_dir_2015_2016 = "data/sst_plots_2015_2016"
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
        plt.figure(figsize=(10, 5))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.coastlines()
        ax.set_xticks(range(-180, -50, 60), crs=ccrs.PlateCarree())
        ax.set_xlim(-180, -50)  
        ax.set_yticks(range(-90, 90, 30), crs=ccrs.PlateCarree())
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        data_for_time['sst'].plot(ax=ax, vmin=270, vmax=315,cbar_kwargs={'shrink': 0.8, 'aspect': 30})  # Set colorbar limits
        plt.title(f'SST for {str(time)[:7]}')  
        plt.savefig(os.path.join(output_dir, f'sst_{i:04d}.png'))
        plt.close()