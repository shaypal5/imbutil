"""Randomly samples data to bring all class frequencies into a range."""

import numpy as np
from sklearn.utils import check_X_y

from imblearn.base import SamplerMixin
from imblearn.utils import check_target_type, hash_X_y
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler


class MinMaxRandomSampler(SamplerMixin):
    """Random samples data to bring all class frequencies into a range.

    Parameters
    ----------
    min_freq : int
        The minimum frequency for a class after sampling. All classes with
        fewer samples are over-sampled to have this number of samples.
    max_freq : int
        The maximum frequency for a class after sampling. All classes with
        more samples are under-sampled to have this number of samples.
    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by np.random.
    """

    def __init__(self, min_freq, max_freq, random_state=None):
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.random_state = random_state
        self.ratio = max_freq / min_freq

    def fit(self, X, y):
        """Find the classes statistics before to perform sampling.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_samples, n_features)
            Matrix containing the data which have to be sampled.
        y : array-like, shape (n_samples,)
            Corresponding label for each sample in X.

        Returns
        -------
        self : object,
            Return self.
        """
        X, y = check_X_y(X, y, accept_sparse=['csr', 'csc'], dtype=None)
        y = check_target_type(y)
        self.ratio_ = self.ratio
        self.X_hash_, self.y_hash_ = hash_X_y(X, y)
        labels = np.unique(y)
        counts = np.bincount(y)
        under_dict = {}
        over_dict = {}
        for lbl in labels:
            count = counts[lbl]
            if count < self.min_freq:
                under_dict[lbl] = count
                over_dict[lbl] = self.min_freq
            elif count > self.max_freq:
                under_dict[lbl] = self.max_freq
                over_dict[lbl] = self.max_freq
            else:
                under_dict[lbl] = count
                over_dict[lbl] = count
        self.under_sampler = RandomUnderSampler(
            ratio=under_dict, random_state=self.random_state)
        self.over_sampler = RandomOverSampler(
            ratio=over_dict, random_state=self.random_state)
        return self

    def _sample(self, X, y):
        """Resample the dataset.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_samples, n_features)
            Matrix containing the data which have to be sampled.
        y : array-like, shape (n_samples,)
            Corresponding label for each sample in X.

        Returns
        -------
        X_resampled : {ndarray, sparse matrix}, shape \
        (n_samples_new, n_features)
            The array containing the resampled data.
        y_resampled : ndarray, shape (n_samples_new)
            The corresponding label of `X_resampled`
        """
        new_X, new_y = self.under_sampler.fit_sample(X, y)
        return self.over_sampler.fit_sample(new_X, new_y)
