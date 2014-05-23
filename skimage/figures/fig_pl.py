import matplotlib
from matplotlib import pyplot as plt
from skimage import io, color


matplotlib.rc('font', size=7)


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(6, 3))
images = [io.imread('fig_pl%i.png' % i) for i in range(1, 4)]
titles = ['Normal photograph', 'Photoluminescence', 'Processed']

for ax, im, ti in zip(axes, images, titles):
    ax.imshow(color.gray2rgb(im), interpolation='nearest')
    ax.axis('off')
    ax.set_title(ti)

plt.tight_layout()
plt.savefig('fig_pl.pdf', dpi=600)
