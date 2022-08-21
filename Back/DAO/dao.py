import sqlite3


# ok
# Fetch all rows from the table 'metrics_cumulative_layout_shift_score'
def fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score():
    conn = sqlite3.connect(
        "Back\\DAO\\database.db"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM metrics_cumulative_layout_shift_score")

    rows = cur.fetchall()

    conn.close()

    return rows


# ok
# Fetch all rows from the table 'metrics_cumulative_layout_shift_score'
def fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min0_and_max10():
    conn = sqlite3.connect(
        "Back\\DAO\\database.db"
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT percentile, proportion_for_distribution_min0_and_max10 
        FROM metrics_cumulative_layout_shift_score
        """
    )

    rows = cur.fetchall()

    conn.close()

    array_percentile = []

    array_proportion_for_distribution_min0_and_max10 = []

    for row in rows:
        array_percentile.append(int(row[0]))
        array_proportion_for_distribution_min0_and_max10.append(float(row[1]))

    return [array_percentile, array_proportion_for_distribution_min0_and_max10]


# ok
# Fetch all rows from the table 'metrics_cumulative_layout_shift_score'
def fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min10_and_max25():
    conn = sqlite3.connect(
        "Back\\DAO\\database.db"
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT percentile, proportion_for_distribution_min10_and_max25
        FROM metrics_cumulative_layout_shift_score
        """
    )

    rows = cur.fetchall()

    conn.close()

    array_percentile = []

    array_proportion_for_distribution_min10_and_max25 = []

    for row in rows:
        array_percentile.append(int(row[0]))
        array_proportion_for_distribution_min10_and_max25.append(float(row[1]))

    return [array_percentile, array_proportion_for_distribution_min10_and_max25]


# ok
# Fetch all rows from the table 'metrics_cumulative_layout_shift_score'
def fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min25():
    conn = sqlite3.connect(
        "Back\\DAO\\database.db"
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT percentile, proportion_for_distribution_min25
        FROM metrics_cumulative_layout_shift_score
        """
    )

    rows = cur.fetchall()

    conn.close()

    array_percentile = []

    array_proportion_for_distribution_min25 = []

    for row in rows:
        array_percentile.append(int(row[0]))
        array_proportion_for_distribution_min25.append(float(row[1]))

    return [array_percentile, array_proportion_for_distribution_min25]
