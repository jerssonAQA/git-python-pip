import  matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,35,130]

    fig,ax =plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close