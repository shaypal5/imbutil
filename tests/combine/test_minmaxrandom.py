"""Testing MinMaxRandomSampler."""

import numpy as np
import pandas as pd
from pdutil.transform import x_y_by_col_lbl

# for pipeline testing
from imblearn import pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

from imbutil.combine import MinMaxRandomSampler


_RANDOM_STATE = 83

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


_DATA2 = [
    [23, 56, 1],
    [33, 98, 1],
    [10, 77, 2],
    [82, 10, 2],
    [70, 65, 2],
    [72, 28, 2],
    [14, 22, 3],
    [81, 90, 3],
    [73, 35, 3],
    [79, 35, 3],
    [44, 83, 3],
    [78, 40, 3],
]


def _df2():
    return pd.DataFrame(
        data=_DATA2,
        columns=['age', 'num_legs', 'label'],
    )


def test_basic_minmax_sample():
    print("testing MinMaxRandomSampler fit_sample...")
    df = _df1()
    sampler = MinMaxRandomSampler(
        min_freq=3, max_freq=4, random_state=_RANDOM_STATE)
    X, y = x_y_by_col_lbl(df, 'label')
    new_X, new_y = sampler.fit_sample(X, y)
    print(new_X)
    print(new_y)
    label_counts = np.bincount(new_y)
    assert label_counts[1] == 3
    assert label_counts[2] == 4
    assert label_counts[3] == 4


def test_minmax_pipeline():
    sampler = MinMaxRandomSampler(
        min_freq=3, max_freq=4, random_state=_RANDOM_STATE)
    clf = LinearSVC(random_state=_RANDOM_STATE)
    pline = pipeline.make_pipeline(sampler, clf)

    df = _df2()
    X, y = x_y_by_col_lbl(df, 'label')
    labels = np.unique(y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=_RANDOM_STATE)

    pline.fit(X_train, y_train)
    y_pred_bal = pline.predict(X_test)
    assert len(y_pred_bal) == len(y_test)
    for x in y_pred_bal:
        assert x in labels


if __name__ == '__main__':
    test_basic_minmax_sample()
