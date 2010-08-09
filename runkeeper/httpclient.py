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


""" Runkeeper Python API

The Runkeeper Python API is used to interact with
Runkeeper (http://runkeeper.com).  Runkeeper does not provide an official API
so BeautifulSoup is used to scrape pages.

Here is the basic example of getting total distance for a user

    from runkeeper import User

    user = User("bnmrrs")
    activities = user.get_all_activities()

    total_distance = 0
    for activity in activities:
        total_distance += activity.get_distance()

    print total_distance
"""


import urllib


def get(url):
    """Used to make very basic HTTP requests.  Currently no error handling.
    Takes a URL as it's only argument and returns the resulting page
    """
    f = urllib.urlopen(url)
    s = f.read()
    f.close()

    return s

