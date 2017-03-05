import os
import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  html = ['<h1>Hello Flask, Docker and Kubernetes!</h1>']
  html.append('<p>The time is: %s</p>' % datetime.datetime.now())
  html.append('<p>I am running on: %s</p>' % os.environ['HOSTNAME'])
  return "\n".join(html)
