"""Testing MinMaxRandomSampler."""

import numpy as np
import pandas as pd
from pdutil.transform import x_y_by_col_lbl

from imbutil.combine import MinMaxRandomSampler

_DATA1 = [
    [23, 'Jo', 1],
    [33, 'Bo', 1],
    [10, 'Ki', 2],
    [82, 'Ro', 2],
    [70, 'Pi', 2],
    [72, 'Po', 2],
    [14, 'Li', 3],
    [81, 'Lo', 3],
    [73, 'Mi', 3],
    [79, 'Mo', 3],
    [44, 'Ma', 3],
    [78, 'Me', 3],
]


def _df1():
    return pd.DataFrame(
        data=_DATA1,
        columns=['age', 'name', 'label'],
    )


def test_basic_minmax_sample():
    print("testing MinMaxRandomSampler fit_sample...")
    df = _df1()
    sampler = MinMaxRandomSampler(min_freq=3, max_freq=4)
    X, y = x_y_by_col_lbl(df, 'label')
    new_X, new_y = sampler.fit_sample(X, y)
    print(new_X)
    print(new_y)
    label_counts = np.bincount(new_y)
    assert label_counts[1] == 3
    assert label_counts[2] == 4
    assert label_counts[3] == 4


if __name__ == '__main__':
    test_basic_minmax_sample()
