
def count_in_list(lst, str):
    """Count the occurrences of a string in a list.

    Args:
        lst (list): The list to search through.
        str (str): The string to count.

    Returns:
        int: The number of occurrences of the string in the list.
    """

    c: int = 0
    for e in lst:
        if e == str:
            c += 1
    return c
