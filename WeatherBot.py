#!/usr/bin/env python3
import requests
import json 
import Weather


LAT = 34.707
LON = -86.6277

class WeatherBot:
    def __init__(self, lat=LAT, lon=LON):
        self.lat = lat
        self.lon = lon 
        self.dump = None
        self.weather = Weather()

    def _buildURL(self):
        return f"https://api.weather.gov/points/{self.lat},{self.lon}"

    def getData(self):
        '''
        Performs a GET request to the server
        Params: None
        Returns: True if success, false if otherwise
        '''
        self.dump = requests.get(_buildURL).json()
        return self.dump.status_code == 200

    def getHourly(self):
        requests.get(self.dump['properties']['hourly'])

def main():
    pass

if __name__ == "__main__":
    main()
