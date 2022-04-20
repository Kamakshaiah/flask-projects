import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os, time, glob

def compute(m, n):

    x = np.random.uniform(0, 1, m)
    y = np.random.normal(0, 1, n)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(x, y)
    plt.title('sample plot')

    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile
