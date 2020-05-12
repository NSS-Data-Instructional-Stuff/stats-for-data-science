import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import t
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import norm

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

def hypot_plot_mean(data, popmean, type = 'both', area = True):
    
    df = len(data) - 1
    
    test_stat, p = ttest_1samp(data, popmean = popmean)
    
    if type != 'both':
        p = p/2
    
    p = round(p,4)
    
    x_min = min(-np.abs(test_stat) - 0.25, -3)
    x_max = max(np.abs(test_stat) + 0.25, 3)
    
    
    x = np.linspace(x_min, x_max, 100)
    
    fig, ax = plt.subplots(1, 1, figsize = (8,4))
    ax.plot(x, t.pdf(x, df = df),'r-', lw=3, alpha=1, label='norm pdf', color = 'black')
    
    if type == 'both':
        left_section = np.linspace(x_min, -np.abs(test_stat), 100)
        right_section = np.linspace(np.abs(test_stat), x_max, 100)
        sections = [left_section, right_section]
        edges = [-np.abs(test_stat), np.abs(test_stat)]
        
    elif type == 'left':
        left_section = np.linspace(x_min, test_stat, 100)
        sections = [left_section]
        edges = [test_stat]

    elif type == 'right':
        right_section = np.linspace(test_stat, x_max, 100)
        sections = [right_section]
        edges = [test_stat]
    
    if area:
        for section in sections:
            plt.fill_between(section, t.pdf(section, df = df), color = 'red')
    for edge in edges:
        plt.vlines(x = edge, ymin =0, ymax = t.pdf(edge, df = df), lw = 3, color = 'black')
        plt.annotate(s = np.round(edge,4), xy = (edge, -0.01), fontsize = 14, fontweight = 'bold', 
                     va = 'top', ha = 'center')
        
    plt.annotate(s = 'Test\n Statistic', ha = 'center', va = 'top', fontweight = 'bold',
             xy = (test_stat, -.05), xytext = (test_stat, -.1), arrowprops=dict(width = 8, headwidth = 20, facecolor = 'red'))
    
    if area:
        area = p
        if type == 'both':
            #area = round(2*t.cdf(-np.abs(test_stat), df = n-1), 4)

            test_stat = np.abs(test_stat)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.01),
                    xytext = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = (-test_stat + 0.1, t.pdf(test_stat, df = df)/2),
                    xytext = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

        if type == 'right':
            #area = round(t.cdf(-test_stat, df = n-1), 4)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.01),
                    xytext = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

        if type == 'left':
            #area = round(t.cdf(test_stat, df = n-1), 4)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_min) / 2, t.pdf((test_stat + x_min)/2, df = df) + 0.01),
                    xytext = ((test_stat + x_min) / 2, t.pdf((test_stat + x_min)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))
    
    
    plt.hlines(y = 0, xmin = min(-3, -np.abs(test_stat + 0.25)), xmax = max(3, np.abs(test_stat + .25)))
    plt.yticks([])
    plt.xticks([])
    plt.annotate(s = '0', xy = (0, -0.01), fontsize = 14, fontweight = 'bold', 
                 va = 'top', ha = 'center')  
       
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.ylim(plt.ylim()[0] - .05, plt.ylim()[1])
    plt.tight_layout()
    plt.title('Sampling Distribution of the $\\frac{\\bar{x} - \\mu}{s}$, Assuming $H_0$', fontsize = 14);

