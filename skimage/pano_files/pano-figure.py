from matplotlib import pyplot as plt
from skimage import io


images = map(io.imread, ['pano_4_0.png', 'pano_11_1.png', 'pano_15_1.png',
                         'pano_23_0.png', 'pano_28_0.png'])

plt.rcParams['axes.edgecolor'] = 'none'
plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['image.interpolation'] = 'nearest'
fig = plt.figure(figsize=(8, 6))
grid_shape = (5, 2)

center = 0.5
bottom = 0
text_alignment = {'verticalalignment': 'center',
                  'horizontalalignment': 'center'}

label_0 = "(a) Petra images"
ax0 = plt.subplot2grid(grid_shape, (0, 0))
ax0.imshow(images[0])
ax0.text(center, bottom, label_0, transform=ax0.transAxes, **text_alignment)

label_1 = "(b) ORB binary features"
ax1 = plt.subplot2grid(grid_shape, (1, 0), rowspan=2)
ax1.imshow(images[1])
ax1.text(center, bottom, label_1, transform=ax1.transAxes, **text_alignment)

label_2 = "(c) RANSAC-filtered features"
ax2 = plt.subplot2grid(grid_shape, (3, 0), rowspan=2)
ax2.imshow(images[2])
ax2.text(center, bottom, label_2, transform=ax2.transAxes, **text_alignment)


label_3 = "(d) Warped & positioned"
ax3 = plt.subplot2grid(grid_shape, (0, 1))
ax3.imshow(images[3])
ax3.text(center, bottom, label_3, transform=ax3.transAxes, **text_alignment)

label_4 = "(e) Final result, combined with Enblend"
ax4 = plt.subplot2grid(grid_shape, (1, 1), rowspan=4)
ax4.imshow(images[4])
ax4.text(center, bottom, label_4, transform=ax4.transAxes, **text_alignment)


def format_axes(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal', adjustable='datalim')

map(format_axes, [ax0, ax1, ax2, ax3, ax4])


plt.subplots_adjust(top=0.99, bottom=0.01, left=0.01, right=0.99,
                    wspace=0, hspace=0.1)
plt.savefig('pano.png', dpi=600)
