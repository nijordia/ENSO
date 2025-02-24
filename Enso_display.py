import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs

file = "C:/Users/nijordia/Desktop/Software/ENSO/data/sst_historical_events.nc"

data = xr.open_dataset(file)

#print(data['valid_time'].values)


test_date = '1997-12-28'
data_for_test_date = data.sel(valid_time=test_date)

plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.set_xticks(range(-180, -50, 60), crs=ccrs.PlateCarree())
ax.set_xlim(-180, -50)  # Crop longitude to remove the white area

ax.set_yticks(range(-90, 90, 30), crs=ccrs.PlateCarree())
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

data_for_test_date['sst'].plot()

plt.title(f'SST for {test_date}')

plt.show()
