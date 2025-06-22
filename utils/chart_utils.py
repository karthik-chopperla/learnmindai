import matplotlib.pyplot as plt

def create_bar_chart(data, labels, title=""):
    fig, ax = plt.subplots()
    ax.bar(labels, data)
    ax.set_title(title)
    return fig
