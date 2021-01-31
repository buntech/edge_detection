# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# define the vertical filter
vertical_filter = [[-1, 2, 1], [0, 0, 0], [1, 2, 1]]

# define the horizontal filter
horizontal_filter = [[-1, 0, 1], [-2, 0, 2], [1, 2, 1]]

# リストは転置できないので、[ndarray]や[pandas]に変換 or zip() 使用
# horizontal_filter_T = vertical_filter.T


# read in the pinwheel image
img = plt.imread('./img/pinwheel.png')

# get the demensions of the image
n, m, d = img.shape

# initialize the edges image
edge_img = img.copy()
