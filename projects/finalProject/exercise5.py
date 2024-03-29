import os
import requests
import psycopg2
import records
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for


app = Flask(__name__)


def get_data_from_db(query):
    try:
        conn = psycopg2.connect(
            user="larsha03", host="knuth.luther.edu", port=5432, dbname="larsha03"
        )
    except:
        raise ConnectionError("Could not connect to the database")

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")    
        
    if request.form.get("country"):
        position = request.form.get("position")
        query = f"select * from nfl where Position='{position}';"

    if request.form.get("region"):
        position = request.form.get("round")
        query = f"select * from nfl where Position='{position}';"

    result = get_data_from_db(query)
    return render_template("result.html", rows=result)


@app.route("/continent", methods=["GET","POST"])
def continent():

    all_continents = get_data_from_db("select DISTINCT continent from country order by continent;")
    continent = request.form.get("continent")
    query = f"select * from country where continent='{continent}';"
    result = get_data_from_db(query)
    return render_template("continent.html", options=all_continents, rows=result)  

@app.route("/region", methods=["GET", "POST"])
def region():

    all_regions = get_data_from_db("select DISTINCT region from country order by region;")
    region = request.form.get("region")
    query = f"select * from country where region='{region}';"
    result = get_data_from_db(query)
    return render_template("region.html", options=all_regions, rows=result)


@app.route("/country", methods=["GET", "POST"])
def country():
    all_countries = get_data_from_db("select code, name from country;")
    return render_template("country.html", options=all_countries)



    




if __name__ == "__main__":
    app.run(host="0.0.0.0")