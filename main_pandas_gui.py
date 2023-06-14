"""Use the 'pandasgui' library to produce an EDA interface."""

import pandas as pd
from pandasgui import show


def main(file_name: str) -> None:
    """Run an Exploratory Data Analysis.

    Args:
        file_name (str): Name of the file to be loaded.

    Returns:
        None.
    """
    # First, load the '.csv' file containing the data
    data = pd.read_csv(
        filepath_or_buffer=f"{file_name}.csv",
        encoding="utf-8"
    )

    # Run the EDA
    show(data)
    return None


if __name__ == '__main__':
    print("\nLOAD DATA\n")

    main(file_name="defect_tags_2023_final")
