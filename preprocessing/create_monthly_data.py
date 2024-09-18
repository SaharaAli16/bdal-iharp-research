import numpy as np

data = np.load("/umbc/rs/iharp/common/causality/data/greenland/racmo_data/RACMO_snowmelt_daily_JJA_1979_2021.npy")
months = [30, 31, 31]
month_lst = []

# Create a full list of days per month for each month in 1979-2021
for i in range(1979, 2022):
    month_lst.append(months)
month_lst = np.array(month_lst).reshape(-1)

# Iterate through each variable add to the final array.
final_arr = np.zeros((len(month_lst),2700, 1496))
var_idx = 0
for key in range(1):
	day_sum = 0
	var = data[:,:,:]
	var_arr = np.zeros((len(month_lst),2700, 1496))
	#print(var.shape)
	#print(var_arr.shape)
	for i in range(len(month_lst)): 
		var_arr[i,:,:] = np.nanmean(var[day_sum:(day_sum + month_lst[i])], axis=0)
		if i % 3 == 0:
			print(day_sum)
		day_sum = day_sum + month_lst[i]
	day_sum = 0
	final_arr[:,:,:] = var_arr # Add variable monthly means to final array.
	var_idx += 1

# Save final data array with shape (months, lat, lon) to a numpy array.
print(final_arr.shape)
monthly_data = np.save("/umbc/rs/iharp/common/causality/data/greenland/racmo_data/RACMO_snowmelt_monthly_JJA_1979_2021.npy",final_arr)
