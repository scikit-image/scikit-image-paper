#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Load picture.
from skimage import data
image = data.coins()[0:95, 70:370]

fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(8, 4))
ax[0, 0].imshow(image, cmap=plt.cm.gray)
ax[0, 0].set_title('Original', fontsize=24)
ax[0, 0].axis('off')

# Histogram.
values, bins = np.histogram(image, bins=np.arange(256))

ax[0, 1].plot(bins[:-1], values)
ax[0, 1].set_xlim(xmax=256)
ax[0, 1].set_aspect(.2)
ax[0, 1].set_title('Histogram', fontsize=24)

# Apply threshold.
from skimage.filter import threshold_adaptive

bw = threshold_adaptive(image, 95, offset=-15)

ax[1, 0].imshow(bw, cmap=plt.cm.gray)
ax[1, 0].set_title('Adaptive threshold', fontsize=24)
ax[1, 0].axis('off')

# Find maxima.
from skimage.feature import peak_local_max

coordinates = peak_local_max(image, min_distance=20)

ax[1, 1].imshow(image, cmap=plt.cm.gray)
ax[1, 1].autoscale(False)
ax[1, 1].plot(coordinates[:, 1], coordinates[:, 0], 'r.')
ax[1, 1].set_title('Peak local maxima', fontsize=24)
ax[1, 1].axis('off')
ax[1, 1].axis('off')

# Detect edges.
from skimage import filter

edges = filter.canny(image, sigma=3, low_threshold=10, high_threshold=80)

ax[2, 0].imshow(edges, cmap=plt.cm.gray)
ax[2, 0].set_title('Edges', fontsize=24)
ax[2, 0].axis('off')

# Label image regions.
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

label_image = label(edges)

ax[2, 1].imshow(image, cmap=plt.cm.gray)
ax[2, 1].set_title('Labeled items', fontsize=24)
ax[2, 1].axis('off')

for region in regionprops(label_image):
    # Draw rectangle around segmented coins.
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax[2, 1].add_patch(rect)

plt.tight_layout()
plt.show()
