import pandas as pd 
import json
import plotly
import requests
import graph

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Landing Page
@app.route("/", methods=['GET','POST'])
def index():
    sep_year_list = '2020'
    sep_programs_list = 'Kids, Teens, Advanced'
    year_list=['2020']
    program_list=['Kids', 'Teens', 'Advanced']

    if request.method == 'POST':
        year_list = request.form.getlist('year')
        program_list = request.form.getlist('program')

    df = graph.filter_data(year_list, program_list)

    sep_year_list = graph.seperate_list(year_list)
    sep_programs_list = graph.seperate_list(program_list)

    graphs = graph.get_graphs(df)
    ids = graph.get_ids(graphs)
    graphJSON = graph.get_json(graphs)

    return render_template('index.html', ids=ids, graphJSON=graphJSON, variable1=sep_year_list, variable2=sep_programs_list)
    
if __name__ == "__main__":
    app.run(debug=True)