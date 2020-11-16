import numpy as np

__all__ = ["pairwise_dists"]


def pairwise_dists(x, y):
    """ Computing pairwise distances using memory-efficient
    vectorization.

    Parameters
    ----------
    x : numpy.ndarray, shape=(M, D)
    y : numpy.ndarray, shape=(N, D)

    Returns
    -------
    numpy.ndarray, shape=(M, N)
        The Euclidean distance between each pair of
        rows between `x` and `y`."""
    dists = -2 * np.matmul(x, y.T)
    dists += np.sum(x**2, axis=1)[:, np.newaxis]
    dists += np.sum(y**2, axis=1)

    # The original function has:
    #
    # `return np.sqrt(dists)`
    #
    # But there is a problem here. It is possible
    # that entries in `x` and `y` are very similar.
    # Subtracting two very similar numbers will lead to
    # large numerical precision errors. So even though
    # it should be mathematically impossible for `dists` to
    # contain negative numbers, this can actually happen!
    # Thus we actually need to clip `dists` to make sure
    # all very-small negative numbers are set to 0.
    return np.sqrt(np.clip(dists, a_min=0., a_max=None))
