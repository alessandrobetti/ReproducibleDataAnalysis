# PART 1: Loading and visualizing data
# data from: https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k

# click on Download -> csv -> Right click and I get the link address
fremont_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

import os
from urllib.request import urlretrieve
import pandas as pd

def get_fremont_data(filename= 'Fremont.csv', url= fremont_URL, force_download= False):
	""" Download and cache the Fremont data
	Parameters
	--------------
	filename : string (optional)
				location to save the data
	url: string (optional)
			web location of the data
	force_download: boolean (optional)
					if True, force redownload of the data
	Returns
	--------------
	data: Pandas.Dataframe
			The Fremont bridge data
	"""
	if (force_download or not os.path.exists(filename)):
		urlretrieve(url, filename)
	# read dataframe from URL link address and use the 'Date' column as the index column itself
    # (data is now index by the Date itself, not the row number)
    # parse_dates= True set the column 'Date' to dates, rather than strings
	data= pd.read_csv(filename, index_col= 'Date', parse_dates= True)
	data.columns= ['West', 'East']
	# add a column to the dataframe (there is an offset between west and east, so summing the flux we can see
	# that the sum is almost constant)
	data['Total']= data['West'] + data['East']
	return data