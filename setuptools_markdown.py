import logging

import pypandoc


logging.basicConfig()
logger = logging.getLogger(__name__)


def long_description_markdown_filename(dist, attr, value):
    logger.info(
        'long_description_markdown_filename: '
        'dist = %r; attr = %r; value = %r',
        dist, attr, value)
    output = pypandoc.convert(value, 'rst')
    dist.metadata.long_description = output
