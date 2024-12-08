from bokeh.plotting import figure, show
from data_1 import x, y

# Tworzenie nowego canvasu za pomocą funkcji figure
p = figure(title = "Prosty wykres liniowy",
           x_axis_label='x',
           y_axis_label='y')

# Dodajemy do canvasu linie, legendę oraz ustawiamy szerokość lini i jej kolor
p.line(x, y,
       legend_label = "Wykres liniowy",
       line_width = 2,
       color = "red")

# Komenda realizująca tworzenie pliku html i wyświetlenie grafu w oknie przeglądarki
show(p)
