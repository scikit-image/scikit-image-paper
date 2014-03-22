import numpy as np
from scipy import ndimage as nd
try:
    from skimage.measure import profile_line
except ImportError:
    from .profile import profile_line


def estimate_mode_width(distribution):
    """Estimate mode and width-at-half-maximum for a 1D distribution.

    Parameters
    ----------
    distribution : array of int or float
        The input distribution. ``plt.plot(distribution)`` should look
        like a histogram.

    Returns
    -------
    mode : int
        The location of the mode of the distribution.
    whm : int
        The difference between the top and bottom crossing points for
        the distribution at ``y = mode / 2``.

    Notes
    -----
    The distribution is assumed to have a unique mode.

    Examples
    --------
    >>> distribution = np.array([0, 0, 4, 8, 16, 22, 16, 8, 4, 0, 0])
    >>> estimate_mode_width(distribution)
    (5, 3)
    """
    mode = distribution.argmax()
    halfmax = float(distribution[mode]) / 2
    whm = (distribution > halfmax).astype(np.int).sum()
    return mode, whm


def trace_profile(image, sigma=5., width_factor=1., check_vertical=False):
    """Trace the intensity profile of a tubular structure in an image.

    Parameters
    ----------
    image : array of int or float, shape (M, N[, P])
        The input image. If 3D, the first dimension is flattened by
        summing along that axis.
    sigma : float, optional
        Convolve the intensity with this sigma to estimate the start
        and end of the scan lines.
    width_factor : float, optional
        The width of the line profile is determined automatically, then
        multiplied by this factor.
    check_vertical : bool, optional
        Check whether the tube is arranged top-to-bottom in the image.
        If `False`, it is assumed to be vertical, otherwise, the
        orientation is automatically determined from the image.

    Returns
    -------
    profile : 1D array of float
        The intensity profile of the tube.

    Examples
    --------
    >>> edges = np.array([8, 16, 22, 16, 8])
    >>> middle = np.array([0, 0, 0, 0, 0])
    >>> image = np.vstack([edges, middle, edges])
    >>> trace_profile(image, sigma=0)
    array([ 18.,   0.,  18.])
    """
    if image.ndim > 2:
        image = image.sum(axis=0)
    if check_vertical:
        top_bottom_mean = np.mean(image[[0, image.shape[0] - 1], :])
        left_right_mean = np.mean(image[:, [0, image.shape[1] - 1]])
        if top_bottom_mean < left_right_mean:
            image = image.T
    top_distribution = nd.gaussian_filter1d(image[0], sigma)
    bottom_distribution = nd.gaussian_filter1d(image[-1], sigma)
    top_loc, top_whm = estimate_mode_width(top_distribution)
    bottom_loc, bottom_whm = estimate_mode_width(bottom_distribution)
    angle = np.arctan(np.abs(float(bottom_loc - top_loc)) / image.shape[0])
    width = np.int(np.ceil(max(top_whm, bottom_whm) * np.cos(angle)))
    profile = profile_line(image,
                           (0, top_loc), (image.shape[0] - 1, bottom_loc),
                           linewidth=width, mode='nearest')
    return profile


if __name__ == '__main__':
    import sys
    from skimage import io
    images = io.imread_collection(sys.argv[1:])
    profiles = map(trace_profile, images)
    np.savez_compressed('profiles.npz', profiles)

