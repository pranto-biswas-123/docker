import os 
from flask import Flask, render_template

app = Flask(__name__)

background_color = os.getenv('BACKGROUND_COLOR', 'green')

@app.route('/')
def index():    
    return render_template('index.html', background_color=background_color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)