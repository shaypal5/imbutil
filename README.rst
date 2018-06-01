imbutil
#######
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

Additions to the ``imbalanced-learn`` package.

.. code-block:: python

  from imbutil.combine import MinMaxRandomSampler; from imblearn import pipeline;
  # oversampling minority classes to 100 and undersampling majority classes to 800
  sampler = MinMaxRandomSampler(min_freq=100, max_freq=800)
  sampling_clf = pipeline.make_pipeline(sampler, inner_clf)
  

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install imbutil


Additionally, the ``MinMaxRandomSampler``, in addition to ``RandomUnderSampler`` and ``RandomOverSampler`` from ``imbalanced-learn``, can technically be used with non-numeric data. However, the current implementation of ``imbalanced-learn`` forces a check for numeric data for all samplers. If you want to bypass this limitation, I have a fork of the project which does not force data to be numeric. You can install it with:

.. code-block:: bash

    pip install git+https://github.com/shaypal5/imbalanced-learn.git@f6adc562fafdc2198931873799e725e5abdd65a1


Basic Use
=========

``imbutil`` additions addhere to the structure of the ``imblearn`` package:

combine
-------

Containes samplers that both under-sample and over-sample:

``MinMaxRandomSampler`` - Random samples data to bring all class frequencies into a range.


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/imbutil.git


Install in development mode, and with test dependencies:

.. code-block:: bash

  cd imbutil
  pip install -e ".[test]"


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd imbutil
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by Shay Palachy (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/imbutil.svg
  :target: https://pypi.org/project/imbutil

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/imbutil.svg
   :target: https://pypi.org/project/imbutil

.. |Build-Status| image:: https://travis-ci.org/shaypal5/imbutil.svg?branch=master
  :target: https://travis-ci.org/shaypal5/imbutil

.. |LICENCE| image:: https://img.shields.io/github/license/shaypal5/imbutil.svg
  :target: https://github.com/shaypal5/imbutil/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/imbutil/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/imbutil?branch=master
