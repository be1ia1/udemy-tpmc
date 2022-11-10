# import pandas

# df = pandas.read_excel('verlegenhuken.xlsx')
# print(df['Temperature'])
import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_excel('verlegenhuken.xlsx')
output_file("graph.html")
p=figure()

p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (C)"
p.yaxis.axis_label="Pressure (hPa)"    
# df['Temperature'], df['Pressure']
p.circle([1,2,3,4,5],[5,6,7,8,9,10], size=10)

show(p)