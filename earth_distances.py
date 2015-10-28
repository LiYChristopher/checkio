'''
IN - Two pairs of Lat./Long. coordinates (First --> Second)
OUT- distance between the two points in kilometers

"The concepts presented in this mission are the exact sorts of concepts used in navigational software, 
enabling a ship or plane to understand where it is, where it must go and how far it has gone. 
Along the same vein, Global Positioning Satellites use similar principles to provide 
pinpoint accurate locations to GPS receivers for use in navigation."

Excerpt taken from CheckIO mission page. Visit http://www.checkio.org/mission/earth-distances/ for more information.
'''
import re
from math import radians
from math import pi, sqrt
from math import sin, cos, atan2
R = 6371
​
def clean_input(input_string):
    ''' Takes pairs of coordinates (first or second),
    and returns a namedtuple-object to be used in the
    main function. '''
​
    format = re.sub(r'(,\s)|\,', " ",input_string, re.I)
    pair_points = format.encode('utf-8').split(' ')
    clean = lambda point: (re.search(r'([0-9]*)°([0-9]*)′([0-9]*)\″([A-Z]*)',
                                    point, re.I)).groups()
    result = [clean(point) for point in pair_points]
    return result
​
def convert_to_radians(deg, min, sec, dir):
    ''' Calculates total degrees of a coordinate (Lat or Long),
    then converts it into radians.'''
    
    total_degrees = float(deg) + (float(min)/60) + (float(sec)/60**2)
    if dir == "S" or dir == "W":
        total_degrees *= -1
    total_radians = radians(total_degrees)
    return total_radians
    
def distance(first, second):
    ''' Calculates shortest-distance over the Earth's surface 
    based on haversine formula:
    a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    '''
    
    lat1, long1 = clean_input(first)
    lat2, long2 = clean_input(second)
​
    phi1 = convert_to_radians(*lat1)
    phi2 = convert_to_radians(*lat2)
    d1 = convert_to_radians(*long1)
    d2 = convert_to_radians(*long2)
    
    d_phi = phi2 - phi1
    d_lambda = d2 - d1
    
    a = sin(d_phi/2)**2 +\
        cos(phi1) * cos(phi2) *\
        sin(d_lambda/2)**2 
        
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    distance = R * c
    return distance
