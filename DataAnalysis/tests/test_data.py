import pandas as pd
from DataAnalysis.data import get_fremont_data

def test_fremont_data():
    # read data()
    data= get_fremont_data()
    # we want to make sure that columns are what we expect
    print(all(data.columns== ['West', 'East', 'Total']))
    print(isinstance(data.index, pd.DatetimeIndex))
	
	