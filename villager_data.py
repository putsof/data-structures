"""Functions to parse a file containing villager data."""

import csv

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """ 
    """ 
    This is what the data looks like when you call (all_data[0])
    ('Cyrano', 'Anteater', 'Cranky', 'Education', "Don't punch your nose to spite your face.")
    
    and this is what all_data[0][0] looks like
    Cyrano
    """

    species = set()
    data = all_data(filename) # use the all_data function to process the csv for us
    for row_num in range(len(data)): # we need to iterate over the entire length of list with each row number
        species.add(data[row_num][1]) # add row number to the set

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    with open(filename, newline='') as villagers_info:
        villagers_info_reader = csv.reader(villagers_info)
        #all_data = list(tuple(row) for row in villagers_info_reader)
        for row in villagers_info_reader: #at this point, each row is a list
            # inside each list is one string
            # we need to split the string up by |
            # then we need it to convert it to a tuple
            row = tuple(row[0].split('|')) # this line splits the list up by the delimiter and then converts it to a tuple
            all_data.append(row) # now that the data is in the form we want, we append it to the all_data list

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code


# print(all_data('villagers.csv'))
print(all_species('villagers.csv'))
