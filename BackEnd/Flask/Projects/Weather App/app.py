from flask import Flask, flash, render_template, request
from pip import main

import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        city = request.form['city']
        if city == '':
            return render_template('index.html')
        else:
            api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d670c867d8c8998117536ef9d9abe6fb"
            response = requests.get(api)
            data = response.json()
            temp = round(data['main']['temp'] - 273.15)
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            return render_template('index.html', temp=temp, pressure=pressure, humidity=humidity, city=city)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# api id = d670c867d8c8998117536ef9d9abe6fb
