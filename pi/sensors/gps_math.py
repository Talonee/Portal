import math as m

def convertLatLon(coords):
    lat = m.radians(coords[0])
    lon = m.radians(coords[1])
    return lat, lon

def calcX(coords, R = 6371000):
    lat,lon = convertLatLon(coords)
    x = R * m.cos(lat) * m.cos(lon)
    return x
    
def calcY(coords, R = 6371000):
    lat,lon = convertLatLon(coords)
    y = R * m.cos(lat) * m.sin(lon)
    return y

def calcZ(coords, R = 6371000):
    lat,lon = convertLatLon(coords)
    z = R *m.sin(lat)
    return z

def LanLonToCart(coords, XY = True):
    if XY:
        return [calcX(coords), calcY(coords)] #2D
    else:
        return [calcX(coords), calcY(coords), calcZ(coords)] #3D