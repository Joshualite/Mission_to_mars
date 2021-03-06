# Import Flask and dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping

# Seting up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Defining route for HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index_challenge.html", mars=mars)


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


if __name__ == "__main__":
    # If running as script, print scraped data
   app.run()

print( mars)