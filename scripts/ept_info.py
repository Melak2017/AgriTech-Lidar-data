import json
#from lidardataextractor import schema
#import pyproj
#from pyproj import CRS
#from lidardataextractor.schema import Schema

class Info(object):
    """ """
    def __init__(self, data) -> None:
        self.data = json.loads(data)

    def length(self) -> int:
        """ """
        return int(self.data['points'])

    def get_span(self) -> int:
        """ """
        return int(self.data['span'])
    span = property(get_span)

    def get_version(self) -> str:
        """ """
        return self.data['version']
    version = property(get_version)

    def get_bounds(self) -> list:
        """ """
        return self.data['bounds']
    bounds = property(get_bounds)

    def get_conforming(self) -> list:
        """ """
        return self.data['boundsConforming']
    conforming = property(get_conforming)

    def get_datatype(self) -> str:
        """ """
        return self.data['dataType']
    datatype = property(get_datatype)

    def get_hierarchytype(self) -> str:
        """ """
        return self.data['hierarchyType']
    hierarchytype = property(get_hierarchytype)

    