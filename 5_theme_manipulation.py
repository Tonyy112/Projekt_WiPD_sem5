# Importujemy funkcje `figure`, `show` i `curdoc` z modułu `bokeh.plotting`.
# - `figure` służy do tworzenia wykresów.
# - `show` pozwala na wyświetlenie wykresu w przeglądarce.
# - `curdoc` pozwala na dostęp do obiektu dokumentu Bokeh, umożliwiając m.in. ustawienie motywu graficznego.
from data_1 import x, y
from bokeh.plotting import figure, show, curdoc

# Ustawienie motywu graficznego wykresu.
# `curdoc().theme` pozwala określić motyw, który wpływa na wygląd tła, siatki, etykiet i innych elementów.
# Ustawaienie koloru tła wykresu na night_sky
curdoc().theme = "night_sky"
# carbon
# dark_minimal etc.
# Możliwe alternatywy: "carbon", "dark_minimal", itp., które zmieniają estetykę wykresu.

# Tworzymy obiekt wykresu za pomocą funkcji `figure`.
# Podajemy tytuł wykresu oraz etykiety osi.
p = figure(title="Prosty wykres typu scatter", x_axis_label = "x", y_axis_label="y")

# Ustawienie rozmiarów wykresu
p.width = 1280
p.height = 720

# Dodajemy dane na wykres w formie punktów za pomocą metody `scatter`.
p.scatter(x,y, legend_label="Wizualizacja danych", color="yellow", size=12)

# Wyświetlamy wykres w przeglądarce.
show(p)