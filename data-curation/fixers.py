import pandas as pd
def fix_date(date_string):
    """
    Check and fix the date string by replacing multiple consecutive forward slashes with a single '/'.
    Args:
        date_string (str): The input date string.
    Returns:
        string date fixed.
    """
    if pd.notnull(date_string) and '/' in date_string:
        return '/'.join(date_string.split('/'))

