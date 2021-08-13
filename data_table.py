import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, DataTable, TableColumn

output_file("data_table.html")

df = pd.read_csv('data-20200422-structure-20190827.csv', encoding="cp1251")

source = ColumnDataSource(df)

columns = [
        TableColumn(field="Subject", title="Subject"),
        TableColumn(field="Value", title="Value"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

show(data_table)