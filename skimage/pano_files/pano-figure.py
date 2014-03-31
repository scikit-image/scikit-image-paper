from matplotlib import pyplot as plt
from skimage import io
images = map(io.imread, ['pano_4_0.png', 'pano_11_1.png', 'pano_15_1.png',
                         'pano_23_0.png', 'pano_28_0.png'])
fig = plt.figure(figsize=(8, 8))

ax0 = plt.subplot2grid((4, 2), (0, 0))
ax0.imshow(images[0], interpolation='nearest')
#ax0.set_xticks([])
#ax0.set_yticks([])
ax0.set_title('A', loc='left')

ax1 = plt.subplot2grid((4, 2), (1, 0))
ax1.imshow(images[1], interpolation='nearest')
#ax1.set_yticks([])
#ax1.set_xticks([])
ax1.set_title('B', loc='left')

ax2 = plt.subplot2grid((4, 2), (2, 0))
ax2.imshow(images[2], interpolation='nearest')
#ax2.set_xticks([])
#ax2.set_yticks([])
ax2.set_title('C', loc='left')

ax3 = plt.subplot2grid((4, 2), (3, 0))
ax3.imshow(images[3], interpolation='nearest')
#ax3.set_xticks([])
#ax3.set_yticks([])
ax3.set_title('D', loc='left')

ax4 = plt.subplot2grid((4, 2), (0, 1), rowspan=4)
ax4.imshow(images[4], interpolation='nearest')
#ax4.set_xticks([])
#ax4.set_yticks([])
ax4.set_title('E', loc='left')

def remove_ticks(axis):
    axis.set_xticks([])
    axis.set_yticks([])

map(remove_ticks, [ax0, ax1, ax2, ax3, ax4])

plt.tight_layout()
plt.savefig('pano-full.png', bbox_inches='tight', dpi=600)
