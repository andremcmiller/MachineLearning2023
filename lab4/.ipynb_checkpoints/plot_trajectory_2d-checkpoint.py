import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_levels(func, ax, xrange=None, yrange=None, levels=None):
    if xrange is None:
        xrange = [-6, 6]
    if yrange is None:
        yrange = [-5, 5]
    if levels is None:
        levels = [0, 0.25, 1, 4, 9, 16, 25]
        
    x = np.linspace(xrange[0], xrange[1], 100)
    y = np.linspace(yrange[0], yrange[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros(X.shape)
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            Z[i, j] = func(np.array([X[i, j], Y[i, j]]))

    CS = ax.contour(X, Y, Z, levels=levels, colors='k')
    ax.clabel(CS, inline=1, fontsize=8) 
    ax.grid()              

        
def plot_trajectory(func, history, ax, fit_axis=False, label=None):
    x_values, y_values = zip(*history)
    ax.plot(x_values, y_values, '-v', 
             alpha=1.0, c='r', label=label)
    
    # Tries to adapt axis-ranges for the trajectory:
    if fit_axis:
        xmax, ymax = np.max(x_values), np.max(y_values)
        COEF = 1.5
        xrange = [-xmax * COEF, xmax * COEF]
        yrange = [-ymax * COEF, ymax * COEF]
        ax.xlim(xrange)
        ax.ylim(yrange)

