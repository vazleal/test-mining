import os
import pandas as pd


def load_from_csv(filename: str):
    """Load a CSV file from the datas directory if it exists.

    Parameters
    ----------
    filename : str
        Name of the CSV file inside the datas directory.

    Returns
    -------
    pandas.DataFrame | None
        The DataFrame loaded from the CSV or None if the file does not exist.
    """
    path = os.path.join('datas', filename)
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

