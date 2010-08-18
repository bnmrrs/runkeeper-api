# Unofficial Runkeeper-API

## Overview
The Runkeeper-API is used to interact with Runkeeper (http://runkeeper.com)
Runkeeper does provide an official API so BeautifulSoup is used to
scrae pages.  Currently this package can only be used for reading.

## Installation

    $ sudo python setup.py install

## Usage

### Get distance
A simple example for getting the total distance a user has covered

<pre><code>from runkeeper import User
	
user = User("bnmrrs")
activities = user.get_all_activities()

total_distance = 0
for activity in activities:
	total_distance += activity.get_distance()

print "%dkm" % total_distance</code></pre>

## Dependencies
[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)  
[simplejson](http://www.undefined.org/python/)

## License
This package is licensed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).