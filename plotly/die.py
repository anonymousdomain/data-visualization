from random import randint
from plotly.graph_objs import Layout ,Bar
from plotly import offline
class Die:
    def __init__(self, die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return randint(1, self.die_sides)


die1 = Die()
die2 = Die(10)
max_res=die1.die_sides+die2.die_sides
results = []
frequancey = []
for i in range(100):
    res = die1.roll()+die2.roll()
    results.append(res)
for value in range(2, max_res+1):
    freq = results.count(value)
    frequancey.append(freq)

x_v=list(range(2,max_res+1))
data=[Bar(x=x_v,y=frequancey)]

x_axis={'title':'Result'}
y_axis={'title':'frequncey of Result'}

layout=Layout(title='Results of rolling one D6 100 times',xaxis=x_axis,yaxis=y_axis)
offline.plot({'data':data,'layout':layout},filename='die.html')