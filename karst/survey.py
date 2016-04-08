class Station:
    name = ''

    def __init__(self, name=''):
        self.name = name


class Shot:
    station_from = None
    station_to = None
    distance = None
    azimuth = None
    inclination = None
    left = None
    right = None
    up = None
    down = None

    def __init__(self, start, end, distance, azimuth, inclination, left=None,right=None, up=None, down=None):
        self.station_from = start
        self.station_to = end
        self.distance = distance
        self.azimuth = azimuth
        self.inclination = inclination
        self.left = left
        self.right = right
        self.up = up
        self.down = down
