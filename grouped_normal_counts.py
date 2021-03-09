import pandas as pd


def gnc(df, col, group=None):
    """
    Usage: gnc(df, col, group=None)
    Returns: df grouped by "group", value_counts for col, count and normalized

    If group is left blank, will return df value counts of col, count and normalized

    """

    if (group is not None) and (group not in df.columns):
        return f'grouping column {group} not found in columns of dataframe'

    if col not in df.columns:
        return f'analysis column {col} not found in columns of dataframe'

    new_df = pd.DataFrame()

    if group is None:
        df_cnt = df[col].value_counts(dropna=False).sort_index()
        df_pct = df[col].value_counts(dropna=False, normalize=True).sort_index()
        new_df[f'count'] = df_cnt
        new_df[f'percent'] = df_pct
    else:
        group_df_cnt = df.groupby(group)[col].value_counts(dropna=False).sort_index()
        group_df_pct = df.groupby(group)[col].value_counts(dropna=False, normalize=True).sort_index()
        levels = group_df_cnt.index.get_level_values(0).unique()

        for idx_lvl in levels:
            new_df[f'count_{group}_{idx_lvl}'] = group_df_cnt.loc[idx_lvl]
            new_df[f'percent_{group}_{idx_lvl}'] = group_df_pct.loc[idx_lvl]

    return new_df
