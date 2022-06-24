from flask import Flask, render_template, request
from bgImage import getImage
import requests

app = Flask(__name__)

API_Key = "Secret_Key"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        city = request.form['city']
        try:
           
            # OpenWeatherMap API
            weatherAPI = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"

            # Response for Weather
            response = requests.get(weatherAPI)
            
            # Data for Weather
            data = response.json()
            temp = round(data['main']['temp'] - 273.15) + "&#8451"
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            iconData = data['weather'][0]['icon']
            weatherDesc = data['weather'][0]['description']
            weatherIcon = f"https://openweathermap.org/img/wn/{iconData}.png"

            return render_template('index.html', caption1="Weather in", temp=temp, caption2= "Humidity",humidity=humidity, caption3= "Pressure", pressure=pressure, city=city, src=getImage(), Icon=weatherIcon, wDesc=weatherDesc)

        except:
            return render_template('index.html')


    return render_template('index.html', src="https://api.unsplash.com/photos/random/?client_id=c5AijfSm_8b_JsYU3kuYBtTRdM9Lj_KdOsveYSZQzL8")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)


# api id = d670c867d8c8998117536ef9d9abe6fb
