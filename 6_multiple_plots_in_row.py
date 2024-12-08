# Importujemy funkcje `figure`, `show` i `curdoc` z `bokeh.plotting`.
# - `figure` służy do tworzenia wykresów.
# - `show` pozwala na wyświetlanie wykresów.
# - `curdoc` umożliwia modyfikację dokumentu Bokeh (np. ustawianie motywów).
# Importujemy funkcję `row` z `bokeh.layouts` do rozmieszczania wykresów w układzie poziomym.
import numpy as np
from bokeh.layouts import row
from bokeh.plotting import figure, show, curdoc

# Tworzymy dane dla osi X: liczby od 0 do 10 z krokiem 0.1.
# Obliczamy wartości funkcji trygonometrycznych dla danych `x`.
x = np.arange(0, 10, 0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = np.tan(x)

# Ustawiamy motyw wizualny wykresów na "dark_minimal" (ciemne tło, minimalistyczny styl).
curdoc().theme = "dark_minimal"

# Tworzymy pierwszy wykres za pomocą funkcji `figure`.
p1 = figure()
p1.line(x, y_1)

# Tworzymy drugi wykres.
p2 = figure()
p2.line(x, y_2)

# Tworzymy trzeci wykres.
p3 = figure()
p3.line(x, y_3)

# Układamy wszystkie trzy wykresy obok siebie w jednym wierszu.
# - `children=[p1, p2, p3]` określa wykresy do wyświetlenia.
# - `sizing_mode="scale_width"` dostosowuje rozmiar wykresów do szerokości okna przeglądarki.
show(row(children=[p1, p2, p3], sizing_mode="scale_width"))
