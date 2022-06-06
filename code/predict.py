# Import necessary libraries

import math
import pickle
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy import distance

# Apartment info

address = "Sunnanväg 10H, Lund"
size = 103
isBalcony = 0
isElevator = 0
floor_number = 1
total_floor = 1
BuildYear = 1965
month = 12


def main():

    # Location
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    lat = location.latitude
    lon = location.longitude

    # Distance
    df = pd.read_csv("apartment_df_latlon.csv")
    ref = (df["Lat"][1971], df["Lon"][1971])
    coordi = (lat, lon)
    dist = distance.distance(coordi, ref).km

    # X, Y coordinates
    radi_Lat = lat * math.pi / 180
    radi_Lon = lon * math.pi / 180

    R = 6371
    X_temp = R * math.cos(radi_Lat) * math.cos(radi_Lat)
    Y_temp = R * math.cos(radi_Lon) * math.sin(radi_Lon)

    # Normalize coordinates
    X = X_temp
    Y = -Y_temp + 4.798804314864128

    # Floor ratio
    ratio = floor_number / total_floor

    # Area transform
    area = np.log10(size)

    # Input

    d = {
        "area (m²)": area,
        "Balcony": isBalcony,
        "Elevator": isElevator,
        "Build year": BuildYear,
        "Month": month,
        "distance": dist,
        "X": X,
        "Y": Y,
        "floorRatio": ratio,
    }

    apart_info = pd.DataFrame([d])

    # Load trained rf model
    rf_load = pickle.load(open("hemnet_rf_pre.sav", "rb"))

    # Output
    result = rf_load.predict(apart_info)
    price = (np.power(10, result) * 1000).astype(int)
    print("The estimating sold price of your apartment is: " + str(int(price)) + " SEK")


if __name__ == "__main__":
    main()
