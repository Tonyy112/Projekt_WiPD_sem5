# Importujemy funkcje `figure` i `show` z modułu `bokeh.plotting`.
# `figure` służy do tworzenia wykresów, a `show` do ich wyświetlania w przeglądarce.
from bokeh.plotting import figure, show
from data_1 import x, y

# Importujemy funkcje `figure` i `show` z modułu `bokeh.plotting`.
# `figure` służy do tworzenia wykresów, a `show` do ich wyświetlania w przeglądarce.
p = figure(title = 'Prosty Bar Plot',
           x_axis_label="x",
           y_axis_label = "y")
# Dodajemy do wykresu pionowe słupki za pomocą funkcji `vbar`.
# Argumenty definiują parametry wizualne i dane dla słupków.
p.vbar(x=x,
       top = y,
       width=0.5,
       bottom = 0,
       color="purple")

# Wyświetlamy wykres w przeglądarce.
# Funkcja `show` generuje wizualizację i otwiera ją w domyślnej przeglądarce użytkownika.
show(p)


