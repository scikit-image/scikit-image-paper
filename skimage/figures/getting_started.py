#!/usr/bin/env python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Setup figure
matplotlib.rc('font', size=9)
matplotlib.rc('xtick', labelsize=7)
matplotlib.rc('ytick', labelsize=7)
center = 0.5
bottom = -0.1

fig, axes = plt.subplots(ncols=2, nrows=3, figsize=(6, 4))
fig.subplots_adjust(left=0.01, right=0.98, top=0.95, bottom=0.01,
                    wspace=0.12, hspace=0.12)
ax0, ax1, ax2, ax3, ax4, ax5  = axes.flat


# Load picture.
from skimage import data
image = data.coins()[0:95, 70:370]

label_0 = "(a) Original"
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title(label_0)
ax0.axis('off')


# Histogram
values, bins = np.histogram(image, bins=np.arange(256))

label_1 = "(b) Histogram"
ax1.plot(bins[:-1], values, lw=2, c='k')
ax1.set_xlim(xmax=256)
ax1.set_yticks([0, 400])
ax1.set_aspect(.2)
ax1.set_title(label_1)


# Apply threshold
from skimage.filter import threshold_adaptive

bw = threshold_adaptive(image, 95, offset=-15)

label_2 = "(c) Adaptive threshold"
ax2.imshow(bw, cmap=plt.cm.gray)
ax2.set_title(label_2)
ax2.axis('off')

# Find maxima
from skimage.feature import peak_local_max

coordinates = peak_local_max(image, min_distance=20)

label_3 = "(d) Peak local maxima"
ax3.imshow(image, cmap=plt.cm.gray)
ax3.autoscale(False)
ax3.plot(coordinates[:, 1], coordinates[:, 0], 'r.')
ax3.set_title(label_3)
ax3.axis('off')
ax3.axis('off')


# Detect edges
from skimage import filter

edges = filter.canny(image, sigma=3, low_threshold=10, high_threshold=80)

label_4 = "(e) Edges"
ax4.imshow(edges, cmap=plt.cm.gray)
ax4.set_title(label_4)
ax4.axis('off')


# Label image regions
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

label_image = label(edges)

label_5 = "(f) Labeled items"
ax5.imshow(image, cmap=plt.cm.gray)
ax5.set_title(label_5)
ax5.axis('off')

for region in regionprops(label_image):
    # Draw rectangle around segmented coins
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax5.add_patch(rect)

plt.savefig('getting_started.eps', dpi=600)
plt.savefig('getting_started.png', dpi=600)
