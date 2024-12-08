import numpy as np
# Importujemy narzędzia do tworzenia wykresów i interfejsu użytkownika z Bokeh.
from bokeh.plotting import figure, show, curdoc  # `figure` do wykresów, `show` do wyświetlenia, `curdoc` do zarządzania dokumentem.
from bokeh.models import Div, Spinner, TextInput  # `Div` do wyświetlania tekstu, `Spinner` do wartości liczbowych, `TextInput` do wpisywania tekstu.
from bokeh.layouts import layout  # `layout` do organizacji elementów interfejsu użytkownika.
from data_1 import x, y  # Importujemy dane `x` i `y` do wykresu.

# Tworzymy obiekt wykresu.
p = figure()
# Dodajemy punkty do wykresu za pomocą `scatter`. Obiekt `points` przechowuje glyph dla tych punktów.
points = p.scatter(x, y)

# Tworzymy element Div (HTML) z tekstem wyświetlanym nad spinnerem.
div = Div(text="<p>Wybierz rozmiar </p>")

# Tworzymy kontrolkę Spinner:
# - `title` ustawia tytuł kontrolki.
# - `low` i `high` określają zakres wartości.
# - `step` definiuje krok zmian wartości.
# - `value` ustawia początkową wartość na rozmiar punktów (`points.glyph.size`).
# - `width` określa szerokość kontrolki.
spinner = Spinner(title = "Rozmiar ikon", low = 1, high = 10, step = 1, value=points.glyph.size, width = 200)

# Łączymy wartość spinnera z rozmiarem punktów (`size` glyph).
# `js_link` tworzy połączenie JavaScript między kontrolką a właściwością glyph.
spinner.js_link("value", points.glyph, "size")

# Tworzymy kontrolkę TextInput:
# - `value` ustawia początkowy tekst jako bieżący kolor wypełnienia punktów.
# - `width` określa szerokość kontrolki.
text_input = TextInput(value = points.glyph.fill_color, width = 200)
# Łączymy wartość tekstową kontrolki z kolorem wypełnienia punktów (`fill_color` glyph).
text_input.js_link("value", points.glyph, "fill_color")

# Tworzymy układ zawierający kontrolki i wykres:
# - Pierwszy wiersz zawiera Div i Spinner.
# - Drugi wiersz zawiera TextInput.
# - Trzeci wiersz zawiera wykres.
layout = layout([[div, spinner], [text_input], [p]])

# Wyświetlamy układ w przeglądarce.
show(layout)