import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, WheelZoomTool, CrosshairTool

def load_data(file_path):
    # Загрузка исторических данных ставки ФРС
    df = pd.read_csv(file_path, header=None, names=['date', 'rate'], sep=';')
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
    df['rate'] = df['rate'].str.replace(',', '.').astype(float)
    return df

def create_figure():
    # Создание фигуры с центрированным заголовком
    p = figure(x_axis_type='datetime', height=600, width=800,
               title='Исторические ставки ФРС', toolbar_location=None)
    p.title.align = 'center'
    p.title.text_color = 'red'
    return p

def add_line(p, source):
    # Отображение линии
    p.line(x='date', y='rate', source=source, color='black', line_width=2)

def add_hover(p, source):
    # Отображение точек с подсказками
    hover_tool = HoverTool(tooltips=[('Дата', '@date{%d-%m-%Y}'), ('Ставка', '@rate{0.00}')],
                           formatters={'@date': 'datetime'})
    p.circle(x='date', y='rate', source=source, color='black', size=3, hover_color='red', hover_line_width=10)
    p.add_tools(hover_tool)

def add_tools(p):
    # Добавление инструментов
    p.toolbar.active_scroll = p.select_one(WheelZoomTool)
    p.add_tools(CrosshairTool())
    
def show_figure(p):
    # Отображение графика
    show(p)

if __name__ == '__main__':
    # Загрузка данных
    file_path = 'stavka.csv'
    df = load_data(file_path)

    # Создание источника данных
    source = ColumnDataSource(df)

    # Создание фигуры
    p = create_figure()

    # Добавление линии и точек с подсказками
    add_line(p, source)
    add_hover(p, source)

    # Добавление инструментов
    add_tools(p)

    # Отображение графика
    show_figure(p)
