import pandas as pd
from datetime import datetime


def check_date_format(date_string):
    """
    Check if the given date string has a valid format of "%d/%m/%Y".
    Args:
        date_string (str): The date string to be checked.
    Returns:
        bool: True if the date string has a valid format, False otherwise.
    """
    if pd.notnull(date_string):
        try:
            datetime.strptime(date_string, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    else:
        return False


def is_float(float_string):
    """
        Check if the given string can be converted to a float.
        Args:
            float_string (str): The string to be checked.
        Returns:
            bool: True if the string can be converted to a float, False otherwise.
    """
    return True if isinstance(float_string, str) and float_string.replace('.', '', 1).isdigit() else False


def check_lower_string(string):
    """
    Check if the given lowercase string matches the specified values.
    Args:
        string (str): The lowercase string to be checked.
    Returns:
        bool: True if the string matches 'heavy' or 'former', False otherwise.
    """
    return True if string.lower() in ["heavy", "former"] else False
