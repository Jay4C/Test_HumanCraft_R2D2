# Test_HumanCraft_R2D2
This repository contains a technical test for a software that analyzes an URL (https://www.voici.fr) by using Google 
Pagespeed Insight API.

The code is written in Python.

The program shows several analysis for an URL (https://www.voici.fr) at a specific date by using the libraries 
Chart.js, Bootstrap for the front-end.

The back-end of the application is developped with Python 3, Framework Flask, Sqlite3.

Steps :
- Install 'python' on your machine.
- Clone this repository on your machine.
- Go to the main folder of this repository containing the file 'main.py'.
- Open the Terminal (CMD).
- Run the following command : 'pip install Flask' into the Terminal.
- Run the following command : 'pip install pysqlite3' into the Terminal.
- Run the following command : 'pip install requests' into the Terminal.
- Run the following command : 'pip install python-crontab' into the Terminal.
- Run the following command : 'flask run' into the Terminal.
- Click on the URL server (http://127.0.0.1:5000) to see the table of one metric into your web browser.
- Open the URL (http://127.0.0.1:5000/charts_from_the_table_metrics_cumulative_layout_shift_score) to the charts of one 
metric into your web browser.
- Run the unit test (Back.Test.unit_tests.UnitTestsForTestingCronJobs
.test_get_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score) 
to schedule a cron job for getting metrics from Google Pagespeed Insight API every minute 
for the URL (https://www.voici.fr). Do not forget to specify your API_KEY into the file "credentials.py" from Back.DAO 
package.
