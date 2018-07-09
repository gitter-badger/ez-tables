'''
TODO: Useful header info?
'''
def average(data):
    '''
    Determines the average (mean) of a list or series of values.

    Parameters
    ----------
    data : list
        The list of values to process.

    Returns
    -------
    mean : float
        The average (mean) of the range.

    Examples
    --------
    >>> data = {"a" : [1,2,3,4,5,6,7,8,9], "b" : [1,2,3,4]}
    >>> eztables.statistical.average(data["a"])
    5

    >>> eztables.statistical.average(data["b"])
    2.5
    '''
    elements = float(len(data))
    mean = sum([element/elements for element in data])
    return(mean)


def countif(data, criteria):
    '''
    Return the number of elements that meet a given criteria.

    Parameters
    ----------
    data : list
        The list of values to process.
    criteria : str
        The logical operation to test.

    Returns
    -------
    count : int
        The number of elements that met the criteria.

    Examples
    --------
    >>> data = {"a" : [1,2,3,4,5,6,7,8,9], "b" : [1,2,3,4]}
    >>> eztables.statistical.countif(data["a"], ">=5")
    3

    >>> eztables.statistical.countif(data["b"], ">=5")
    0
    '''

    count = sum([eval("element" + criteria) for element in data])
    return(count)


def median(data):
    '''
    Determines the median of a list or series of values.

    Parameters
    ----------
    data : list
        The list of values to process.

    Returns
    -------
    med : float
        The median of the range.

    Examples
    --------
    >>> data = {"a" : [1,2,3,4,5,6,7,8,9], "b" : [1,2,3,4]}
    >>> eztables.statistical.median(data["a"])
    5

    >>> eztables.statistical.median(data["b"])
    2.5
    '''
    elements = len(data)
    sort_list = sorted(data)
    if elements == 0:
        med = None
    elif (elements % 2) != 0:
        med = sort_list[(elements-1)/2]
    else:
        print("odd")
        med = (sort_list[elements/2-1] + sort_list[elements/2])/2.0
    return(med)

