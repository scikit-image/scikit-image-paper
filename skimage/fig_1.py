from skimage import data
from paper import savefig

import matplotlib.pyplot as plt
plt.imshow(data.chelsea())

savefig('fig_chelsea.png')
