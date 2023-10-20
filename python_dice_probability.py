from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Dd():
    ''''Class for 1 cube'''
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    


dd_1 = Dd()
dd_2 = Dd()
results = []

for roll_num in range(10000):
    result = dd_1.roll() + dd_2.roll()
    results.append(result)

    frequencies = []
    max_result = dd_1.num_sides + dd_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value) 
        frequencies.append(frequency)

    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')