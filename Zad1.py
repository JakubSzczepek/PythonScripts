import math

def euclidean_distance(A,B):
    """
    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
    """
    output = math.sqrt(((B[0]-A[0])**2)+((B[1]-A[1])**2))
    return output





