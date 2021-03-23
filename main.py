
from flask import Flask
import random
app = Flask(__name__)

from flask import render_template

@app.route('/hello/')
@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/hi')
def hello_hi():
  return 'Hi!'


if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Starts the site
  host='0.0.0.0', # EStablishes the host, required for repl to detect the site
  port=random.randint(2000, 9000)) # Randomly select the port the machine hosts on