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

    import runkeeper.user

    user = runkeeper.user.User("bnmrrs")
    activities = user.get_all_activities()

    total_distance = 0
    for activity in activities:
        total_distance += activity.get_distance()

    print total_distance
"""

import math
from datetime import date, timedelta

import simplejson as json
from BeautifulSoup import BeautifulSoup

import httpclient


class Activity:
    """Runkeeper Activity"""

    def __init__(self, activity_id):
        self.activity_id = activity_id

        self._load()

        self.distance = 0
        self.pace = 0
        self.avg_speed = 0

    def get_distance(self):
        """Gets the activity distance in kilometres"""
        if self.distance:
            return self.distance

        for i in range(len(self.points) - 1):
            start_latt = self.points[i]['latitude']
            start_long = self.points[i]['longitude']

            end_latt = self.points[i+1]['latitude']
            end_long = self.points[i+1]['longitude']

            self.distance += self._calc_distance(start_latt, start_long,
                                                 end_latt, end_long)

        return self.distance

    def get_pace(self):
        """Gets the average kilometre pace in milliseconds"""
        if self.pace:
            return self.pace

        duration = self.get_duration()
        distance = self.get_distance()

        self.pace = duration / distance
        return self.pace

    def get_avg_speed(self):
        """Gets the average speed in kilometeres per hour"""
        if self.avg_speed:
            return self.avg_speed

        duration = self.get_duration()
        distance = self.get_distance()

        self.avg_speed = (distance / duration) * 3600000 # milliseconds / hour
        return self.avg_speed

    def get_start_time(self):
        """Gets the start timestamp"""
        return self.start_time

    def get_end_time(self):
        """Gets the end timestand"""
        return self.end_time

    def get_duration(self):
        """Gets the duraton in milliseconds"""
        return self.duration

    def get_type(self):
        """Gets the activity type"""
        return self.type

    def get_as_json(self):
        """Gets a JSON representation of the activity"""
        data = {
            'activity_type': self.get_type(),
            'start_time': self.get_start_time(),
            'end_time': self.get_end_time(),
            'total_distance': self.get_distance(),
            'pace': str(timedelta(milliseconds=self.get_pace())),
            'average_speed': self.get_avg_speed(),
            'points': self.points
        }

        return json.dumps(data)

    def _load(self):
        activity_data = self._get_activity_data()

        self.start_time = activity_data[0]['timeMillis']
        self.end_time = activity_data[len(activity_data) - 1]['timeMillis']
        self.duration  = self.end_time - self.start_time

        self.type = self._get_activity_type()
        self.points = activity_data


    def _get_activity_data(self):
        activity_url = "http://runkeeper.com/ajax/activityInfo?tripId=%s" % self.activity_id
        activity_info = httpclient.get(activity_url)

        activity_info = json.loads(activity_info);
        return activity_info['points']

    def _get_activity_type(self):
        activity_url = "http://runkeeper.com/ui/activityHeader/%s" % self.activity_id
        activity_header = httpclient.get(activity_url)

        if activity_header.find('Running'):
          activity_type = 'Running'
        elif activity_header.find('Cycling'):
          activity_type = 'Cycling'
        elif activity_header.find('Mountain Biking'):
          activity_type = 'Mountain Biking'
        elif activity_header.find('Walking'):
          activity_type = 'Walking'
        elif activity_header.find('Hiking'):
          activity_type = 'Hiking'
        elif activity_header.find('Downhill Skiing'):
          activity_type = 'Downhill Skiiing'
        elif activity_header.find('Cross-Country Skiing'):
          activity_type = 'Cross-Country Skiiing'
        elif activity_header.find('Snowboarding'):
          activity_type = 'Snoboarding'
        elif activity_header.find('Skating'):
          activity_type = 'Skating'
        elif activity_header.find('Swimming'):
          activity_type = 'Swimming'
        elif activity_header.find('Wheelchair'):
          activity_type = 'Wheelchair'
        elif activity_header.find('Rowing'):
          activity_type = 'Rowing'
        elif activity_header.find('Elliptical'):
          activity_type = 'Elliptical'
        elif activity_header.find('Other'):
          activity_type = 'Other'
        else:
          activity_type = 'Unknown'

        return activity_type

    def _calc_distance(self, start_latt, start_long, end_latt, end_long):
        """
          Calculate distance in kilometers between two points
          Python implimentation thanks to Gee's Blog
          http://www.geesblog.com/2009/01/calculating-distance-between-latitude-longitude-pairs-in-python/
          Originally based on Aviation Formulary (http://williams.best.vwh.net/avform.htm)
        """

        nautical_miles_per_latitude = 60.00721
        nautical_miles_per_longitude = 60.10793

        rad = math.pi / 180.0
        km_per_nautical_mile = 1.852

        yDistance = (end_latt - start_latt) * nautical_miles_per_latitude
        xDistance = (math.cos(start_latt * rad) + math.cos(end_latt * rad)) * \
                    (end_long - start_long) * (nautical_miles_per_longitude / 2)

        distance = math.sqrt( yDistance**2 + xDistance**2 )

        return distance * km_per_nautical_mile
