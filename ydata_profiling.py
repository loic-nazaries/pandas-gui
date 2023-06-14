"""Use the 'ydata-profiling' library to produce an EDA interface."""

import pandas as pd
from ydata_profiling import ProfileReport


def main(file_name: str) -> None:
    """Run an Exploratory Data Analysis.

    Args:
        file_name (str): Name of the file to be loaded.

    Returns:
        None. A .html file is generated.
    """
    # First, load the '.csv' file containing the data
    data = pd.read_csv(
        filepath_or_buffer=f"{file_name}.csv",
        encoding="utf-8"
    )

    # Run the EDA
    profile = ProfileReport(
        data,
        title="Pandas Profiling Report",
        # config_file="my_config.yml",  # not working
        correlations={
            "auto": {"calculate": True},
            "pearson": {"calculate": True},
            "spearman": {"calculate": True},
            "kendall": {"calculate": True},
            "phi_k": {"calculate": True},
            "cramers": {"calculate": True},
        },
        progress_bar=True,
        explorative=True,
    )
    # profile.config.correlations.phi_k.calculate = True
    profile.to_file("rockwool_eda_report.html")
    return None


if __name__ == '__main__':
    print("\nLOAD DATA\n")

    main(file_name="defect_tags_2023_final")
