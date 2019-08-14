import os
from setuptools import setup

version = '0.4.1'
long_description_filename = os.path.join(
    os.path.dirname(__file__), 'README.rst')
long_description = open(long_description_filename).read()

setup(
    name="setuptools-markdown",
    version=version,
    author="Marc Abramowitz",
    author_email="marc@marc-abramowitz.com",
    url="https://github.com/msabramo/setuptools-markdown",
    keywords='distutils setuptools markdown',
    description="[Deprecated] Use Markdown for your project description",
    long_description=long_description,
    license='MIT',
    install_requires=['pypandoc'],
    py_modules=['setuptools_markdown'],
    zip_safe=False,
    entry_points="""
        [distutils.setup_keywords]
        long_description_markdown_filename=setuptools_markdown:long_description_markdown_filename
        """
)
