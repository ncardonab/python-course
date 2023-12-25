import matplotlib.pyplot as plt


plt.style.use('dark_background')
def generate_bar_chart(labels, values):
    _, ax = plt.subplots()
    plt.xticks(rotation='vertical')
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.pie(values, wedgeprops=dict(width=0.6), startangle=-40)
    plt.legend(labels, loc='center left', bbox_to_anchor=(-0.1, .5), fontsize=8)
    plt.title(title)
    ax.axis('equal')
    plt.show()
