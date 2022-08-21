import sqlite3
import json
import requests
from Back.DAO import credentials

api_key = credentials.API_KEY
url_to_analyze = 'https://www.voici.fr'


# Insert data from Google Pagespeed Insight API
# into the table metrics_cumulative_layout_shift_score
def insert_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score():
    conn = sqlite3.connect(
        "Back\\DAO\\database.db"
    )

    category = 'performance'

    endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
               + "&key=" + api_key \
               + "&category=" + category

    response = requests.get(endpoint)

    cumulative_layout_shift_score_object = json.loads(response.text)["loadingExperience"]["metrics"][
        "CUMULATIVE_LAYOUT_SHIFT_SCORE"]

    # dataset
    analysis_utc_timestamp = json.loads(response.text)["analysisUTCTimestamp"]
    percentile = cumulative_layout_shift_score_object["percentile"]
    proportion_for_distribution_min0_and_max10 = cumulative_layout_shift_score_object["distributions"][0][
        "proportion"]
    proportion_for_distribution_min10_and_max25 = cumulative_layout_shift_score_object["distributions"][1][
        "proportion"]
    proportion_for_distribution_min25 = cumulative_layout_shift_score_object["distributions"][2][
        "proportion"]

    static_dataset = {
        "analysis_utc_timestamp": analysis_utc_timestamp,
        "percentile": percentile,
        "proportion_for_distribution_min0_and_max10": proportion_for_distribution_min0_and_max10,
        "proportion_for_distribution_min10_and_max25": proportion_for_distribution_min10_and_max25,
        "proportion_for_distribution_min25": proportion_for_distribution_min25
    }

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO metrics_cumulative_layout_shift_score 
        (analysis_utc_timestamp, percentile, proportion_for_distribution_min0_and_max10, 
        proportion_for_distribution_min10_and_max25, proportion_for_distribution_min25) 
        VALUES(?, ?, ?, ?, ?)
        """,
        (
            static_dataset.get('analysis_utc_timestamp'),
            static_dataset.get('percentile'),
            static_dataset.get('proportion_for_distribution_min0_and_max10'),
            static_dataset.get('proportion_for_distribution_min10_and_max25'),
            static_dataset.get('proportion_for_distribution_min25')
        )
    )

    conn.commit()

    conn.close()

    return "Data inserted into table metrics_cumulative_layout_shift_score : " + str(static_dataset)
