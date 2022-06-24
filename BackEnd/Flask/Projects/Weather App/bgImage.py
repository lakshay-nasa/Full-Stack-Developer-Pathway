from ast import Try
from flask import Flask, flash, render_template, request
import requests
import random

app = Flask(__name__)

# Access Key
client_id = "c5AijfSm_8b_JsYU3kuYBtTRdM9Lj_KdOsveYSZQzL8"

@app.route('/', methods=['GET', 'POST'])
def getImage():
    if request.method == "POST":
        try:
            location = request.form['city']
            # API for bg-Image
            # imageKeywordAPI = f"https://api.unsplash.com/search/photos?query={location}&page{random.randint(0, 1000)}&client_id={client_id}"

            imageAPI = f"https://api.unsplash.com/photos/random/?query={location}&client_id={client_id}"

            # Response for bg-Image
            response = requests.get(imageAPI)

            # Data for bg-Image
            data = response.json()

            bg_image = data['urls']['raw']

            return bg_image
        
        except:
            bg_image = "https://api.unsplash.com/photos/random/?client_id={client_id}"
            
            return bg_image

    