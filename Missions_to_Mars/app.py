from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import mars_scraper

app = Flask(__name__)

mongo = PyMongo(app, url="mongodb://localhost:27017/mars_data")

@app.route("/")
def index():
    mars_db = mongo.db.mars_data.find_one()
    return render_template("index.html", mars=mars_db)
    
# Need to import each scraped function for each of the data types collected

@app.route("/mars_scraper")
def mars_news_scrape():
    mars_db = mars_scraper.nasa_news()
    mongo.db.mars_data.update({}, mars_db, upsert=True)
    return redirect("/", code=302)

