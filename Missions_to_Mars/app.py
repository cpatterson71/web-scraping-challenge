from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import mars_scraper

app = Flask(__name__)

mongo = PyMongo(app, url="mongodb://localhost:27017/Mars")

@app.route("/")
def index():
    Mars_data = mongo.db.Mars.find_one()
    return render_template("index.html", mars=Mars_data)
    
# Need to import each scraped function for each of the data types collected
# Where does the Mongo DB come in? is it put into here are created in the app.py?

@app.route("/")
def mars_news_scrape():
    mars_data = mars_scraper.nasa_news()
    mongo.db.Mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if_name__=="__main__"
  app.run(debug=True)