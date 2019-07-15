import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

class BarChart:
    def __init__(self, title, ds, y_axis=None, x_axis=None):
        self.title = title
        self.ds = ds
        self.x_axis = x_axis
        self.y_axis = y_axis

    def build_mult(self):
        c_labels = self.ds.columns.values 
        colors = ['royalblue', 'red', 'orange', 'green', 'purple', 'deepskyblue', 'deeppink', 'limegreen', 'firebrick']
        x_labels = self.ds.index
        sizes = self.ds.head(5).values

        fig, axes = plt.subplots(ncols=sizes.shape[0], figsize=(12, 5), sharey=True)
        plt.gcf().subplots_adjust(bottom=0.2)

        for ax, height, title in zip(axes, sizes, x_labels):
            ax.set_title(title)
            left = np.arange(len(height)) + 1
            ax.bar(left, height, color=colors)
            ax.set_ylabel(self.y_axis, fontsize=8)
            ax.set_xticks(left)
            ax.set_xticklabels(c_labels, rotation=45, rotation_mode='anchor', ha='right')
            
            if len(self.ds.columns) <= 8:
                for i in ax.patches:
                    ax.text(i.get_x()+0.3, i.get_height()+.3, str(i.get_height()), fontsize=7)

            else:
                for i in ax.patches:
                    ax.set_xticklabels(c_labels, fontsize=7)
                    ax.text(i.get_x(), i.get_height()+.25, str(i.get_height()), fontsize=7)
                      
        return(plt)

    def build_hz(self):
        plt.rcdefaults()
        fig, ax = plt.subplots(figsize=(8,4))
        plt.gcf().subplots_adjust(left=0.28, right=0.9, top=0.9)

        labels = list(self.ds.index)
        y_pos = np.arange(len(labels))
        values = list(self.ds.values)
                
        ax.barh(y_pos, values, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        
        ax.invert_yaxis()
        ax.set_ylabel(self.y_axis)
        ax.set_xlabel(self.x_axis)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_title(self.title)
        ax.set_xlim(0, 1.25*(max(self.ds.values)))

        if max(self.ds.values) < 5:
            for i in ax.patches:
                ax.text(i.get_width()+.1, i.get_y()+.43, str(i.get_width()))

        else:
            for i in ax.patches:
                ax.text(i.get_width()+.3, i.get_y()+.43, str(i.get_width()))

        return(plt)

    def build_single(self):

        ax = self.ds[list(self.ds.columns.values)].plot(kind='bar', width=0.5, align='center', title=self.title, figsize=(12, 9), legend=True, fontsize=8)
       
        ax.set_xlabel(self.x_axis, fontsize=8)
        ax.set_xticklabels(self.ds.index, wrap=True, rotation=45)
        
        ax.set_ylabel(self.y_axis, fontsize=8)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.gcf().subplots_adjust(left=0.1, right=0.75, top=0.9)
        plt.legend(loc=(1.04,0))

        for i in ax.patches:
            ax.text(i.get_x()+0.3*(i.get_width()), i.get_height()+.01*(i.get_height()), str(i.get_height()), fontsize=10)

        return(plt)