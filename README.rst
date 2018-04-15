imbutil
######
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

Additions to the ``imblearn`` package.

.. code-block:: python

  from imbutil.combine import MinMaxRandomSampler

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install imbutil


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


Credits
=======

Created by Shay Palachy (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/imbutil.svg
  :target: https://pypi.python.org/pypi/imbutil

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/imbutil.svg
   :target: https://pypi.python.org/pypi/imbutil

.. |Build-Status| image:: https://travis-ci.org/shaypal5/imbutil.svg?branch=master
  :target: https://travis-ci.org/shaypal5/imbutil

.. |LICENCE| image:: https://img.shields.io/github/license/shaypal5/imbutil.svg
  :target: https://github.com/shaypal5/imbutil/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/imbutil/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/imbutil?branch=master
