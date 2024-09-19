# Get weather data

# TODO: figure out what is going on here with my conda/pip install conflicts

from meteostat import Point, Daily
from datetime import datetime
import matplotlib.pyplot as plt

# Set time period
start = datetime(2014, 1, 1)
end = datetime(2019, 12, 31)

# Set location for Bristol
lat = 51.454514
lon = -2.587910
alt = 36 # feet

# Create Point for Bristol
bristol = Point(lat, lon, alt)

# Get daily data for 2014-2019 in Bristol
data = Daily(bristol, start, end)
data = data.fetch()
data.to_csv('data/raw/meteostat_bristol.csv')

# NB: this location didn't have precip data, so I'm going to try a different location-

# Lyneham has precipitation data-
data = Daily('03740', start, end)
data = data.fetch()
data.head()

data.to_csv('data/raw/meteostat_lyneham.csv')
