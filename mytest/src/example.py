"""
The `reverse` function takes a string as input and returns the reversed version of that string,
handling the case where the input string is `None`.

:param string: The `string` parameter is a string input that you want to reverse using the `reverse`
function. If the input string is `None`, the function will return `None`
:return: The `reverse` function returns the reversed version of the input string. If the input
string is `None`, the function will return `None`.

>>> reverse('hello')
'olleh'
>>> reverse(None)

doctest
python -i example.py
python example.py -v
"""

def reverse(string):
    """
    The function reverses a given string.
    
    :param string: The `reverse` function takes a string as input and returns the reversed version of
    that string. If the input string is `None`, the function will return `None`
    :return: The function `reverse` takes a string as input and returns the reversed version of the
    string. If the input string is `None`, the function will return `None`.

    >>> reverse('')
    ''
    >>> reverse('Something')
    'gnihtemoS'
    """
    if string is None:
        return None
    return string[::-1]

# это нужно для запуска
if __name__ == '__main__':
    import doctest
    doctest.testmod()