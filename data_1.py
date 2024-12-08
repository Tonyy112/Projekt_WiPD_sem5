import numpy as np
from bokeh.plotting import figure, show
from random import randint

#Przygotowywanie danych
x = np.arange(0,50,1)
y = []
y_1 = []
y_2 = []
y_3 = []

for _ in range(len(x)):
    y.append(randint(0,50))
    y_1.append(randint(0,50))
    y_2.append(randint(0,50))
    y_3.append(randint(0,50))


fuel_type = ["Gasline", "Diesel", "PHEV", "MHEV", "EV"]
years = ["2020", "2021", "2022", "2023", "2024"]

car_data_by_years = {'fuel_type': fuel_type,
            '2020': [randint(1500,3000) for _ in range(len(fuel_type))],
            '2021': [randint(1500,3000) for _ in range(len(fuel_type))],
            '2022': [randint(1500,3000) for _ in range(len(fuel_type))],
            '2023': [randint(1500,3000) for _ in range(len(fuel_type))],
            '2024': [randint(1500,3000) for _ in range(len(fuel_type))]}

car_data_by_fueltype = {'years': years,
                        'Gasoline': [randint(1500,3000) for _ in range(len(years))],
                        'Diesel': [randint(1500,3000) for _ in range(len(years))],
                        'PHEV': [randint(1500,3000) for _ in range(len(years))],
                        'MHEV': [randint(1500,3000) for _ in range(len(years))],
                        'EV': [randint(1500,3000) for _ in range(len(years))]}