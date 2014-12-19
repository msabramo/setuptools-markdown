# setuptools-markdown

Use [Markdown][] for your project description

# Use

```python
setup(
    ...
    long_description_markdown_filename='README.md',
    ...
)
```

The plugin will read the specified file, convert it to reST using
[pypandoc][] and store the resulting [reST][] in the `long_description`
metadata field of your distribution.

[Markdown]: http://daringfireball.net/projects/markdown/
[pypandoc]: https://pypi.python.org/pypi/pypandoc
[reST]: http://en.wikipedia.org/wiki/ReStructuredText
