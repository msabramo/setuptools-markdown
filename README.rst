setuptools-markdown
===================

Use `Markdown <http://daringfireball.net/projects/markdown/>`__ for your
project description

-------------------------------------------------------------------------

This project is deprecated.
===========================

**Instead of using this, you should use the built-in functionality of
setuptools and PyPI.**

See `this page
<https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi/>`__
for details.

-------------------------------------------------------------------------


Install
=======

1. Install `pandoc <http://johnmacfarlane.net/pandoc/>`_

2. Install this module

.. code:: console

    pip install setuptools-markdown


Use
===

.. code:: python

    #!/usr/bin/env python
    # setup.py

    from setuptools import setup

    setup(
        ...
        setup_requires=['setuptools-markdown'],
        long_description_markdown_filename='README.md',
        ...
    )

The plugin will read the specified file, convert it to
`reST <http://en.wikipedia.org/wiki/ReStructuredText>`__ using
`pypandoc <https://pypi.python.org/pypi/pypandoc>`__ and store the
resulting reST in the ``long_description`` metadata field of your
distribution.
