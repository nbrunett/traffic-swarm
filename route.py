import numpy as np
import urllib2

class route:
    def __init__(self, sLat, sLon, eLat, eLon):
        self.sLat = sLat
        self.sLon = sLon
        self.eLat = eLat
        self.eLon = eLon
        self.URL = 'http://www.yournavigation.org/api/1.0/gosmore.php?'+ \
                   'flat='+str(self.sLat)+'&'+ \
                   'flon='+str(self.sLon)+'&'+ \
                   'tlat='+str(self.eLat)+'&'+ \
                   'tlon='+str(self.eLon)+'&'+ \
                   'v=motorcar&'+ \
                   'fast=1&'+ \
                   'layer=mapnik&'+ \
                   'format=kml&'+ \
                   'geometry=1&'+ \
                   'distance=v&'+ \
                   'instructions=0&'+ \
                   'lang=en_US'

        response = urllib2.urlopen(self.URL)
        data = response.read()
        response.close()
        data = data.split('\n')
        self.coords = list()
        for line in data:
            if '<' not in line and line != '':
                self.coords.append(line.strip('\n').split(','))
        self.coords = np.array(self.coords, dtype=float)
