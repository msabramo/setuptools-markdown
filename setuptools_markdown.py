import inspect
import os
import logging

import pypandoc


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def long_description_filename(dist, attr, value):
    logger.debug(
        'long_description_filename: '
        'dist = %r; attr = %r; value = %r',
        dist, attr, value)
    filename = _get_filepath(value)
    output = pypandoc.convert(filename, 'rst')
    dist.metadata.long_description = output


def _get_filepath(filename):
    frame = _get_code_object()
    setup_py_path = inspect.getsourcefile(frame)
    filepath = os.path.join(os.path.dirname(setup_py_path), filename)
    logger.debug('filepath = %r', filepath)
    return filepath


def _get_code_object():
    frame = inspect.currentframe()

    while frame:
        code = frame.f_back.f_code
        if code.co_filename.endswith('setup.py'):
            return code
        frame = frame.f_back
