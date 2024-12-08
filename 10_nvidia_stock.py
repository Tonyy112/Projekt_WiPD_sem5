import yfinance as yf
from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from bokeh.models import DatetimeTickFormatter
from datetime import datetime
from threading import Thread
import time

# Funkcja do pobierania danych akcji NVIDIA
def fetch_nvidia_data():
    ticker = "NVDA"
    data = yf.download(ticker, period="1d", interval="1m")
    return data

# Funkcja do aktualizacji danych
def update_data():
    while True:
        try:
            # Pobierz dane i zaktualizuj źródło danych
            new_data = fetch_nvidia_data()
            source_data.data = {
                'datetime': new_data.index,
                'close': new_data['Close']
            }
        except Exception as e:
            print(f"Błąd podczas aktualizacji danych: {e}")
        time.sleep(60)  # Aktualizuj dane co 60 sekund

# Przygotowanie początkowych danych
data = fetch_nvidia_data()
source_data = ColumnDataSource(data=dict(
    datetime=data.index,
    close=data['Close']
))

# Utwórz wykres Bokeh
p = figure(
    title="NVIDIA Stock Price",
    x_axis_type='datetime',
    width=800,
    height=400
)
p.line('datetime', 'close', source=source_data, line_width=2, color='blue', legend_label='Close Price')
p.xaxis.formatter = DatetimeTickFormatter(minutes="%H:%M", hours="%H:%M")
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Price (USD)'
p.legend.location = "top_left"
p.title.align = "center"
p.title.text_font_size = "16pt"

# Układ interfejsu
layout = layout([p])

# Wątek do aktualizacji danych
thread = Thread(target=update_data, daemon=True)
thread.start()

# Uruchom aplikację Bokeh
curdoc().add_root(layout)
curdoc().title = "NVIDIA Stock Price Live"

show(p)