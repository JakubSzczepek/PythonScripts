def km_na_m(km: [float, int]) -> float:
    """
    >>> km_na_m(50)
    50000.0
    >>> km_na_m(-5)
    5000.0
    >>> km_na_m(0)
    0.0
    >>> km_na_m([1, 2, 3])
    Traceback (most recent call last):
    ...
    ValueError: invalid argument
    >>> km_na_m(15.6)
    15600.0
    """
    if not isinstance(km, (int, float)):
        raise ValueError('invalid argument')
    return float(abs(km * 1000))

