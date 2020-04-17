import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def range_plot(x, **kwargs):
    center = np.mean([np.min(x), np.max(x)])
    
    y = plt.hist(x, **kwargs)[0].max()
    y_range = plt.ylim()[1] - plt.ylim()[0]
    x_range = plt.xlim()[1] - plt.xlim()[0]
    
    plt.hlines(y = 0, xmin = np.min(x) - 0.01*x_range, xmax = np.max(x) + 0.01*x_range)
    plt.annotate(s = 'Range', ha = 'center', va = 'bottom', fontweight = 'bold',
                 xy = (center, y + 0.05*y_range), fontsize = 14)
    plt.plot([np.min(x), np.max(x)], [y + 0.05*y_range, y + 0.05*y_range], linewidth = 3, color = 'black')
    plt.plot([np.min(x), np.min(x)], [y+.02*y_range, y + .08*y_range], linewidth = 3, color = 'black')
    plt.plot([np.max(x), np.max(x)], [y+.02*y_range, y + .08*y_range], linewidth = 3, color = 'black')

    plt.ylim(-.1*y_range, y + 0.15*y_range);

def std_plot(x, **kwargs):
    mu = np.mean(x)
    sigma = np.std(x)

    y = plt.hist(x, **kwargs)[0].max()
    y_range = plt.ylim()[1] - plt.ylim()[0]
    x_range = plt.xlim()[1] - plt.xlim()[0]

    plt.hlines(y = 0, xmin = np.min(x) - 0.01*x_range, xmax = np.max(x) + 0.01*x_range)
    plt.annotate(s = 'Mean', ha = 'center', va = 'top', fontweight = 'bold',
                 xy = (np.mean(x), -.01*y_range), xytext = (np.mean(x), -.15*y_range), arrowprops=dict(width = 8, headwidth = 20, facecolor = 'red'))

    plt.annotate(s = '$\sigma$', ha = 'center', va = 'bottom', fontweight = 'bold',
                  xy = (mu - sigma / 2, y + 0.05*y_range), fontsize = 14)
    plt.annotate(s = '$\sigma$', ha = 'center', va = 'bottom', fontweight = 'bold',
                  xy = (mu + sigma / 2, y + 0.05*y_range), fontsize = 14)
    plt.plot([mu - sigma, mu], [y + 0.05*y_range, y + 0.05*y_range], linewidth = 3, color = 'black')
    plt.plot([mu, mu +sigma], [y + 0.05*y_range, y + 0.05*y_range], linewidth = 3, color = 'black')

    plt.plot([mu - sigma, mu - sigma], [y+.02*y_range, y+.08*y_range], linewidth = 3, color = 'black')
    plt.plot([mu, mu], [y+.02*y_range, y+.08*y_range], linewidth = 3, color = 'black')
    plt.plot([mu + sigma, mu + sigma], [y+.02*y_range, y+.08*y_range], linewidth = 3, color = 'black')

    plt.ylim(-.22*y_range, y + 0.15*y_range);


def iqr_plot(x, **kwargs):
    lq = np.quantile(x, 0.25)
    uq = np.quantile(x, 0.75)
    med = np.quantile(x, 0.5)

    y = plt.hist(x, **kwargs)[0].max()
    y_range = plt.ylim()[1] - plt.ylim()[0]
    x_range = plt.xlim()[1] - plt.xlim()[0]

    plt.hlines(y = 0, xmin = np.min(x) - 0.01*x_range, xmax = np.max(x) + 0.01*x_range)
    plt.annotate(s = 'Median', ha = 'center', va = 'top', fontweight = 'bold',
                 xy = (med, -.01*y_range), xytext = (med, -.15*y_range), arrowprops=dict(width = 8, headwidth = 20, facecolor = 'blue'))

    plt.annotate(s = 'IQR', ha = 'center', va = 'bottom', fontweight = 'bold',
                  xy = ((lq + uq) / 2, y + 0.05*y_range), fontsize = 14)
    
    plt.plot([lq, uq], [y + 0.05*y_range, y + 0.05*y_range], linewidth = 3, color = 'black')
    
    plt.plot([lq, lq], [y+.02*y_range, y+.08*y_range], linewidth = 3, color = 'black')
    plt.plot([uq, uq], [y+.02*y_range, y+.08*y_range], linewidth = 3, color = 'black')

    plt.ylim(-.22*y_range, y + 0.15*y_range);

def qq_plot(data):
    mu = np.mean(data)
    sigma = np.std(data)
    
    sm.qqplot(data, line='45', loc = mu, scale = sigma);
