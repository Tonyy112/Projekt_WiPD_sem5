from bokeh.plotting import figure, show
import numpy as np

# Generowanie danych
x = np.arange(0, 10, 1)
y1 =  x ** 1
y2 =  x ** 2
y3 =  x ** 3

# Twrzymy nowy canvas z tytułem oraz podpisami poszczególnych osi
p = figure(title = "Przykładowy wykres liniowy", 
           x_axis_label = "X", 
           y_axis_label = "y")

# Dodajemy do canvasu linie, legendę oraz ustawiamy szerokość lini i jej kolor
p.line(x, y1, legend_label="Funkcja liniowa", line_width = 2, color="orange")
p.line(x, y2, legend_label="Funkcja kwadratowa", line_width = 2, color="blue")
p.line(x, y3, legend_label="Wielomian", line_width = 2, color="green")

show(p)

