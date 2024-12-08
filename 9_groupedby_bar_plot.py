# Importujemy wymagane biblioteki.
import numpy as np  # Do przetwarzania danych numerycznych.
import pandas as pd  # Do manipulacji danymi w formie tabelarycznej.
from bokeh.plotting import figure, show  # `figure` do tworzenia wykresów, `show` do wyświetlenia.
from data_1 import car_data_by_years, fuel_type, years  # Importujemy dane z modułu `data_1`.
from bokeh.palettes import Bright5  # Predefiniowana paleta kolorów z Bokeh.

# Tworzymy obiekt wykresu z odpowiednimi ustawieniami osi i tytułem.
p = figure(x_range=fuel_type, # Określamy kategorie osi X jako `fuel_type` (np. rodzaje paliwa).
           title = "Przykładowy zgrupowany wykres słupkowy", # Tytuł wykresu.
           x_axis_label = "Rodzaj paliwa", # Etykieta osi X.
           y_axis_label = "Ilość", # Etykieta osi Y.
           tools="hover", # Aktywujemy narzędzie hover do wyświetlania informacji po najechaniu myszką.
           tooltips="$name @fuel_type: @$name") # Ustawiamy szablon podpowiedz.

# Dostosowujemy rozmiar wykresu
p.width = 1280
p.height = 720
p.legend.location = "top_right"
p.legend.orientation = "horizontal"

# Dodajemy wykres słupkowy zgrupowany za pomocą metody `vbar_stack`.
p.vbar_stack(years,
             x='fuel_type',
             source=car_data_by_years,
             width = 0.5,
             legend_label=years,
             color = Bright5)

# Wyświetlamy gotowy wykres w przeglądarce.
show(p)

