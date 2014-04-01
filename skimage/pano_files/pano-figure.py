from matplotlib import pyplot as plt
from skimage import io


images = map(io.imread, ['pano_4_0.png', 'pano_11_1.png', 'pano_15_1.png',
                         'pano_23_0.png', 'pano_28_0.png'])

plt.rcParams['axes.edgecolor'] = 'lightgray'
plt.rcParams['image.interpolation'] = 'nearest'
fig = plt.figure(figsize=(8, 6))
fig_shape = (5, 2)


x0 = 0.01
y0 = 0.99

ax0 = plt.subplot2grid(fig_shape, (0, 0))
ax0.imshow(images[0])
ax0.text(x0, y0, 'A', transform=ax0.transAxes, va='top', ha='left')

ax1 = plt.subplot2grid(fig_shape, (1, 0), rowspan=2)
ax1.imshow(images[1])
ax1.text(x0, y0, 'B', transform=ax1.transAxes, va='top', ha='left')

ax2 = plt.subplot2grid(fig_shape, (3, 0), rowspan=2)
ax2.imshow(images[2])
ax2.text(x0, y0, 'C', transform=ax2.transAxes, va='top', ha='left')

x1 = 0.99
y1 = 0.99

ax3 = plt.subplot2grid(fig_shape, (0, 1))
ax3.imshow(images[3])
ax3.text(x1, y1, 'D', transform=ax3.transAxes, va='top', ha='right')

ax4 = plt.subplot2grid(fig_shape, (1, 1), rowspan=4)
ax4.imshow(images[4])
ax4.text(x1, y1, 'E', transform=ax4.transAxes, va='top', ha='right')


def format_axes(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal', adjustable='datalim')

map(format_axes, [ax0, ax1, ax2, ax3, ax4])


plt.subplots_adjust(top=1, bottom=0, left=0, right=1, wspace=0, hspace=0)
plt.savefig('../figures/pano.pdf')
