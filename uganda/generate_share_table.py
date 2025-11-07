#!/usr/bin/env python3
# -*- coding: utf-8 -*-
------------------------------------------------------------------------------

"""
===============================================================================
Project: Uganda Securities Exchange — Share Accumulation Cost Table Generator
File: generate_share_table.py
Source: https://github.com/ivanshim/ivanshim.github.io
Raw: https://raw.githubusercontent.com/ivanshim/ivanshim.github.io/main/uganda/generate_share_table.py

Description:
    This Python script generates a modular, neatly formatted share purchase
    cost table for listed companies on the Uganda Securities Exchange (USE).

    It calculates:
        • Base Value (price × shares)
        • Brokerage Commission (e.g. 2.1%)
        • Total Cost per purchase block
        • Cumulative Shares (running total)

    Features:
        - Automatic wrap-around share counts (e.g. 900k → 910k → … → 990k → 900k)
        - Dynamically computed TOTALS row
        - Optional comma formatting for readability
        - Fully generic column handling (no hard-coded labels)
        - Output as a pandas DataFrame, printable as Markdown or exportable to Excel

    Example:
        >>> from generate_share_table import generate_share_table
        >>> df = generate_share_table(price_per_share=5.0, total_target_shares=21_000_000)
        >>> print(df.to_markdown(index=False))

Authors:
    Ivan Shim — https://github.com/ivanshim
    GPT-5 (OpenAI ChatGPT)
License:
    MIT License
Version:
    1.0
Date:
    2025-11-06
===============================================================================
"""

import pandas as pd


def generate_share_table(
    start_shares=900_000,
    wrap_interval=100_000,   # wraps 900k→910k→…→990k→900k
    increment=10_000,
    price_per_share=5.0,
    commission_rate=0.021,
    total_target_shares=21_000_000,
    format_numbers=True      # toggle comma-formatting on/off
):
    """
    Generate a share purchase cost table with wrap-around share counts.

    Parameters
    ----------
    start_shares : int
        Starting share count for each row (default 900,000)
    wrap_interval : int
        Interval size before share count wraps around (default 100,000 → wraps at 990,000)
    increment : int
        Step size between rows (default 10,000)
    price_per_share : float
        Current market price per share (default UGX 5.0)
    commission_rate : float
        Brokerage fee rate (default 0.021 = 2.1%)
    total_target_shares : int
        Target total cumulative shares (e.g. 21,000,000 for ~1% ownership)
    format_numbers : bool
        If True, display numbers with thousands separators (commas).
        Keeps math numeric internally.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with:
        - Shares
        - Base Value (UGX)
        - +Commission
        - Total Cost (UGX)
        - Cumulative Shares
        Plus a final TOTALS row (generated dynamically).
    """

    # 1) Declare headers for readability
    columns = [
        "Shares",
        f"Base Value (UGX {price_per_share} × shares)",
        f"+{commission_rate*100:.1f}% Commission",
        "Total Cost (UGX)",
        "Cumulative Shares"
    ]

    # 2) Generate rows numerically
    rows = []
    cumulative_shares = 0
    shares = start_shares
    while cumulative_shares < total_target_shares:
        base_value = shares * price_per_share
        commission = base_value * commission_rate
        total_cost = base_value + commission
        cumulative_shares += shares

        rows.append([
            shares,
            round(base_value),
            round(commission),
            round(total_cost),
            cumulative_shares
        ])

        # modular wrap
        shares = start_shares + ((shares + increment - start_shares) % wrap_interval)

    # 3) Create DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # 4) Add generic TOTALS row
    totals = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            totals[col] = df[col].sum()
        else:
            totals[col] = "TOTALS"
    df = pd.concat([df, pd.DataFrame([totals])], ignore_index=True)

    # 5) Optional comma-formatting for numeric-looking columns
    if format_numbers:
        def fmt(x):
            return f"{x:,}" if isinstance(x, (int, float)) else x
        for col in df.columns:
            if df[col].apply(lambda v: isinstance(v, (int, float))).any():
                df[col] = df[col].map(fmt)

    return df


"""
# Example 1 — NIC Holdings Limited (USE:NIC)
# ------------------------------------------------------------------------
nic_df = generate_share_table(
    start_shares=900_000,
    wrap_interval=100_000,
    increment=10_000,
    price_per_share=5.0,
    commission_rate=0.021,
    total_target_shares=21_000_000,
    format_numbers=True
)
print(nic_df.to_markdown(index=False))
# nic_df.to_excel("NIC_1percent_cost_table.xlsx", index=False)
"""


"""
# Example 2 — Uganda Clays Limited (USE:UCL)
# ------------------------------------------------------------------------
ucl_df = generate_share_table(
    start_shares=900_000,
    wrap_interval=100_000,
    increment=10_000,
    price_per_share=6.5,
    commission_rate=0.021,
    total_target_shares=9_000_000,
    format_numbers=True
)
print(ucl_df.to_markdown(index=False))
# ucl_df.to_excel("UCL_1percent_cost_table.xlsx", index=False)
"""
