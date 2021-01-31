import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline


# define the vertical filter
vertical_filter = [[-1, 2, 1], [0, 0, 0], [1, 2, 1]]

# define the horizontal filter
horizontal_filter = [[-1, 0, 1], [-2, 0, 2], [1, 2, 1]]

# read in the pinwheel image
img = plt.imread('./img/pinwheel.png')

# get the demensions of the image
n, m, d = img.shape

# initialize the edges image
edge_img = img.copy()
