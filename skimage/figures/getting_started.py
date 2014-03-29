#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Load picture.
from skimage import data
image = data.coins()[0:95, 70:370]

fig, axes = plt.subplots(ncols=2, nrows=3, figsize=(6, 4.5))
ax0, ax1, ax2, ax3, ax4, ax5  = axes.flat
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Original')
ax0.axis('off')

# Histogram.
values, bins = np.histogram(image, bins=np.arange(256))

ax1.plot(bins[:-1], values, lw=2)
ax1.set_xlim(xmax=256)
ax1.set_aspect(.2)
ax1.set_title('Histogram')
ax1.set_yticks(np.arange(0, 500, 100))

# Apply threshold.
from skimage.filter import threshold_adaptive

bw = threshold_adaptive(image, 95, offset=-15)

ax2.imshow(bw, cmap=plt.cm.gray)
ax2.set_title('Adaptive threshold')
ax2.axis('off')

# Find maxima.
from skimage.feature import peak_local_max

coordinates = peak_local_max(image, min_distance=20)

ax3.imshow(image, cmap=plt.cm.gray)
ax3.autoscale(False)
ax3.plot(coordinates[:, 1], coordinates[:, 0], 'r.')
ax3.set_title('Peak local maxima')
ax3.axis('off')
ax3.axis('off')

# Detect edges.
from skimage import filter

edges = filter.canny(image, sigma=3, low_threshold=10, high_threshold=80)

ax4.imshow(edges, cmap=plt.cm.gray)
ax4.set_title('Edges')
ax4.axis('off')

# Label image regions.
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

label_image = label(edges)

ax5.imshow(image, cmap=plt.cm.gray)
ax5.set_title('Labeled items')
ax5.axis('off')

for region in regionprops(label_image):
    # Draw rectangle around segmented coins.
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax5.add_patch(rect)

plt.tight_layout()
plt.savefig('getting_started.png', dpi=200)
plt.show()
