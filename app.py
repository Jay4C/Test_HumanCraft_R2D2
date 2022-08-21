from flask import Flask, render_template, request
from Back.Service import service
from Back.DAO import dao

app = Flask(__name__, template_folder='Front\\templates')


@app.route('/')
def list_all_data_from_the_table_metrics_cumulative_layout_shift_score():
    rows = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score()

    return render_template("list_all_data.html", rows=rows)


@app.route('/charts_from_the_table_metrics_cumulative_layout_shift_score')
def charts_from_the_table_metrics_cumulative_layout_shift_score():
    rows1 = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min0_and_max10()

    rows2 = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min10_and_max25()

    rows3 = dao.fetch_all_rows_from_the_table_metrics_cumulative_layout_shift_score_for_metric_proportion_for_distribution_min25()

    return render_template(
        "charts_analysis_performance.html",
        rows1=rows1,
        rows2=rows2,
        rows3=rows3
    )


@app.route("/insert_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score")
def insert_new_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score():
    return service.insert_data_from_google_pagespeed_insight_api_into_the_table_metrics_cumulative_layout_shift_score()


if __name__ == '__main__':
    app.run(debug=True)
