from os.path import join, dirname
import datetime

import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.palettes import Blues4
from bokeh.plotting import figure

from collections import OrderedDict

months = OrderedDict([('January',1),
        ('February',2),
        ('March',3),
        ('April',4),
        ('May',5),
        ('June',6),
        ('July',7),
        ('August',8),
        ('September',9),
        ('October',10),
        ('November',11),
        ('December',12)
        ])
month_list = months.keys()
year_list = ['2012', '2013']
day_list =  [str(i) for i in range(1,32) ]

# Initialize with these strings:
year = '2012'
month = 'March'
day = '1'

year_select = Select(value=year, title='Year', options = year_list)
month_select = Select(value=month, title='Month', options = month_list)
day_select = Select(value=day, title = 'Day', options = day_list)

df = pd.read_csv('REU2016_volume_and_duration_by_hour.csv')


def get_dataset(src, year=year, month=month, day=day):
    df = src[ (src.year == year) & (src.month == month) & (src.day == day) ].copy()  #TODO why .copy ??
    #del df['airport']
    hours = df['hour'].values
    volume = df['Volume'].values
    return dict(x=hours,y=volume)

def make_plot(source, title):
    #plot = figure(x_axis_type="datetime", plot_width=800, tools="", toolbar_location=None)
    plot = figure(plot_width=800, plot_height=500, tools = "pan,wheel_zoom,box_zoom,save,reset,hover" )
    plot.title.text = title
#    plot.circle(x=source.data['hour'][0:40], y=source.data['Volume'][3:40], size=10)
    plot.circle('x','y', source=source)
#    plot.circle(x=source.data['x'], y=source.data['y'],size=10 )
    # fixed attributes
    plot.xaxis.axis_label = "Hour"
    plot.yaxis.axis_label = "Volume (unit?)"
    plot.axis.axis_label_text_font_style = "bold"
    #plot.x_range = DataRange1d(range_padding=0.0)
    plot.grid.grid_line_alpha = 0.3
    return plot

def update_plot(attrname, old, new):
    year  = year_select.value
    month = month_select.value
    day = day_select.value
    plot.title.text = "Rainwater Volume by hour for " + month + ' ' + day + ', ' + year
    updated_data = get_dataset(df, year=int(year), month=months[month], day=int(day) )
    source.data = updated_data #dict(x=x, y=y)

datadict = get_dataset(df, year = int(year), month = months[month], day = int(day) )
source = ColumnDataSource(datadict)

plot = make_plot(source, "Rainwater Volume by hour for " + month + ' ' + day + ', ' + year)

year_select.on_change('value', update_plot)
month_select.on_change('value', update_plot)
day_select.on_change('value', update_plot)

curdoc().add_root(row(
        column(year_select, month_select, day_select),
        plot ))
curdoc().title = "Rainwater Data"

