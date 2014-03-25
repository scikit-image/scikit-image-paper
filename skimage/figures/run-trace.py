import numpy as np
from skimage.measure import profile_line
from skimage.measure.profile import _line_profile_coordinates as lpcoords
from skimage import io
from skimage import draw
import trace as tr
from matplotlib import pyplot as plt, cm

im = io.imread('zebrafish-spinal-cord.png')
img = np.dstack([np.zeros_like(im), im, np.zeros_like(im)]).astype(float) / im.max()
top_mode, top_width = tr.estimate_mode_width(im[0])
bottom_mode, bottom_width = tr.estimate_mode_width(im[-1])
overlay = np.ones_like(img)
rr, cc = draw.line(0, top_mode, im.shape[0] - 1, bottom_mode)
rect = lpcoords((0, top_mode), (im.shape[1] - 1, bottom_mode),
                (top_width + bottom_width) / 2)
rcorners = np.rint(rect[0][[0, 0, -1, -1], [0, -1, -1, 0]]).astype(int)
ccorners = np.rint(rect[1][[0, 0, -1, -1], [0, -1, -1, 0]]).astype(int)
rrect, crect = draw.polygon(rcorners, ccorners, overlay.shape)
overlay[rrect, crect] = 0.5
overlay[rr, cc] = 0.0
fig, axes = plt.subplots(1, 3, figsize=(8, 3))

axes[0].imshow(img, interpolation='nearest')
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].set_title('original image')

axes[1].imshow(1 - overlay, interpolation='nearest', cmap=cm.gray)
prof = profile_line(im, (0, top_mode), (im.shape[1] - 1, bottom_mode),
                    linewidth=(top_width + bottom_width) / 2, mode='reflect')
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].set_title('measured overlay')

axes[2].plot(prof, lw=2, c='k')
axes[2].set_ylabel('mean intensity')
axes[2].set_xlabel('distance in pixels')
axes[2].set_ylim(0, 2000)
axes[2].set_xlim(0, 1100)
axes[2].set_yticks(np.arange(200, 2000, 400))
axes[2].set_xticks(np.arange(200, 1100, 400))
axes[2].set_title('intensity profile')

plt.tight_layout()
plt.savefig('fig2.png', bbox_inches='tight', dpi=600)

