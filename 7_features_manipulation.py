# Importujemy funkcje `figure` i `show` z modułu `bokeh.plotting`.
# - `figure` służy do tworzenia wykresów.
# - `show` pozwala na wyświetlenie wykresów w przeglądarce.
from bokeh.plotting import figure, show
from data_1 import x, y

# Tworzymy obiekt wykresu za pomocą funkcji `figure`.
# Ustawiamy tytuł wykresu oraz etykiety osi.
p = figure(title = "Prosty wykres typu scatter",
           x_axis_label = "x",
           y_axis_label='y')

# Dodajemy punkty do wykresu za pomocą metody `scatter`.
# Zmienna `my_plot` przechowuje obiekt wykresu punktowego (glyph renderer).
my_plot = p.scatter(x, y,
          legend_label="Wizualizacja danych",
          line_width=2,
          color = "red",
          fill_color = "blue",
          size = 15)

# Pobieramy obiekt `glyph` z `my_plot`, aby zmodyfikować jego właściwości.
glyph = my_plot.glyph
glyph.size = 25
glyph.fill_color = "orange"

# Wyświetlamy wykres w przeglądarce.
show(p)