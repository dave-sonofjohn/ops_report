import matplotlib.pyplot as plt

class DonutChart:
    def __init__(self, title, labels, values, d_type):
        self.title = title
        self.labels = labels
        self.values = values
        self.d_type = d_type

    def build(self):
        patches, texts = plt.pie(self.values, startangle=90)
        pct_list = []

        for i in range(len(self.values)):
            pct_list.append(round((self.values[i]/sum(self.values))*100, 2))

        formatted_labels = ['{0} - {1} {2} ({3} %)'.format(i, j, self.d_type, k) for i,j, k in zip(self.labels, self.values, pct_list)]  
        plt.legend(patches, formatted_labels, loc=(0.95, 0))

        plt.title('{}'.format(self.title))
        
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        
        fig.gca().add_artist(centre_circle)
        fig = plt.gcf().subplots_adjust(right=0.5)
        
        plt.tight_layout()
        return(plt)