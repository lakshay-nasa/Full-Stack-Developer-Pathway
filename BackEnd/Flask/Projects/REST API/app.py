from flask import Flask, jsonify, render_template
from requests import request
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #This will Disable sorting app-wide

s_no = []
id = []
for i in range(1,31):
    s_no.append(i)
    id.append(f"dMinion0{i}")
    i+=1

minions_list = ["Bob", "Carl", "Darwin", "Dave", "Frank", "Jerry", "John","Kevin", "Ken", "Lance", "Larry","Mark", "Mike", "Nobert", "Paul", "Phil", "Steve", "Stuart", "Tim", "Tom", "Chris", "Mel", "Jorge", "Donny"]

food = ["bananas"]

m_data = []

for i in range(len(minions_list)):
    if minions_list[0] == True:
        Hair ="no"
    else:
        Hair = "yes"

    details = {
        "s no.": s_no[i],
        "name": minions_list[i],
        "id": id[i],
        "favourite food" : food[0],
        "hair": Hair,
    }
    i += 1
    m_data.append(details)



@app.route('/')
def home():
    return "<h1> Hello World </h1>"

@app.route('/minions')
def  minions():
    return jsonify({'Minions':m_data})

if __name__ == "__main__":
    app.run(debug=True)