def hypot_plot_mean_2sample(data1, data2, type = 'both', area = True):
    
    df = min(len(data1) - 1, len(data2) -1)
    
    test_stat, p = ttest_ind(data1, data2, equal_var = False)
    
    if type != 'both':
        p = p/2
    
    p = round(p,4)
    
    x_min = min(-np.abs(test_stat) - 0.25, -3)
    x_max = max(np.abs(test_stat) + 0.25, 3)
    
    
    x = np.linspace(x_min, x_max, 100)
    
    fig, ax = plt.subplots(1, 1, figsize = (8,4))
    ax.plot(x, t.pdf(x, df = df),'r-', lw=3, alpha=1, label='norm pdf', color = 'black')
    
    if type == 'both':
        left_section = np.linspace(x_min, -np.abs(test_stat), 100)
        right_section = np.linspace(np.abs(test_stat), x_max, 100)
        sections = [left_section, right_section]
        edges = [-np.abs(test_stat), np.abs(test_stat)]
        
    elif type == 'left':
        left_section = np.linspace(x_min, test_stat, 100)
        sections = [left_section]
        edges = [test_stat]

    elif type == 'right':
        right_section = np.linspace(test_stat, x_max, 100)
        sections = [right_section]
        edges = [test_stat]
    
    if area:
        for section in sections:
            plt.fill_between(section, t.pdf(section, df = df), color = 'red')
    for edge in edges:
        plt.vlines(x = edge, ymin =0, ymax = t.pdf(edge, df = df), lw = 3, color = 'black')
        plt.annotate(s = np.round(edge,4), xy = (edge, -0.01), fontsize = 14, fontweight = 'bold', 
                     va = 'top', ha = 'center')
        
    plt.annotate(s = 'Test\n Statistic', ha = 'center', va = 'top', fontweight = 'bold',
             xy = (test_stat, -.05), xytext = (test_stat, -.1), arrowprops=dict(width = 8, headwidth = 20, facecolor = 'red'))
    
    if area:
        area = p
        if type == 'both':
            #area = round(2*t.cdf(-np.abs(test_stat), df = n-1), 4)

            test_stat = np.abs(test_stat)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.01),
                    xytext = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = (-test_stat + 0.1, t.pdf(test_stat, df = df)/2),
                    xytext = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

        if type == 'right':
            #area = round(t.cdf(-test_stat, df = n-1), 4)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.01),
                    xytext = ((test_stat + x_max) / 2, t.pdf((test_stat + x_max)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

        if type == 'left':
            #area = round(t.cdf(test_stat, df = n-1), 4)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_min) / 2, t.pdf((test_stat + x_min)/2, df = df) + 0.01),
                    xytext = ((test_stat + x_min) / 2, t.pdf((test_stat + x_min)/2, df = df) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))
    
    
    plt.hlines(y = 0, xmin = min(-3, -np.abs(test_stat + 0.25)), xmax = max(3, np.abs(test_stat + .25)))
    plt.yticks([])
    plt.xticks([])
    plt.annotate(s = '0', xy = (0, -0.01), fontsize = 14, fontweight = 'bold', 
                 va = 'top', ha = 'center')  
       
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.ylim(plt.ylim()[0] - .05, plt.ylim()[1])
    plt.tight_layout()
    plt.title('Sampling Distribution of the $\\frac{\\bar{x}_1 - \\bar{x}_2}{s}$, Assuming $H_0$', fontsize = 14);


def hypot_plot_proportion_2sample(counts, nobs, alternative = 'two-sided', area = True):
    
    if alternative == 'two-sided':
        type = 'both'
    elif alternative == 'smaller':
        type = 'left'
    elif alternative == 'larger':
        type = 'right'
    
    test_stat, p = proportions_ztest(counts, nobs, alternative = alternative)
    
    p = round(p,4)
    
    x_min = min(-np.abs(test_stat) - 0.25, -3)
    x_max = max(np.abs(test_stat) + 0.25, 3)
    
    x = np.linspace(x_min, x_max, 100)
    
    fig, ax = plt.subplots(1, 1, figsize = (8,4))
    ax.plot(x, norm.pdf(x),'r-', lw=3, alpha=1, label='norm pdf', color = 'black')
    
    if type == 'both':
        left_section = np.linspace(x_min, -np.abs(test_stat), 100)
        right_section = np.linspace(np.abs(test_stat), x_max, 100)
        sections = [left_section, right_section]
        edges = [-np.abs(test_stat), np.abs(test_stat)]
        
    elif type == 'left':
        left_section = np.linspace(x_min, test_stat, 100)
        sections = [left_section]
        edges = [test_stat]

    elif type == 'right':
        right_section = np.linspace(test_stat, x_max, 100)
        sections = [right_section]
        edges = [test_stat]
    
    if area:
        for section in sections:
            plt.fill_between(section, norm.pdf(section), color = 'red')
    for edge in edges:
        plt.vlines(x = edge, ymin =0, ymax = norm.pdf(edge), lw = 3, color = 'black')
        plt.annotate(s = np.round(edge,4), xy = (edge, -0.01), fontsize = 14, fontweight = 'bold', 
                     va = 'top', ha = 'center')
        
    plt.annotate(s = 'Test\n Statistic', ha = 'center', va = 'top', fontweight = 'bold',
             xy = (test_stat, -.05), xytext = (test_stat, -.1), arrowprops=dict(width = 8, headwidth = 20, facecolor = 'red'))
    
    if area:
        area = p
        if type == 'both':
            #area = round(2*t.cdf(-np.abs(test_stat), df = n-1), 4)

            test_stat = np.abs(test_stat)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_max) / 2, norm.pdf((test_stat + x_max)/2) + 0.01),
                    xytext = ((test_stat + x_max) / 2, norm.pdf((test_stat + x_max)/2) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = (-test_stat + 0.1, norm.pdf(test_stat)/2),
                    xytext = ((test_stat + x_max) / 2, norm.pdf((test_stat + x_max)/2) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

        if type == 'right':
            #area = round(t.cdf(-test_stat, df = n-1), 4)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_max) / 2, norm.pdf((test_stat + x_max)/2) + 0.01),
                    xytext = ((test_stat + x_max) / 2, norm.pdf((test_stat + x_max)/2) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))

        if type == 'left':
            #area = round(t.cdf(test_stat, df = n-1), 4)

            plt.annotate(s = 'Area = {}'.format(area), ha = 'center', fontweight = 'bold', fontsize = 14,
                    xy = ((test_stat + x_min) / 2, norm.pdf((test_stat + x_min)/2) + 0.01),
                    xytext = ((test_stat + x_min) / 2, norm.pdf((test_stat + x_min)/2) + 0.2),
                    arrowprops=dict(width = 4, headwidth = 8, facecolor = 'black'))
    
    
    plt.hlines(y = 0, xmin = min(-3, -np.abs(test_stat + 0.25)), xmax = max(3, np.abs(test_stat + .25)))
    plt.yticks([])
    plt.xticks([])
    plt.annotate(s = '0', xy = (0, -0.01), fontsize = 14, fontweight = 'bold', 
                 va = 'top', ha = 'center')  
       
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.ylim(plt.ylim()[0] - .05, plt.ylim()[1])
    plt.tight_layout()
    plt.title('Sampling Distribution of the $\\frac{\\bar{p}_1 - \\bar{p}_2}{s_p}$, Assuming $H_0$', fontsize = 14);

def deviation_plot(Player, df):
    
    i = df.player.tolist().index(Player)
    
    salary = df.loc[i,'salary']
    mean = df['salary'].mean()

    print('Player: {}'.format(df.loc[i, 'player']))
    print('Salary: ${:,}'.format(df.loc[i, 'salary']))
    print('Mean Salary: ${:,}'.format(int(mean)))
    
    fig, ax = plt.subplots(figsize = (10,3))
    plt.scatter(df['salary'], [0 + 0.015]*len(df['salary']), edgecolor = 'black', s = 100)
    xmin, xmax = plt.xlim()
    
    plt.scatter([salary], [0 + 0.015], edgecolor = 'black', color = 'orange', s = 100)
    plt.annotate(s = 'Mean ($\mu$) \n \${:,}'.format(int(mean)), ha = 'center', va = 'top', fontweight = 'bold', fontsize = 12,
                 xy = (df['salary'].mean(), -.01), xytext = (df['salary'].mean(), -.06),
                 arrowprops=dict(width = 8, headwidth = 20, facecolor = 'red'))

    lineheight = 0.1
    
    plt.plot([mean, salary], [lineheight,lineheight], color = 'black', linewidth = 3)
    for x in [mean, salary]:
        plt.plot([x,x], [lineheight - 0.01, lineheight + 0.01], color = 'black', linewidth = 3)

    plt.annotate(s = '$x_i$ = \${:,}'.format(salary), xy = (salary, 0.035), fontsize = 14, fontweight = 'bold',
                ha = 'center', va = 'bottom')
        
    plt.annotate(s = '$x_i - \mu =$ \${:,}'.format(int(salary - mean)),
                 xy = ((mean + salary) / 2, lineheight + 0.025),
                 fontsize = 14, fontweight = 'bold', ha = 'center', va = 'bottom', color = 'red')

    xmin -= 4000000
    xmax += 4000000
    plt.hlines(y = 0, xmin = xmin, xmax = xmax)
    plt.xlim(xmin, xmax)
    plt.ylim(-0.15, 0.2)
    plt.yticks([]);
