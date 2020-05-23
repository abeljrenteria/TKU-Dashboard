import pandas as pd
import plotly
import data
import plots
import json

def csv_import():
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/1RQjoKJVDzhkEetKvocoNrLoIB0K-wLJlGF4yzHcfpQo/export?format=csv")
    df['date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df['Scholarship Amount'] = df.loc[df['Scholarship'] == 'Y', 'Scholarship Amount'] = df['Workshop Amount'] - df['Amount Paid']
    return df

def filter_data(years, programs):
    df = csv_import()

    # Change str year value in list to int
    year_list = [int(i) for i in years]

    # filter df by values in lists
    df = df[df['Year'].isin(year_list)]
    df = df[df['Program'].isin(programs)]

    return df

def filter_period(df, period):
    df = df[df['Period'] == period]
    return df

def seperate_list(list):
    sep_list = (', '.join(list))
    return sep_list

def get_ids(graphs):
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
    return ids

def get_json(graphs):
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def get_graphs(df):
    indicator_unique = plots.indicator(data.unique_students(df), "Unique Students")
    indicator_total = plots.indicator(data.total_students(df), "Total Students")
    indicator_return_rate = plots.indicator(data.return_rates(df), "Return Rate %")
    indicator_total_revenue = plots.indicator(data.total_revenue(df), "Total Revenue $")
    indicator_scholarship = plots.indicator(data.total_scholarship(df),"Total Scholarships")
    indicator_scholarship_amount = plots.indicator(data.amount_scholarship(df),"Scholarship Amount $")
    line_attendance = plots.line_plot(data.student_attendance(df)[0], data.student_attendance(df)[1], data.student_attendance(df)[2], "Student Attendance", "Workshop Date", "Count")
    line_revenue_2 = plots.line_plot_2(data.revenue_line_data(df)[0], data.revenue_line_data(df)[1], data.scholarship_line_data(df)[1], data.revenue_line_data(df)[2], "Total Revenue by Date", "Workshop Date", "$ Amount")

    graphs=[
        indicator_unique,
        indicator_total,
        indicator_return_rate,
        indicator_total_revenue,
        indicator_scholarship,
        indicator_scholarship_amount,
        line_attendance,
        line_revenue_2
    ]

    return graphs

