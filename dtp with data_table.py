import pandas as pd
from bokeh.io import curdoc
from bokeh.models import DataTable, TableColumn
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.layouts import layout

output_file("dtp with data_table.html")

df = pd.read_csv('data-20200422-structure-20190827.csv', encoding="cp1251")

source = ColumnDataSource(df)

sub_list = source.data['Subject'].tolist()

p = figure(
  y_range=sub_list,
  title='Количество ДТП за январь-март 2020 года',
  x_axis_label='Количество ДТП с пострадавшими',
  y_axis_label='Федеральные округа',
  plot_width=800,
  plot_height=400,
  tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

p.hbar(
    y='Subject',
    right='Value',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=1,
    source=source
)

hover = HoverTool()
hover.tooltips = """
    <div>
        <div>@Subject</div>  
        <div><strong>Количество ДТП с пострадавшими: </strong>@Value</div>
    </div>
"""
p.add_tools(hover)

columns = [
        TableColumn(field="Subject", title="Subject"),
        TableColumn(field="Value", title="Value"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

layout = layout([
    [data_table],
    [p],
], sizing_mode='fixed')

curdoc().add_root(layout)

show(layout)