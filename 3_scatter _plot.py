# Importujemy funkcję `figure` i `show` z modułu `bokeh.plotting`.
# `figure` służy do tworzenia wykresów, a `show` do ich wyświetlania w przeglądarce.
from bokeh.plotting import figure, show
from data_1 import x, y

# Tworzymy obiekt wykresu za pomocą funkcji `figure`.
# Podajemy tytuł wykresu oraz etykiety osi X i Y.
p = figure(title = "Prosty wykres typu scatter",
           x_axis_label = "x",
           y_axis_label='y')
# Dodajemy dane do wykresu w formie punktów (`scatter` to wykres punktowy).
p.scatter(x, y,
          legend_label="Wizualizacja danych",
          line_width=2,
          color = "red",
          size = 15)
# Wyświetlamy wykres w przeglądarce.
# Funkcja `show` renderuje i otwiera wykres w domyślnej przeglądarce użytkownika.
show(p)

