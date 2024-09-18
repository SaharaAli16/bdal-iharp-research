import xarray as xr
import numpy as np

path = "/umbc/rs/iharp/common/causality/data/greenland/racmo_data/*.nc"
snow_data = xr.open_mfdataset(path, concat_dim = "time",chunks=None, combine='nested', drop_variables =['time','x','y','LAT','LON'])
snow_np = np.array(snow_data.to_array())
print(snow_np.shape)
snow = snow_np.reshape(snow_np.shape[1], 2700, 1496)
print(snow.shape)
np.save("/umbc/rs/iharp/common/causality/data/greenland/racmo_data/RACMO_snowmelt_daily_AMJ_1979_2021.npy",snow)
