import pandas as pd
from scipy.stats import chi2_contingency


def chi2_table(df, col_list):
    """
    Usage: chi2_table(df, col_list)
    Returns: df + chi^2 column with chi^2(df) = value, p rounded to 5 decimals

    Function only works if columns in col_list are mutually exclusive (SUD_dx = True, SUD_dx = False)

    Meant to be used on count data after grouped with value_counts() or grouped_normal_counts() functions
    """

    df = df[col_list]
    new_df = pd.DataFrame()
    col_totals = df.sum().astype(int)
    for row in df.itertuples():
        a = []
        b = []
        for col in range(1, df.shape[1] + 1):
            a.append(row[col])
            b.append(col_totals[col - 1] - row[col])

        x2 = chi2_contingency([a, b])
        new_df.loc[row.Index, 'chi2'] = f"chi^2({x2[2]}) = {round(x2[0], 3)}, p={round(x2[1], 5)}"
    return df.merge(new_df, left_index=True, right_index=True)
