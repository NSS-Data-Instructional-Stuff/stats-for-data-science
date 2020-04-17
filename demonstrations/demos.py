import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def confidence_interval_plot(area = 0.95, interval = 0):
    x = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 100)
    fig, ax = plt.subplots(1, 1, figsize = (14,4))
    ax.plot(x, norm.pdf(x),'r-', lw=3, alpha=1, label='norm pdf', color = 'black')
    x_min = norm.ppf((1-area) / 2)
    x_max = norm.ppf(1 - (1-area) / 2)
    if x_min < x_max:
        section = np.arange(x_min, x_max, 0.01)
        plt.fill_between(section,norm.pdf(section), color = 'slateblue')
    else:
        section_1 = np.arange(-3, x_max, 0.01)
        plt.fill_between(section_1, norm.pdf(section_1), color = 'slateblue')
        section_2 = np.arange(x_min, 3, 0.01)
        plt.fill_between(section_2, norm.pdf(section_2), color = 'slateblue')
    if x_min != -3:
        plt.vlines(x = x_min, ymin = 0, ymax = norm.pdf(x_min), lw = 3, color = 'black')
        #plt.xticks(ticks = [x_min], labels = [f'z = {x_min}'], fontsize = 14)
        plt.annotate(s = f'{round(x_min,2)}', xy = (x_min, -0.01), fontsize = 14, fontweight = 'bold', 
                     va = 'top', ha = 'center', color = 'orangered')
    if x_max != 3:
        plt.vlines(x = x_max, ymin = 0, ymax = norm.pdf(x_max), lw = 3, color = 'black')
        #plt.xticks(ticks = [x_max], labels = [f'z = {x_max}'], fontsize = 14)
        plt.annotate(s = f'{round(x_max,2)}', xy = (x_max, -0.01), fontsize = 14, fontweight = 'bold', 
                     va = 'top', ha = 'center', color = 'orangered')
        
    plt.annotate(s = f'Area = {area}', xy = (0, 0.01), fontsize = 14,
                va = 'bottom', ha = 'center', fontweight = 'bold', color = 'yellow')
    if True:
        plt.plot([interval + x_min, interval - 0.35], [-0.1, -0.1], lw = 3, color = 'red')
        plt.plot([interval + 0.35, interval + x_max], [-0.1, -0.1], lw = 3, color = 'red')
        plt.plot([interval + x_min, interval + x_min], [-0.09, -0.11], lw = 3, color = 'red')
        plt.plot([interval + x_max, interval + x_max], [-0.09, -0.11], lw = 3, color = 'red')
        plt.plot([interval, interval], [0, -0.08], lw = 3, linestyle = '--', color = 'black')
        plt.annotate(s = str(interval), xy = (interval, -0.1), 
                     va = 'center', ha = 'center',
                     fontsize = 14, fontweight = 'bold')
        plt.annotate(s = r'0', xy = (0, -0.01), fontsize = 14, fontweight = 'bold', 
                     va = 'top', ha = 'center', color = 'orangered')
        
    plt.plot([0, 0], [-0.15, 0.4], linestyle = '--', color = 'black')
        
    plt.hlines(y = 0, xmin = -3, xmax = 3)
    plt.yticks([])
    plt.xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.ylim(plt.ylim()[0] - 0.01, plt.ylim()[1])
    plt.xlim(-5.5, 5.5);
