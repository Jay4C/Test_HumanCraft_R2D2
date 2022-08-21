import unittest
import requests
import json
import sqlite3
from Back.DAO import dao
from Back.Service import service
from Back.DAO import credentials
from crontab import CronTab

api_key = credentials.API_KEY
url_to_analyze = 'https://www.voici.fr'


class UnitTestsForTestingGooglePageSpeedInsightAPI(unittest.TestCase):
    # ok
    # https://developers.google.com/speed/docs/insights/v5/get-started#APIKey
    def test_simple_runpagespeed(self):
        print('test_simple_runpagespeed')

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key

        response = requests.get(endpoint)

        print(response.text)

    # ok
    # https://developers.google.com/speed/docs/insights/v5/reference/pagespeedapi/runpagespeed?apix_params=%7B%22url%22%3A%22https%3A%2F%2Fwww.voici.fr%22%7D#http-request
    def test_runpagespeed_with_a_specific_category(self):
        print('test_runpagespeed_with_a_specific_category')

        category = 'performance'

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key \
                   + "&category=" + category

        response = requests.get(endpoint)

        print(response.text)

    # ok
    # https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed#response-body
    def test_runpagespeed_with_a_specific_category_for_retrieving_analysisUTCTimestamp(self):
        print('test_runpagespeed_with_a_specific_category_for_retrieving_analysisUTCTimestamp')

        category = 'performance'

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key \
                   + "&category=" + category

        response = requests.get(endpoint)

        analysis_utc_timestamp = json.loads(response.text)["analysisUTCTimestamp"]

        print(analysis_utc_timestamp)

    # ok
    # https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed#PagespeedApiLoadingExperienceV5
    def test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object(self):
        print('test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object')

        category = 'performance'

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key \
                   + "&category=" + category

        response = requests.get(endpoint)

        loading_experience_object = json.loads(response.text)["loadingExperience"]

        pretty_object = json.dumps(loading_experience_object, indent=4)

        print(pretty_object)

    # ok
    # https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed#PagespeedApiLoadingExperienceV5
    def test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_CUMULATIVE_LAYOUT_SHIFT_SCORE(self):
        print('test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_CUMULATIVE_LAYOUT_SHIFT_SCORE')

        category = 'performance'

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key \
                   + "&category=" + category

        response = requests.get(endpoint)

        cumulative_layout_shift_score_object = json.loads(response.text)["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]

        pretty_object = json.dumps(cumulative_layout_shift_score_object, indent=4)

        print(pretty_object)

    # ok
    # https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed#PagespeedApiLoadingExperienceV5
    def test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_FIRST_CONTENTFUL_PAINT_MS(self):
        print('test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_CUMULATIVE_LAYOUT_SHIFT_SCORE')

        category = 'performance'

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key \
                   + "&category=" + category

        response = requests.get(endpoint)

        first_contentful_paint_ms_object = json.loads(response.text)["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]

        pretty_object = json.dumps(first_contentful_paint_ms_object, indent=4)

        print(pretty_object)

    # ok
    # https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed#PagespeedApiLoadingExperienceV5
    def test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_FIRST_INPUT_DELAY_MS(self):
        print('test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_FIRST_INPUT_DELAY_MS')

        category = 'performance'

        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url_to_analyze \
                   + "&key=" + api_key \
                   + "&category=" + category

        response = requests.get(endpoint)

        first_input_delay_ms_object = json.loads(response.text)["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]

        pretty_object = json.dumps(first_input_delay_ms_object, indent=4)

        print(pretty_object)

    # ok
    # https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed#PagespeedApiLoadingExperienceV5
    def test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_CUMULATIVE_LAYOUT_SHIFT_SCORE_dataset(self):
        print('test_runpagespeed_with_a_specific_category_for_retrieving_loadingExperience_object_for_accessing_CUMULATIVE_LAYOUT_SHIFT_SCORE_dataset')

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

        pretty_object = json.dumps(
            {
                "analysis_utc_timestamp": analysis_utc_timestamp,
                "percentile": percentile,
                "proportion_for_distribution_min0_and_max10": proportion_for_distribution_min0_and_max10,
                "proportion_for_distribution_min10_and_max25": proportion_for_distribution_min10_and_max25,
                "proportion_for_distribution_min25": proportion_for_distribution_min25
            }, indent=4)

        print(pretty_object)


class UnitTestsForTestingDatabaseSqlite(unittest.TestCase):
    # ok
    def test_create_database(self):
        print('test_create_database')

        conn = sqlite3.connect("..\\DAO\\database.db")
        print("Opened database successfully")
        conn.close()

    # ok
    def test_list_of_tables(self):
        print('test_list_of_tables')

        # Making a connection between sqlite3
        # database and Python Program
        sqlite_connection = sqlite3.connect('..\\DAO\\database.db')

        try:
            # If sqlite3 makes a connection with python
            # program then it will print "Connected to SQLite"
            # Otherwise it will show errors
            print("Connected to SQLite")

            # Getting all tables from sqlite_master
            sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

            # Creating cursor object using connection object
            cursor = sqlite_connection.cursor()

            # executing our sql query
            cursor.execute(sql_query)
            print("List of tables\n")

            # printing all tables list
            print(cursor.fetchall())

        except sqlite3.Error as error:
            print("Failed to execute the above query", error)

        finally:
            # Inside Finally Block, If connection is
            # open, we need to close it
            if sqlite_connection:
                # using close() method, we will close
                # the connection
                sqlite_connection.close()

                # After closing connection object, we
                # will print "the sqlite connection is
                # closed"
                print("the sqlite connection is closed")

    # ok
    def test_create_table_metrics_cumulative_layout_shift_score(self):
        print('test_create_table_metrics_cumulative_layout_shift_score')

        conn = sqlite3.connect("..\\DAO\\database.db")
        print("Opened database successfully")

        conn.execute(
            '''
            CREATE TABLE metrics_cumulative_layout_shift_score 
            (analysis_utc_timestamp TEXT, 
            percentile TEXT, 
            proportion_for_distribution_min0_and_max10 TEXT, 
            proportion_for_distribution_min10_and_max25 TEXT,
            proportion_for_distribution_min25 TEXT)
            '''
        )
        print('Table created successfully')

        conn.close()

    # ok
    def test_insert_data_into_table_metrics_cumulative_layout_shift_score_from_static_dataset(self):
        print('test_insert_data_into_table_metrics_cumulative_layout_shift_score_from_static_dataset')

        conn = sqlite3.connect("..\\DAO\\database.db")
        print("Opened database successfully")

        static_dataset = {
            "analysis_utc_timestamp": "2022-08-21T12:11:33.958Z",
            "percentile": 3,
            "proportion_for_distribution_min0_and_max10": 0.865021770682148,
            "proportion_for_distribution_min10_and_max25": 0.11030478955007259,
            "proportion_for_distribution_min25": 0.024673439767779397
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

        print("Data inserted into table metrics_cumulative_layout_shift_score")

        conn.close()

    # ok
    def test_insert_data_into_table_metrics_cumulative_layout_shift_score_from_api(self):
        print('test_insert_data_into_table_metrics_cumulative_layout_shift_score_from_api')

        conn = sqlite3.connect("..\\DAO\\database.db")
        print("Opened database successfully")

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

        print("Data inserted into table metrics_cumulative_layout_shift_score")

        conn.close()

    # ok
    def test_select_all_rows_from_table_metrics_cumulative_layout_shift_score(self):
        print("test_select_all_rows_from_table_metrics_cumulative_layout_shift_score")

        conn = sqlite3.connect("..\\DAO\\database.db")
        print("Opened database successfully")

        cur = conn.cursor()
        cur.execute("SELECT * FROM metrics_cumulative_layout_shift_score")

        rows = cur.fetchall()

        pretty_object = json.dumps(rows, indent=4)

        print(pretty_object)

        conn.close()


class UnitTestsForTestingDAOPackage(unittest.TestCase):
    # ok
    def test_select_all_rows_from_table_metrics_cumulative_layout_shift_score(self):
        print('test_select_all_rows_from_table_metrics_cumulative_layout_shift_score')

        data = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score()

        print(data)

    # ok
    def test_select_all_rows_from_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min0_and_max10(self):
        print('test_select_all_rows_from_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min0_and_max10')

        data = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min0_and_max10()

        print(data)

    # ok
    def test_select_all_rows_from_table_metrics_cumulative_layout_shift_score_proportion_for_metrics_distribution_min10_and_max25(self):
        print('test_select_all_rows_from_table_metrics_cumulative_layout_shift_score_proportion_for_distribution_min10_and_max25')

        data = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min10_and_max25()

        print(data)

    # ok
    def test_select_all_rows_from_table_metrics_cumulative_layout_shift_score_for_metrics_proportion_for_distribution_min25(self):
        print('test_select_all_rows_from_table_metrics_cumulative_layout_shift_score_for_metrics_proportion_for_distribution_min25')

        data = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min25()

        print(data)


class UnitTestsForTestingServicePackage(unittest.TestCase):
    # ok
    def test_insert_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score(self):
        print('test_insert_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score')

        print(service.insert_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score())


class UnitTestsForTestingAppFlask(unittest.TestCase):
    # ok
    def test_insert_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score(self):
        print('test_insert_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score')

        endpoint = 'http://127.0.0.1:5000/insert_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score'

        response = requests.get(endpoint)

        print(response.text)


class UnitTestsForTestingCronJobs(unittest.TestCase):
    # ok
    def test_get_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score(self):
        print('test_get_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score')

        cron = CronTab(tab="""
          * * * * * python get_data.py
        """)
        job = cron.new(command='python get_data.py')
        job.minute.every(1)
        cron.write()
        print('cron.write() was just executed')


if __name__ == '__main__':
    unittest.main()
