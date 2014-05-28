#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=9)
matplotlib.rc('xtick', labelsize=7)
matplotlib.rc('ytick', labelsize=7)

import glob

import skimage.io
from skimage import filter
from skimage.transform import hough_circle
from skimage.feature import peak_local_max
from skimage.draw import circle_perimeter


# Load the first picture and detect the drop edge
image = skimage.io.imread('data/im00070.png', as_grey=True)
edges = filter.canny(image, sigma=2.0)

# Hough transform
hough_radii = np.arange(400, 500, 5)
hough_res = hough_circle(edges, hough_radii)

centers = []
accums = []
radii = []

for radius, h in zip(hough_radii, hough_res):
    # For each radius, extract two circles
    peaks = peak_local_max(h, num_peaks=2)
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius, radius])

# Draw the detected edge (circle, largest accumulator)
idx = np.argsort(accums)[::-1][0]
center_x, center_y = centers[idx]
radius = radii[idx]

# Generate points of the inner circle
radius2 = int(radius * 35/40.)
rr, cc = circle_perimeter(center_y, center_x, radius2, method='andres')

# Sort rr,cc according to the angle
points = np.vstack((rr, cc))
idx = np.argsort(np.arctan2(rr-center_y, cc-center_x))
points = points[:, idx]
rr, cc = points

# Scan each picture (1 over 10 of the record)
pictures = sorted(glob.glob('data/*0.png'))
spacetime = []
for picture in pictures:
    img = skimage.io.imread(picture, as_grey=True)
    spacetime.append(img[cc, rr].tolist())

# Plot
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(6, 4.2))
ax1.imshow(spacetime, cmap=plt.cm.gray,
           extent=[0, 360, np.shape(spacetime)[0], 0])
ax1.set_xlabel('Angle')
ax1.set_xticks([0, 90, 180, 270, 360])
ax1.set_ylabel('Time')
ax1.set_yticks([0, 100, 200])
ax1.set_aspect(0.5)
plt.savefig('fig_cracks.eps', dpi=600)
