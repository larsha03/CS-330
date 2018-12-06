import os
import requests
import psycopg2
import records
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for


app = Flask(__name__)

#create a table- insert things into that table

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
        
    if request.form.get("continent"):
        continent = request.form.get("continent")
        order = request.form.get("order")
        query = f"select * from nfl where year='{continent}' order by fortyyd;"

    if request.form.get("region"):
        region = request.form.get("region")
        query = f"select * from nfl where round='{region}';"

    if request.form.get("country"):
        country = request.form.get("country")
        query = f"select * from nfl where position='{country}';"



    result = get_data_from_db(query)
    return render_template("result.html", rows=result)

@app.route("/continent", methods=["GET","POST"])
def continent():

    all_continents = get_data_from_db("select DISTINCT year from nfl;")
    continent = 2012
    query = f"select * from nfl where year='{continent}';"
    result = get_data_from_db(query)
    return render_template("continent.html", options=all_continents, rows=result)  

@app.route("/region", methods=["GET", "POST"])
def region():

    all_regions = get_data_from_db("select DISTINCT round from nfl;")
    region = 3
    query = f"select * from nfl where round='{region}';"
    result = get_data_from_db(query)
    return render_template("region.html", options=all_regions, rows=result)


@app.route("/country", methods=["GET", "POST"])
def country():
    all_countries = get_data_from_db("select DISTINCT position from nfl;")
    country = "CB"
    query = f"select * from nfl where position='{country}';"
    result = get_data_from_db(query)
    return render_template("country.html", options=all_countries, rows=result)



    




if __name__ == "__main__":
    app.run(host="0.0.0.0")