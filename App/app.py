from flask import Flask, render_template
import requests
import os
app = Flask(__name__)


 

@app.route("/")
def home():
    if (os.environ.get('SVC')):
        svc_location = os.environ.get('SVC')
        uri = "http://"+svc_location
    else:
        uri = "http://loaclhost:500"
    try:
        response = requests.get(uri)
    except requests.RequestException as e:
           return render_template("home.html", Status=" Service Connection is NOT OK", Response= e, color= "red")


    if response.ok:
       return render_template("home.html", Status=" Service Connection is OK", Response= response.text, color= "green")
    else:
       return render_template("home.html", Status=" Service Connection is NOT OK")

@app.route("/env")
def env():
    for k,v in os.environ.items():
     print(f"{k} : {v}")
    
    return render_template("env.html", env=os.environ)

@app.route("/img")
def ing():
     return render_template("images.html")

if __name__ == '__main__': 
    app.run(host="0.0.0.0")