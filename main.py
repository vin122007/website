
from flask import Flask
import random
import requests
app = Flask(__name__)

from flask import render_template

@app.route('/hello/')
@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/hi')
def hello_hi():
  return 'Hi!'

@app.route('/planes')
def planes():
  r = requests.get('https://api.creativecommons.engineering/v1/images?q=cirrussr22')
  print(str(r.status_code))
  print(r.text)
  x = r.json()
  return render_template('planes.html', name="Vinay", data = x)



if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Starts the site 
  host='0.0.0.0', # Establishes the host, required for repl to detect the site
  port=random.randint(2000, 9000)) # Randomly select the port the machine hosts on