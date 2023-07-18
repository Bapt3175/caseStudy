import logging
import pandas as pd
import plotly.express as px
import plotly.io as pio
from checkers import check_date_format, is_float, check_lower_string
from fixers import fix_date

filename = r'curation-input\fake_dataset (2).csv'


def create_variable_checked_file(df):
    """
    Create a variable-checked file based on the provided DataFrame.
    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
    Returns:
        pandas.DataFrame: The modified DataFrame with error information.
    """
    logging.debug("create_variable_checked_file")
    df['Error_Column'] = ''

    for index, row in df.iterrows():
        if not check_date_format(row['Date of Birth']):
            df.at[index, 'Error_Column'] += 'Date of Birth|'

        if not is_float(row['PSA level']):
            df.at[index, 'Error_Column'] += 'PSA level|'

        if not check_lower_string(row['Smoking history']):
            df.at[index, 'Error_Column'] += 'Smoking history|'

    df['Error_Column'] = df['Error_Column'].str.rstrip('|')
    df['Error_Column'] = df['Error_Column'].str.strip().replace('', 'row ok')

    df.to_csv(r'curation-output\fake_dataset_checked.csv', index=False)
    return df


def create_insights(df):
    """
    Create insights from the provided DataFrame.
    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
    Returns:
        None. Displays a bar chart visualization.
    """
    logging.debug("create_insights")
    split_columns = df['Error_Column'].str.split('|', expand=True)
    num_columns = len(split_columns.columns)
    column_names = [f'Error_Column{i + 1}' for i in range(num_columns)]
    df[column_names] = split_columns
    fig = px.bar(df, x='Patient ID', y=column_names, barmode='stack')
    pio.show(fig)


def fix_dataframe(df):
    """
    Fixes the given DataFrame by applying the 'fix_date' function to the 'Date of Birth' and 'Date of Diagnosis' columns,
    and saves the modified DataFrame to a CSV file.
    Args:
        df (pandas.DataFrame): The DataFrame to be fixed.
    Returns:
        None
    """
    logging.debug("fix_dataframe")
    df['Date of Birth'] = df['Date of Birth'].apply(fix_date)
    df['Date of Diagnosis'] = df['date of diagnosis'].apply(fix_date)
    df.to_csv(r'curation-output\fake_dataset_fixed.csv', index=False)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    df = pd.read_csv(filename, delimiter=';')
    df_with_checked_errors = create_variable_checked_file(df)
    create_insights(df_with_checked_errors)
    fix_dataframe(df)




