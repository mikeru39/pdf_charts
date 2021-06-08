from bitrix24 import *
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

bx = Bitrix24('https://mike.bx-demo.polus.io/rest/1/iavftth7cp5mkbk4/')

data = bx.callMethod('crm.deal.list',

                     select=['TITLE', 'PROBABILITY'],
                     )


def set_pie_chart(labels, data, position):
    # colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    explode = []
    for i in data:
        explode.append(0.05)

    position.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)


def set_horizontal_chart(labels, data, position):
    position.barh(labels, data, align='center')


def set_vertical_chart(labels, data, position):
    position.bar(labels, data, align='center')


figure(figsize=(80, 60), dpi=80)
name = [i['TITLE'] for i in data]
print(name)
info = [i['PROBABILITY'] for i in data]
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.set_size_inches(18.5, 10.5)
set_pie_chart(name, info, ax1)
set_horizontal_chart(name, info, ax2)
set_vertical_chart(name, info, ax3)
# plt.show()
plt.savefig("plots.pdf", dpi=10)
