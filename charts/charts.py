import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D', 'E']
    values = [10, 20, 15, 25, 30]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close()