#!/usr/bin/env python
#
#  The MIT License
#
#  Copyright (c) 2009 Ben Morris
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.


import distutils.core
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

distutils.core.setup(
    name="runkeeper-api",
    version="0.1",
    packages = ["runkeeper"],
    author="Ben Morris",
    author_email="ben@bnmrrs.com",
    url="http://www.github.com/bnmrrs/runkeeper",
    license="http://www.opensource.org/licenses/mit-license.php",
    description="Runkeeper provides an API for the Runkeeper Webapp (http://runkeeper.com).",
)
