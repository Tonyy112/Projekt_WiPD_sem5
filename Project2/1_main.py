# Importujemy wymagane moduły
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Greys10
import pandas as pd

# Wczytujemy dane z pliku CSV do obiektu DataFrame z Pandas.
# Parametr `on_bad_lines='skip'` pozwala pominąć błędne wiersze w pliku.
df = pd.read_csv("fotballers.csv", on_bad_lines='skip')

# name = df["Name"]
# earnings = df["Earnigns"]
# Tworzymy obiekt ColumnDataSource, który pozwala Bokeh pracować z danymi w formacie tabelarycznym.
# `ColumnDataSource` jest używany jako źródło danych dla wykresu.
source = ColumnDataSource(df)
# Tworzymy listę nazw piłkarzy (kolumna "Name"), która będzie używana jako oś Y na wykresie.
name_list = source.data["Name"].tolist()

# Ustawiamy plik wyjściowy HTML, w którym zapisany będzie wykres.
output_file("index.html")

# Tworzymy obiekt wykresu za pomocą `figure`.
p = figure(y_range = name_list,
    title="Zarobki TOP10 piłkarzy według Forbes",
    x_axis_label = "Earnings",
    tools="reset, pan, box_select, zoom_in, zoom_out, save")

# Ustawiamy rozmiar wykresu.
p.width = 1280
p.height = 720

# Dodajemy poziome paski (horyzontalny wykres słupkowy).
p.hbar(y = "Name",
       right = "Earnings",
       left=0,
       height = 0.4,
       fill_color = factor_cmap("Name", palette = Greys10, factors=name_list),
       fill_alpha = 2,
       source = source)

# Tworzymy narzędzie HoverTool, które wyświetla szczegóły po najechaniu myszką na pasek.
hover = HoverTool()

hover.tooltips = """
<div>
    <h3>@Name</h3>
    <div><strong>Age: </strong>@Age</div>
    <div><strong>Club: </strong>@Club</div>
    <div><img src="@Photo" alt="" width="200"</div>
</div>
"""

# Dodajemy narzędzie hover do wykresu.
p.add_tools(hover)

# Wyświetlamy gotowy wykres w przeglądarce.
show(p)