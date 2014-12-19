setuptools-markdown
===================

Use `Markdown <http://daringfireball.net/projects/markdown/>`__ for your
project description

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
