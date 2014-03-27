#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Load picture
from skimage import data
image = data.coins()[0:95, 70:370]

plt.figure(figsize=(8, 5))
plt.subplot(3, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original', fontsize=30)
plt.axis('off')

# Histogram
values, bins = np.histogram(image, bins=np.arange(256))

plt.subplot(3, 2, 2)
plt.plot(bins[:-1], values)
plt.xlim(xmax=256)
plt.title('Histogram', fontsize=30)

# Apply threshold
from skimage.filter import threshold_adaptive
from skimage.morphology import closing, square

bw = threshold_adaptive(image, 95, offset=-15)

plt.subplot(3, 2, 3)
plt.imshow(bw, cmap=plt.cm.gray)
plt.title('Adaptive threshold', fontsize=30)
plt.axis('off')

# Find maxima
from skimage.feature import peak_local_max

coordinates = peak_local_max(image, min_distance=20)

plt.subplot(3, 2, 4)
plt.imshow(image, cmap=plt.cm.gray)
plt.autoscale(False)
plt.plot([p[1] for p in coordinates], [p[0] for p in coordinates], 'r.')
plt.axis('off')
plt.title('Peak local maxima', fontsize=30)

# Detect edges
from skimage import filter

edges = filter.canny(image, sigma=3, low_threshold=10, high_threshold=80)

plt.subplot(3, 2, 5)
plt.imshow(edges, cmap=plt.cm.gray)
plt.title('Edges', fontsize=30)
plt.axis('off')

# Label image regions
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

label_image = label(edges)

ax = plt.subplot(3, 2, 6)
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('Labeled items', fontsize=30)

for region in regionprops(label_image):
    # draw rectangle around segmented coins
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

plt.show()
