# Copyright (c) 2014-2017 Marc Abramowitz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import inspect
import os
import logging

import m2r


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def long_description_markdown_filename(dist, attr, value):
    logger.debug(
        'long_description_markdown_filename: '
        'dist = %r; attr = %r; value = %r',
        dist, attr, value)
    frame = _get_code_object()
    setup_py_path = inspect.getsourcefile(frame)
    markdown_filename = os.path.join(os.path.dirname(setup_py_path), value)
    logger.debug('markdown_filename = %r', markdown_filename)
    output = m2r.parse_from_file(markdown_filename)
    lines = output.strip().splitlines()
    while len(lines) >= 2 and (not lines[1] or lines[1].isspace()):
        del lines[1]
    
    output = '\n'.join(lines)
    dist.metadata.long_description = output


def _get_code_object():
    frame = inspect.currentframe()

    while frame:
        code = frame.f_back.f_code
        if code.co_filename.endswith('setup.py'):
            return code
        frame = frame.f_back
