from setuptools import setup

version = '0.0dev'

setup(
    name="setuptools-markdown",
    version=version,
    author="Marc Abramowitz",
    author_email="marc@marc-abramowitz.com",
    url="https://github.com/msabramo/setuptools-markdown",
    keywords='distutils setuptools markdown',
    description="Use Markdown for your project description",
    license='MIT',
    py_modules=['setuptools_markdown'],
    long_description_markdown_filename='README.md',
    entry_points="""
        [distutils.setup_keywords]
        long_description_markdown_filename=setuptools_markdown:long_description_markdown_filename
        """
)
